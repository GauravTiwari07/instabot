import requests
from constants import BASE_URL, APP_ACCESS_TOKEN
from get_user_posts import get_users_post
from get_user_id import get_user_id


def get_list_of_comments_on_users_post(username):
    post_id = get_user_id(username)
    req_url = BASE_URL + 'media/' + post_id + '/comments?access_token=' + APP_ACCESS_TOKEN
    comments_here = requests.get(req_url).json()
    print('The comments on this post are : \n')
    if comments_here['meta']['code'] == 200:
            for i in range(len(comments_here['data'])):
                print(comments_here['data'][i]['from']['username'], end=' : ')
                print(comments_here['data'][i]['text'])
                print()
    else:
            print('Status code other than 200!!!')

