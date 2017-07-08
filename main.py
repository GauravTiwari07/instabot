from get_own_posts import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_posts import get_users_post
from constants import APP_ACCESS_TOKEN, BASE_URL
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
            own_post_id = get_recent_posts()
            print(own_post_id)
            show_menu()
        elif choice == 4:
            user_post_id = get_user_recent_posts(insta_username)
            print(user_post_id)
            show_menu()
        elif choice == 5:
            recent_media_liked_by_self()
        elif choice == 6:
            like_a_users_post(insta_username)
        elif choice == 7:
            get_list_of_comments_on_users_post(insta_username)
        elif choice == 8:
            comment_on_a_users_post(insta_username)
        elif choice == 9:
            exit(code="Application Closed")
        else:
            exit(code="You did'nt entered one of the choices above")
    else:
        exit(code="You have to enter a username")


show_menu()