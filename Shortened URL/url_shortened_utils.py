import os
import json
import random
import string

ALL_DATA_PATH = 'all_data.txt'


def create_db():
    """
    This function checks whether you have the db file saved locally, and if not it creates it
    :return: text file containing empty dictionary
    """
    if not os.path.exists(ALL_DATA_PATH):
        return_data_to_file({})


def import_data_to_dict():
    """
    This function reads the data from the txt file and saves it as a dict
    :return: dictionary
    """
    with open(ALL_DATA_PATH, 'r') as json_file:
        data_dict = json.load(json_file)
    return data_dict


def return_data_to_file(data_dict):
    """
    This function dumps all the data in the dict, back to the txt file
    :param data_dict: dictionary with all our used url's
    :return: nothing
    """
    with open(ALL_DATA_PATH, 'w') as my_file:
        json.dump(data_dict, my_file)


def add_new_url_to_dict(user_url, new_shortened_url):
    """
    This function receives the user url and a shorten url and adds it to the dict and dumps to the txt file
    :param user_url: the user url
    :param new_shortened_url: new shorten url
    :return: nothing
    """
    all_data_dict = import_data_to_dict()
    all_data_dict[user_url] = new_shortened_url
    return_data_to_file(all_data_dict)


def is_origin_url_exist_in_db(user_url):
    """
    This function checks if the url already exist in out db
    :param user_url: the given url from the user
    :return: boolean param. False if it does not exist and True if it does
    """
    return user_url in import_data_to_dict().keys()


def is_shorten_url_exist_in_db(short_url):
    """

    :param short_url:
    :return:
    """
    return short_url in import_data_to_dict().values()


def get_shorten_url_from_origin_url(origin_url):
    """
    This function receives url and return the shortened url we created
    :param origin_url: the user url
    :return: string of shorten url
    """
    return import_data_to_dict()[origin_url]


def get_origin_url_from_shorten_url(shorten_url):
    """
    This function receives a shorten url and return the original url that was given from the user
    :param shorten_url: shorten url
    :return: the original url
    """
    for key, value in import_data_to_dict().items():
        if shorten_url == value:
            return key


def get_random_url_length():
    """
    This function is responsible for managing the url length we randomize
    :return: string stands for the shortened url length
    """
    shortened_url_length = 3
    num = len(import_data_to_dict()) // 26 ** shortened_url_length
    while num:
        shortened_url_length += 1
        num = num // 26
    return shortened_url_length


def validate_web_url(url):
    """
    This function validate the given url by trying to open the url and catching possible errors
    :param url: user url
    :return: error index
    """
    return url.startswith('http://') or url.startswith('https://') or url.startswith('www.')


def create_random_word():
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for i in range(get_random_url_length()))
    return random_word


def create_random_shorten_url(origin_url):
    """
    This function receives the user url and randomize a new shorten url with the relevant length
    :param origin_url: the user url
    :return: new shorten url
    """
    random_shorten_url = create_random_word()
    while is_shorten_url_exist_in_db(random_shorten_url):
        random_shorten_url = create_random_word()
    add_new_url_to_dict(origin_url, random_shorten_url)
    return random_shorten_url


def get_random_shorten_url(origin_url):
    """
    This function receives the user url and returns the shorten url, whether if it exists already or not
    :param origin_url: the user url
    :return: the shorten url
    """
    if is_origin_url_exist_in_db(origin_url):
        return get_shorten_url_from_origin_url(origin_url)
    return create_random_shorten_url(origin_url)


def save_custom_shorten_url(origin_url, custom_url):
    """
    This function receives an original url and custom url and return an Error if needed
    :param origin_url:
    :param custom_url:
    :return:
    """
    if not is_shorten_url_exist_in_db(custom_url):
        add_new_url_to_dict(origin_url, custom_url)
    elif not get_origin_url_from_shorten_url(custom_url) == origin_url:
        return 'ERROR - custom url is taken'
    return custom_url


def get_shorten_url(origin_url, custom_url=None):
    if not validate_web_url(origin_url):
        return 'ERROR - url is not valid. Check yourself'
    if custom_url:
        return save_custom_shorten_url(origin_url, custom_url)  # returns error string or random string
    return get_random_shorten_url(origin_url)
