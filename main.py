from get_own_posts import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_posts import get_users_post
from constants import APP_ACCESS_TOKEN, BASE_URL
while True:
    choice = input("Enter you choice: \n1.get own post \n2.get user's information \n3.get user's id \n4.get user's post")
    choice = int(choice)
    if choice == 1:
        get_own_post()
    elif choice == 2:
        insta_username = input("Enter the username of the user: ")
        get_user_info(insta_username)
    elif choice == 3:
        insta_username = input("Enter the username of the user: ")
        get_user_id(insta_username)
    elif choice == 4:
        insta_username = input("Enter the username of the user: ")
        get_users_post(insta_username)
    else:
        print("wrong choice")
RAW Paste Data

# main file.
from get_own_posts import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_posts import get_users_post
from constants import APP_ACCESS_TOKEN, BASE_URL
while True:
    choice = input("Enter you choice: \n1.get own post \n2.get user's information \n3.get user's id \n4.get user's post")
    choice = int(choice)
    if choice == 1:
        get_own_post()
    elif choice == 2:
        insta_username = input("Enter the username of the user: ")
        get_user_info(insta_username)
    elif choice == 3:
        insta_username = input("Enter the username of the user: ")
        get_user_id(insta_username)
    elif choice == 4:
        insta_username = input("Enter the username of the user: ")
        get_users_post(insta_username)
    else:
        print("wrong choice")
