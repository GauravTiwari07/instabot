import requests
import urllib3
from constants import APP_ACCESS_TOKEN, BASE_URL
from get_user_id import get_user_id

def get_users_post(insta_username):
    #function logic
    user_id = get_user_id(insta_username)
    if user_id is None:
        print('The user does not exist')
        exit()
    req_url = BASE_URL + 'users/' + user_id + '/media/recent/?access_token=' + APP_ACCESS_TOKEN
    media_user = requests.get(req_url).json()
    if media_user['meta']['code'] == 200:
        if len(media_user['data']):
            rec_img = media_user['data'][0]['images']['standard_resolution']['url']
            urllib3.disable_warnings()
            conn = urllib3.PoolManager()
            response = conn.request('GET', rec_img)
            f = open('user_post.jpg', 'wb')
            f.write(response.data)
            f.close()
            print('Your post was downloaded')
        else:
            print('Post does not exist!')
    else:
        print('Status code other than 200 received!')


print(get_users_post("eviledmpredator"))