import random
import string

url_dict = {}


def url_exist(url):
    if url in url_dict.keys():
        return True
    return False


def get_shorten_url_from_dict(user_url):
    return url_dict[user_url]


def shortened_url(user_url):
    return 'blah'


def add_new_url_to_dict(user_url):
    url_dict[user_url] = shortened_url(user_url)


def handle_user_request(user_url):
    if url_exist(user_url):
        print("The given url already exist in our system.")
        print('Your shortened url: %s' % (get_shorten_url_from_dict(user_url)))
    else:
        add_new_url_to_dict(user_url)
        print('Your new shortened url: %s ' % (url_dict[user_url]))


def main():
    user_url = input("Enter your url: ")
    handle_user_request(user_url)
    print(url_dict)


if __name__ == '__main__':
    main()

