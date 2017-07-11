import requests
import urllib3
from constants import BASE_URL, APP_ACCESS_TOKEN

def get_own_post():
    #function logic
        req_url = BASE_URL + 'users/self/media/recent/?access_token=' + APP_ACCESS_TOKEN
        media_self = requests.get(req_url).json()

        if media_self['meta']['code'] == 200:
            if len(media_self['data']):
                rec_img = media_self['data'][0]['images']['standard_resolution']['url']
                urllib3.disable_warnings()
                conn = urllib3.PoolManager()
                response = conn.request('GET', rec_img)
                f = open('own_post.jpg', 'wb')
                f.write(response.data)
                f.close()
                print('Your post was downloaded')
            else:
                print('Post does not exist!')
        else:
            print('Status code other than 200 received!')
