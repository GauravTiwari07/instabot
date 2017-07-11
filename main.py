from get_own_posts import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_posts import get_users_post
from constants import APP_ACCESS_TOKEN, BASE_URL
from recent_media_liked_by_self import recent_media_liked_by_self
from self_info import self_info
from like_user_posts import like_a_post
from comment import comment_on_a_users_post
from list_comments import get_list_of_comments_on_users_post
import time
menu = "\nChoose from the following options:\n1.View your own details\n2.Get user_id of an instagram user\n" \
       "3.Retrieve Your latest post\n4.Retrieve a user's latest post\n5.Recent media liked by you\n" \
       "6.Like a user's post\n7.Get List of comments on a user's post\n8.Comment on a user's post\n9.exit\n"
# creating High level design of function show_menu()
def show_menu():
    insta_username = input("Enter the username for which you want to perform these actions")
    if len(insta_username) > 0:
        choice = int(input(menu))
        if choice == 1:
            self_info()
        elif choice == 2:
            user_id = get_user_id(insta_username)
            print(user_id)
            show_menu()
        elif choice == 3:
            own_post_id = get_own_post()
            print(own_post_id)
            show_menu()
        elif choice == 4:
            user_post_id = get_users_post(insta_username)
            print(user_post_id)
            show_menu()
        elif choice == 5:
            recent_media_liked_by_self()
            show_menu()
        elif choice == 6:
            like_a_post(insta_username)
            show_menu()
        elif choice == 7:
            get_list_of_comments_on_users_post(insta_username)
            show_menu()
        elif choice == 8:
            comment_on_a_users_post(insta_username)
            show_menu()
        elif choice == 9:
            exit(code="Application Closed")
        else:
            exit(code="You did'nt entered one of the choices above")
    else:
        exit(code="You have to enter a username")


show_menu()
