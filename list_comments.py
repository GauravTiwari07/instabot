import requests
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_posts import get_users_post

def get_list_of_comments_on_users_post(insta_username):
    post_id =  get_users_post(insta_username)
    print("post_id = ", post_id)
    request_url = BASE_URL + "media/{}/comments?access_token={}".format(post_id, APP_ACCESS_TOKEN)
    print("Requesting:\n{}".format(request_url))
    comments_on_this_post = requests.get(request_url).json()
    if comments_on_this_post["meta"]["code"] == 200:
        for i in range(len(comments_on_this_post)):
            print(comments_on_this_post["data"][i]["from"]["username"], end=" : ")
            print(comments_on_this_post["data"][i]["text"])
            print()
    else:
        print("Status code other than 200")