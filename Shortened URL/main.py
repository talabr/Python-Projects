import json
import random
import string

all_data_dict = {}
NEW_URL_LENGTH = 8


def import_data_to_dict():
    with open('all_data.txt') as json_file:
        data_dict = json.load(json_file)
    return data_dict


def return_data_to_file(data_dict):
    with open('all_data.txt', 'w') as my_file:
        json.dump(data_dict, my_file)


def url_exist(user_url):
    if user_url in all_data_dict.keys():
        return True
    else:
        return False


def get_shorten_url_from_dict(user_url):
    return all_data_dict[user_url]


def shortened_url(user_url):
    # return 'blah blah'
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(NEW_URL_LENGTH))


def add_new_url_to_dict(user_url):
    all_data_dict[user_url] = 'our_domain/'+shortened_url(user_url)
    print("added url")


def handle_user_request(user_url):
    if url_exist(user_url):
        print("The given url already exist in our system.")
        print('Your shortened url: %s' % (get_shorten_url_from_dict(user_url)))
    else:
        add_new_url_to_dict(user_url)
        print('Your new shortened url: %s ' % (all_data_dict[user_url]))


def main():
    global all_data_dict
    all_data_dict = import_data_to_dict()  # now I have all the file data in a dict
    user_url = (input("Enter your url: ")).replace("'", "")
    # now I need to check if the url already exists in my dict
    handle_user_request(user_url)
    return_data_to_file(all_data_dict)


if __name__ == '__main__':
    main()

