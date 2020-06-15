import os
import json
import random
import string
from urllib.request import urlopen
from urllib.error import URLError, HTTPError


ALL_DATA_PATH = 'all_data.txt'


def create_db():
    """
    This function checks whether you have the db file saved locally, and if not it creates it
    :return: text file containing empty dictionary
    """
    if not os.path.exists(ALL_DATA_PATH):
        return_data_to_file({})


def custom_url(user_url, user_custom_url):
    """
    This function receives an original url and custom url and return an Error if needed
    :param user_url:
    :param user_custom_url:
    :return:
    """
    if short_url_in_db(user_custom_url):
        if get_key_from_value(user_custom_url) == user_url:
            return user_custom_url
        return 'ERROR - custom url already exist'
    elif not validate_web_url(user_url):
        return 'ERROR - url is not valid. Check yourself'
    add_new_url_to_dict(user_url, user_custom_url)
    return user_custom_url


def url_length():
    """
    This function is responsible for managing the url length we randomize
    :return: string stands for the shortened url length
    """
    shortened_url_length = 3
    num = len(import_data_to_dict())//26**shortened_url_length
    while num:
        shortened_url_length += 1
        num = num//26
    return shortened_url_length


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


def url_exist_in_db(user_url):
    """
    This function checks if the url already exist in out db
    :param user_url: the given url from the user
    :return: boolean param. False if it does not exist and True if it does
    """
    return user_url in import_data_to_dict().keys()


def short_url_in_db(user_custom_url):
    """

    :param user_custom_url:
    :return:
    """
    return user_custom_url in import_data_to_dict().values()


def get_key_from_value(custome_url):
    my_dict = import_data_to_dict()
    for key,value in my_dict.items():
        if custome_url == value:
            return key


def validate_web_url(url):
    """
    This function validate the given url by trying to open the url and catching possible errors
    :param url: user url
    :return: error index
    """
    if not (url.startswith('http://') or url.startswith('https://')):
        url = 'http://%s' % url
    try:
        urlopen(url)
        return True
    except ValueError:
        return False
    except HTTPError:
        return False
    except URLError:
        return False


def get_shorten_url_from_dict(user_url):
    """
    This function receives url and return the shortened url we created
    :param user_url: the user url
    :return: string of shorten url
    """
    return import_data_to_dict()[user_url]


def get_origin_url(shorten_url):
    """
    This function receives a shorten url and return the original url that was given from the user
    :param shorten_url: shorten url
    :return: the original url
    """
    for key, value in import_data_to_dict().items():
        if shorten_url == value:
            return key


def create_shortened_url(user_url):
    """
    This function receives the user url and randomize a new shorten url with the relevant length
    :param user_url: the user url
    :return: new shorten url
    """
    letters = string.ascii_lowercase
    shorten_url = ''.join(random.choice(letters) for i in range(url_length()))
    if shorten_url in import_data_to_dict().values():
        return create_shortened_url(user_url)
    add_new_url_to_dict(user_url, shorten_url)
    return shorten_url


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


def get_shorten_url(user_url):
    """
    This function receives the user url and returns the shorten url, whether if it exists already or not
    :param user_url: the user url
    :return: the shorten url
    """
    if url_exist_in_db(user_url):
        return get_shorten_url_from_dict(user_url)
    elif not validate_web_url(user_url):
        return 'ERROR - url is not valid. Check yourself'
    return create_shortened_url(user_url)

