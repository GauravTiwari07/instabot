import requests
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_posts import get_users_post

# full fledged function to print the id of media liked by self
def recent_media_liked_by_self():
    request_url = BASE_URL + "users/self/media/liked?access_token={}".format(APP_ACCESS_TOKEN)
    print("Requesting:\n{}".format(request_url))
    media_liked = requests.get(request_url).json()
    if media_liked["meta"]["code"] == 200:
        if len(media_liked["data"]) > 0:
            print(media_liked["data"][0]["id"])
        else:
            print("No media to show")
    else:
        print("Status code other than 200")
