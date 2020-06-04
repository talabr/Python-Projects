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


def get_new_url():
    user_url = input("Enter your url: ")
    handle_user_request(user_url)
    print(url_dict)
    
 
def go_to_url():
    adress = input("enter the url:\n")
    if not adress.startswith('"our_domain/'):
        print("error! url not legal")
    adress = adress[len("our_domain/ "):-1]
    for key in all_data_dict.keys():
        if adress == all_data_dict[key]:
            my_url = key
            webbrowser.open(my_url)
            return
    print("error! unknown adress")


def main() :
    while 1:
        choice=input("choose 1 get a new url \nchoose 2 to use your new url \nchoose 3 to exit\n")
        if int(choice)==1 :
            get_new_url()
        elif int(choice)==2:
            go_to_url()
            break
        elif int(choice)==0:
            break
        else:
            print("error! please enter 1,2 or 3")
            continue


if __name__ == '__main__':
    main()

