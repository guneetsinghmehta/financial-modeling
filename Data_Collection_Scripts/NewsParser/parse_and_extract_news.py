from __future__ import print_function
import json, os

def list_files_in_directory(dir_name):
    return [f for f in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name, f))]

def extract_news(dir_name, files):
    if not os.path.exists("weburls"):
        os.makedirs("weburls")
    for file_name in files:
        with open(os.path.join(dir_name, file_name), "r") as f:
            ticker = file_name.split(".")[0]
            lines = f.readlines()
            if len(lines) == 0:
                continue
            # print(len(lines))
            json_data = json.loads(lines[0])
            docs = json_data['response']['docs']
            # print("docs length = ", len(docs))
            output_file = open("weburls/" + ticker + ".txt", "w")
            for data in docs:
                if data['snippet'] is None or data['web_url'] is None:
                    continue
                print(data['web_url'], file=output_file)


if __name__ == "__main__":
    extract_news("newsdata", list_files_in_directory("newsdata"))
