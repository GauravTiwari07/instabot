import requests
import urllib
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_posts import get_users_post
def comment_on_a_users_post(insta_username):
    post_id = get_users_post(insta_username)
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
comment_on_a_users_post("eviledmpredator")