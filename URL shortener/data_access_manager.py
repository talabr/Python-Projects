import os
import json

URLS_DATA_FILE_NAME = 'urls_data.json'


def create_urls_db():
    if not os.path.exists(URLS_DATA_FILE_NAME):
        insert_urls_data_to_db({})


def get_urls_data_from_db():
    with open(URLS_DATA_FILE_NAME, 'r') as json_file:
        data_dict = json.load(json_file)
    json_file.close()
    return data_dict


def insert_urls_data_to_db(data_dict):
    with open(URLS_DATA_FILE_NAME, 'w') as my_file:
        json.dump(data_dict, my_file)


def add_url_to_db(user_url, short_url):
    all_data_dict = get_urls_data_from_db()
    all_data_dict[user_url] = short_url
    insert_urls_data_to_db(all_data_dict)


def is_user_url_exist_in_db(user_url):
    return user_url in get_urls_data_from_db().keys()


def is_short_url_exist_in_db(short_url):
    return short_url in get_urls_data_from_db().values()


def get_short_url_by_user_url(origin_url):
    return get_urls_data_from_db()[origin_url]


def get_user_url_by_short_url(short_url):
    for key, value in get_urls_data_from_db().items():
        if short_url == value:
            return key


def count_num_of_keys_in_json():
    with open(URLS_DATA_FILE_NAME, 'r') as json_file:
        data_dict = json.load(json_file)
    return len(data_dict.keys())
