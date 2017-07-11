import requests
import urllib
from constants import APP_ACCESS_TOKEN,BASE_URL
from get_user_id import get_user_id

from comment import comment_on_a_users_post

def target_a_comment(insta_username):

  user_id = get_user_id(insta_username)



  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)

  print ('GET request url : %s' % (request_url))
  user_media = requests.get(request_url).json()

  service = [ 'clothes','coffee','Ice-cream','Pizza..','dress']
  for post in user_media['data']:
      print(post)
      for serve in service:
          if post['caption'] == None:
              print("No caption")
          else:
              if serve in post['caption']['text']:
                  comment_on_a_users_post(insta_username)
              else:
                  print('Not match by user\'s interst')


