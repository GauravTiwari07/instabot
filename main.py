from get_own_posts import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_posts import get_users_post
from constants import APP_ACCESS_TOKEN, BASE_URL
from self_info import self_info
from comment_on_post  import comment_on_a_users_post
from list_comments import get_list_of_comments_on_users_post
while True:
    choice = input("Enter you choice:\n1.gey self information \n2.get own post \n3.get user's information \n4.get user's id \n5.get user's post")
    choice = int(choice)
    if choice == 1:
        self_info()
    elif choice == 2:
        get_own_post()
    elif choice == 3:
        insta_username = input("Enter the username of the user: ")
        get_user_info(insta_username)
    elif choice == 4:
        insta_username = input("Enter the username of the user: ")
        get_user_id(insta_username)
    elif choice == 5:
        insta_username = input("Enter the username of the user: ")
        get_users_post(insta_username)
    else:
        print("wrong choice")
        exit(0)
