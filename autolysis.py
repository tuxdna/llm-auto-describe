# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
#   "pandas",
#   "numpy",
#   "matplotlib",
#   "tabulate",
#   "seaborn",
# ]
# ///


import pandas as pd
import numpy as np
import httpx
import sys
import json
import os
import matplotlib.pyplot as plt

import textwrap
from dataclasses import dataclass

"""
Description of task:

This should create, in your current directory, the following files:

 * A single Markdown file called README.md with results of your automated analysis, written as a story.
 * 1-3 charts as PNG providing supporting data visualizations. Name them as *.png. Add the images in your README.md.

Tasks:
 * Do generic analysis that will apply to all datasets. 
   For example, summary statistics, counting missing values, correlation matrices,
    outliers, clustering, hierarchy detection, etc.

"""


@dataclass
class PromptStore:
    plot_feature_preamble: str = textwrap.dedent(f"""
        Write python code to plot a histogram with following data provided as JSON.
        In the JSON below, there is:
          * field "feature_name" that is name of the feature
          * field "hist_values" which represent values of the histogram
          * field "hist_bins" which represent edges of the bins for which histogram values are provided
          * field "output_plot_file" which is name of where plot should be written to

        Use the JSON as is from below provided data. Do not load any file.
        Save plot to a file named using the field "output_plot_file" from JSON.
        Do not output anything else except the Python code. 

        """)

    description_preamble = textwrap.dedent(f"""
        From data samples, and dataset description given below below, describe the dataset in detail.
        Provide the answer in well formatted markdown raw text that can be copied as is.
        Make sure there is an headline summarizing the dataset at the end of markdown.

        """)

    select_features_preamble = textwrap.dedent(f"""
        From data samples, and dataset description given below below, select name of only numeric features.
        Select those features that we can use to create histogram plots. Keep other features at the end of list.
        Do not return features that are unsuitable for histogram plots.
    
        Provide the answer in JSON list that can be eval()'d as is. Do not nest the output.

        """)

    @classmethod
    def create_summary(cls, csv_dataframe: pd.DataFrame):
        # summarize the dataset and build a prompt to describe the data
        ten_samples = csv_dataframe.sample(10)

        data_description = textwrap.dedent(f"""
            Shape of data: {csv_dataframe.shape}

            Data types of all features:
            {csv_dataframe.dtypes}

            Null counts of all features:
            {csv_dataframe.isna().sum()}

            Descriptive stats of numeric features:
            {csv_dataframe.describe()}

            Ten samples are provided below after separator marked with dashes.
            Do not output anything else.

            ------------

            {ten_samples.to_markdown(tablefmt="pipe")}
        """)
        return data_description


def execute_prompt(user_prompt: str, api_key: str, system_prompt: str = None):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", }
    data = {
        "model": "gpt-4o-mini",
        "messages": [{
            "role": "user",
            "content": user_prompt
        }],
        "temperature": 0.7
    }

    client = httpx.Client(timeout=None)
    response = client.post(url, headers=headers, json=data)
    resp_json = response.json()
    print(resp_json)
    return resp_json["choices"][0]["message"]["content"]


def ensure_markdown_text(input_text):
    if input_text.startswith('```markdown') or input_text.startswith('```'):
        output = "\n".join(input_text.split("\n")[1:-1])
        is_markdown = True
    else:
        output = input_text
        is_markdown = False

    return output, is_markdown


def ensure_python_script(input_text):
    if input_text.startswith('```python'):
        output = "\n".join(input_text.split("\n")[1:-1])
        is_python = True
    else:
        output = input_text
        is_python = False

    return output, is_python


def ensure_json_response(input_text):
    if input_text.startswith('```json'):
        output = "\n".join(input_text.split("\n")[1:-1])
        is_python = True
    else:
        output = input_text
        is_python = False

    return output, is_python


def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("CSV file path is required as first argument to the script.")
        sys.exit(1)

    # Load csv file provided as input
    csv_path = sys.argv[1]
    print(f"Loading file: {csv_path}")
    try:
        csv_dataframe = pd.read_csv(csv_path)
    except UnicodeDecodeError as e:
        # 'utf-8' codec can't decode byte 0xe9 in position 532: invalid continuation byte
        csv_dataframe = pd.read_csv(csv_path, encoding='latin-1')
    except pd.errors.EmptyDataError as e:
        print("CSV is empty.")
        sys.exit(0)

    # Load API key from environment variable
    api_key = os.environ.get("AIPROXY_TOKEN", "")

    # To build final README.md we will keep this list as incremental buffer
    markdown_list = []

    # Build a prompt to analyze the data from some samples.
    data_summary = PromptStore.create_summary(csv_dataframe)
    description_prompt = f"{PromptStore.description_preamble}\n{data_summary}"

    # print(f"description_prompt\n{description_prompt}")
    description_response = execute_prompt(description_prompt, api_key=api_key)
    print(f"{description_response=}")
    description_md, _ = ensure_markdown_text(description_response)
    markdown_list.append(description_md)

    # select features to plot
    select_features_prompt = f"{PromptStore.select_features_preamble}\n{data_summary}"
    select_features_response = execute_prompt(select_features_prompt, api_key=api_key)
    print(f"{select_features_response=}")
    pyscript, _ = ensure_json_response(select_features_response)
    selected_features = eval(pyscript)
    print(f"{selected_features=}")

    markdown_list.append(textwrap.dedent(f"""
        # Histogram of features: {selected_features}
        
        Let us explore some of these features below
        
    """))

    feature_count = 0
    for feature_name in selected_features:
        if feature_count >= 3:
            print(f"Completed analyzing {feature_count} features. Continue...")
            break

        try:
            print(f"Analyze: {feature_name}")
            hist_values, bin_edges = np.histogram(csv_dataframe[feature_name], bins=10)
            feature_hist_data = {
                "feature_name": feature_name,
                "hist_values": hist_values.tolist(),
                "bin_edges": bin_edges.tolist(),
                "output_plot_file": f"{feature_name}.plot.png"
            }
            feature_count += 1
            plot_prompt = f"{PromptStore.plot_feature_preamble}\n{json.dumps(feature_hist_data, indent=2)}"
            plot_response = execute_prompt(plot_prompt, api_key=api_key)
            print(f"{plot_response=}")

            script_py, _ = ensure_python_script(plot_response)

            exec("\n".join(plot_response.split("\n")[1:-1]))

            plot_file_path = feature_hist_data["output_plot_file"]

            markdown_list.append(textwrap.dedent(f"""
                    ## Plot of feature: {feature_name}
                    
                    ![{plot_file_path}]({plot_file_path})
                    
                    """))
        except ValueError as e:
            print("Skip this feature")
            continue

    output_readme_file = "README.md"
    print(f"Writing output: {output_readme_file}")
    with open(output_readme_file, "w") as f:
        f.write("\n".join(markdown_list))


if __name__ == "__main__":
    main()
