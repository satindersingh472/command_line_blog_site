from http import client
import mariadb
import dbcreds

def ask_username_and_password():
    username = input('Please enter your username: ')
    password = input('Please enter your password: ')
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call find_client_id(?,?)',[username,password])
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    if(len(result) == 1):
        return result[0]
    elif(len(result) == 0):
        print('Invalid username or password')
        return None
    
def insert_post(argument1):
    insert_title = input('Please add title for the post: ')
    insert_content = input('Please add content for the post: ')
    print('Blog post added successfully')
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call insert_post(?,?,?)',[argument1, insert_title, insert_content])
    cursor.close()
    conn.close()
    return 


def all_posts():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call all_posts()')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def infinite_ask():
    while(True):
        print('Option 1 : Will display all the blog posts with the title....')
        print('Option 2 : Will let the user sign in with username and password and user can write title and content for blog post....')
        print('Option 3 and greater: Will let the user exit from the function and print a goodbye message....')
        user_input = input('Please select option 1 or 2 or 3: ')
        try:
            user_input = int(user_input)
            if(user_input == 1):
                posts = all_posts()
                for post in posts:
                    print('The title of the post: ', post[0])
                    print('The content of the post: ', post[1])
                    print('------------------------')
                ask_user = input('Do you want to see options again? (yes/no) ')
                if ask_user in ['','y','yes']:
                    continue
                elif ask_user in ['n','no']:
                    print('You have choose to end the function. See you again...')
                    break
                else:
                    print('Value entered was not valid.So, please proceed further with the options.....enjoy...')
                    continue
            elif(user_input == 2):
                client_id =  ask_username_and_password()
                if(client_id):
                    insert_post(client_id[0])
            elif(user_input <= 0 or user_input >= 4):
                print('Only values from 1 to 3 will show any output, please try again')
                continue
            elif(user_input == 3):
                print('Good bye user have a wonderfull day....')
                break

        except ValueError:
            print('You have selected the value which is not included or it is not an integer, please select from the given numbers(1, 2 or 3)')

infinite_ask()