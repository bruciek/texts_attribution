import pandas as pd
from tqdm import tqdm
import json
import compress_pickle
import os

from preprocessing.features.features_lemma_part_speech import get_feature_lemma_part_speech
from preprocessing.features.features_with_word_count import get_feature_symbol
from preprocessing.features.features_with_sentence_list import get_feature_sents
from preprocessing.features.features_words import get_feature_word
from preprocessing.features.features_bin import get_feature_bin
from preprocessing.features.features_text import get_feature_text

from preprocessing.features.features_words import func_words
from preprocessing.features.features_with_sentence_list import FUNC_LIST
from preprocessing.features.features_with_word_count import func_chars
from preprocessing.features.features_lemma_part_speech import func_lemma_part_speech
from preprocessing.features.features_bin import func_bin
from preprocessing.features.features_text import func_text


all_func = FUNC_LIST + func_words + func_chars + func_lemma_part_speech + func_bin + func_text
path = os.getcwd()


def get_list_of_features(doc):
    features_symbol = get_feature_symbol(doc)
    features_words = get_feature_word(doc)
    features_sents = get_feature_sents(doc)
    features_lemma_part_speech = get_feature_lemma_part_speech(doc)
    features_bin = get_feature_bin(doc)
    features_text = get_feature_text(doc)
    list_of_features = features_sents + features_words + features_symbol + features_lemma_part_speech + features_bin + features_text
    return list_of_features


def dataset_target(dataset):
    authors = list(set(dataset['authors']))
    dict_authors = dict()
    reverse_dict_authors = dict()
    for index in range(len(authors)):
        dict_authors[authors[index]] = index
        reverse_dict_authors[index] = authors[index]
    target = []
    for author in dataset["authors"]:
        target += [dict_authors[author]]
    return target


def dataset_output(data_path : str, json_file = "docs_info.json", books_folder = "Обработанные"):
    """
    :param data_path: Absolute path to Данные folder.
    :param json_file: json filename.
    :param books_folder: Folder with books inside Данные folder.
    :return: csv file in current directory.
    """
    observations = []
    with open(os.path.join(data_path, json_file), "r") as f_docs_info:
        docs_info = json.load(f_docs_info)
        authors = docs_info["authors"]
        file_names = docs_info["file_name"]
        for i, file_name in enumerate(tqdm(file_names)):
            author = authors[i]
            doc = compress_pickle.load(os.path.join(data_path, books_folder, file_name))

            features = get_list_of_features(doc)
            observation = features + [author]
            observations.append(observation)

    df_features = pd.DataFrame(observations, columns=all_func + ["targets"])
    df_features.to_csv('output.csv', index=False)
