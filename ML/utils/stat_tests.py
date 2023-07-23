import json
import os
import compress_pickle
import pandas as pd
from tqdm import tqdm


def get_authors_texts(data_path):
    authors_texts = dict()
    with open(os.path.join(data_path, "docs_info.json"), "r") as f_docs_info:
        docs_info = json.load(f_docs_info)
        file_names = docs_info["file_name"]
        authors_texts["targets"] = docs_info["authors"]
        authors_texts["texts"] = []
        for file_name in tqdm(file_names):
            doc = compress_pickle.load(os.path.join(data_path, "Обработанные", file_name))
            authors_texts["texts"].append(doc.text)

    return pd.DataFrame(authors_texts)


def get_merged_texts(df, group_by="targets"):
    return df.groupby(group_by).agg({"texts": " ".join}).reset_index()

