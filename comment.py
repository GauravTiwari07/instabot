import requests
import urllib
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_posts import get_users_post
from get_user_id import get_user_id

def get_post_id(insta_username):
    # program logic.
    user_id = get_user_id(insta_username)
    if user_id is None:
        print('User does not exist!')
        exit()
    req_url = BASE_URL + 'users/' + user_id + '/media/recent/?access_token=' + APP_ACCESS_TOKEN
    user_media = requests.get(req_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print('There is no recent post of the user!')
            exit()
    else:
        print('Status code other than 200 received!')
        exit()

def comment_on_a_users_post(insta_username):
    post_id = get_post_id(insta_username)
    print("post_id = ", post_id)
    request_url = BASE_URL + "media/{}/comments".format(post_id)
    print("Requesting:\n{}".format(request_url))
    comment_to_post = input("Enter your comment: ")
    comment = requests.post(request_url, data={'access_token': APP_ACCESS_TOKEN, 'text': comment_to_post}).json()
    print(comment)
    if comment['meta']['code'] == 200:
        print("comment was successful")
    else:
        print("comment not successful")
