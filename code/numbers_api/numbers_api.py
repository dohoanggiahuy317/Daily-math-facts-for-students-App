import requests
import json
import logging
import argparse
import pandas as pd
import os


def get_api_content(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content = response.json()  # Parse the response as JSON
        return content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return -1


def write_data(content, output_filename):
    # Check if the file exists
    file_exists = os.path.isfile(output_filename)
    new_df = pd.DataFrame(content)

    if not file_exists:
        # File does not exist, create it with header
        new_df.to_csv(output_filename, mode='w', index=False, header=True)
    else:
        # File exists, append data without header
        new_df.to_csv(output_filename, mode='a', index=False, header=False)
    
    return


def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from the file {file_path}.")



def scraping(info, origin_url, output_filename):

    for data_type, v in info.items():
        start, end = v["start"], v["end"]

        for i in range(start, end, 100):
            url = origin_url + str(i) + ".." + str(i+100) + "/" + data_type
            try:
                content = get_api_content(url)

                if content != -1:
                    logging.info(f"Successfully scrape URL: {url}")

                    data = {"url": [], "text": []}
                    for k, line in content.items():
                        data['url'].append(origin_url + str(k) + "/" + data_type)
                        data['text'].append(line)
                    # data['url'].append(url)
                    # data['text'].append(" ".join(list(content.values())))
                    write_data(data, output_filename)
            except Exception as e:
                logging.error(f"Error processing URL {url}: {e}")


def main():

    parser = argparse.ArgumentParser(description='Scrap content from a link')
    parser.add_argument('--original_url', type=str, help='link of the root url')
    parser.add_argument('--json_filename', type=str, help='stoping threshold', default=2)
    parser.add_argument('--output_filename', type=str, help='path to content file in csv')
    args = parser.parse_args()


    # Setup logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    # Setup scrape data
    origin_url = args.original_url
    info = read_json(args.json_filename)

    # Start scraping
    scraping(info, origin_url, args.output_filename)


if __name__=='__main__':
    main()