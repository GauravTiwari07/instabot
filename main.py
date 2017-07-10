from get_own_posts import get_own_post
from get_user_id import get_user_id
from get_user_info import get_user_info
from get_user_posts import get_users_post
from constants import APP_ACCESS_TOKEN, BASE_URL
from self_info import self_info
from comment  import comment_on_a_users_post
from list_comments import get_list_of_comments_on_users_post
from like_user_posts import like_a_post
def instabot():
    while True:
        print('\n')
        print('Hello and welcome to Instabot!!!!!!!!')
        print('Whom do you want to use the application for ??? \nEnter \'self\' or username : ')
        user = input()
        if user == 'self':
            while True:
                print('You can perform the following functions....')
                print('1. Get your own details')
                print('2. Get your own recent post')
                print('3. Get to the previous menu')
                choice = eval(input('Enter your choice : '))
                if choice == 1:
                    self_info()

                elif choice == 2:
                    get_own_post()

                elif choice == 3:
                    break

                else:
                    print('You did not enter a valid choice!')

        else:
            while True:
                print('You can perform the following functions....')
                print('1. Get the details of the user')
                print('2. Get the recent post of the user')
                print('3. Like the recent post of a user')
                print('4. Comment on the recent post of a user')
                print('5. Delete negative comments from the recent pot of a user')
                print('6. Get back to the previous menu')

                choice = eval(input('Enter your choice : '))

                if choice == 1:
                    get_user_info(user)

                elif choice == 2:
                    get_users_post()

                elif choice == 3:
                    like_a_post()

                elif choice == 4:
                    comment_on_a_users_post()

                elif choice == 5:
                     get_user_id()

                elif choice == 6:
                    get_list_of_comments_on_users_post()

                    break

                else:
                    print('You did not enter a valid choice')


instabot()

