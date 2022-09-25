from sqlite3 import Cursor
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
        return None
    

# client_id = ask_username_and_password()
# if(client_id):
#     print(client_id[0])
# else:
#     print('credentials do not match with any username in database')

def insert_post(argument1):
    insert_title = input('Please add title for the post: ')
    insert_content = input('Please add content for the post: ')
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call insert_post(?,?,?)',[argument1, insert_title, insert_content])
    cursor.close()
    conn.close()
    return 

# print(insert_post(client_id[0]))

def all_posts():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call all_posts()')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

posts = all_posts()

# for post in posts:
#     print(post)

def infinite_ask():
    while(True):
        user_input = input('Please select option 1 or 2 or 3: ')
        if(user_input == '1'):
            for post in posts:
                 print(post)
        elif(user_input == '2'):
            client_id =  ask_username_and_password()
            insert_post(client_id[0])
        else:
            print('goodbye')
            break

infinite_ask()