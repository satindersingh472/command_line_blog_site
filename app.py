#import database
import mariadb
#import credentials from dbcreds file
import dbcreds
#below function will take the input for username and password from user
#it will connect to the database and open the cursor
#execute the stored procedures with given username and password as a arguments
#the result from the database will get stored inside result 
#then close the cursor and connection in an order
#if there is any user associated with the given username and password 
#the function will return result[0] otherwise none will be returned
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
        print('Sign in is successfull')
        print('Welcome,',result[0][1])
        return result[0]
    elif(len(result) == 0):
        print('Invalid username or password')
        return None

#insert post will take title and content as inputs from user after successfull sign in  
#it will connect to database and open the cursor and execute the stored procedures
#after executing it will close the cursor and connection and print the statement
#and return the function
def insert_post(argument1):
    insert_title = input('Please add title for the post: ')
    insert_content = input('Please add content for the post: ')
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call insert_post(?,?,?)',[argument1, insert_title, insert_content])
    cursor.close()
    conn.close()
    print('Blog post added successfully')
    return 

#all posts will display all the post in the database
#it will connect to database and open the cursor and execute the stored procedure
#it will store the data from stored procedures inside the result variable 
#after getting and storing data it will close the cursor and connection and return the result
def all_posts():
    conn = mariadb.connect(user=dbcreds.user, password=dbcreds.password, host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
    cursor = conn.cursor()
    cursor.execute('call all_posts()')
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

#infinite ask is the function that will have while loop and call the functions base on input
def infinite_ask():
    #while loop will continue to work until we break it 
    while(True):
        print('Option 1 : Will display all the blog posts with the title....')
        print('Option 2 : Will let the user sign in with username and password and user can write title and content for blog post....')
        print('Option 3 and greater: Will let the user exit from the function and print a goodbye message....')
        user_input = input('Please select option 1 or 2 or 3: ')
        #based on inputs the loop will try different conditions and try or except methods will prevent the code
        try:
            #the user input will get converted to integer value
            user_input = int(user_input)
            #if user enters 1 then post variable will execute all posts and store the data inside posts itself
            if(user_input == 1):
                posts = all_posts()
                #there will be many posts inside posts variable then it will take the help of loop to display all posts
                for post in posts:
                    print('The title of the post: ', post[0])
                    print('The content of the post: ', post[1])
                    print('------------------------')
                    #after writing all the posts it will ask user to further choose from 3 options
                    #based on user input if yes then the while loop will continue otherwise not
                ask_user = input('Do you want to see options again? (yes/no) ')
                if ask_user in ['','y','yes']:
                    continue
                elif ask_user in ['n','no']:
                    print('You have choose to end the function. See you again...')
                    break
                else:
                    print('Value entered was not valid.So, please proceed further with the options.....enjoy...')
                    continue
                #if user enters 2 then it will execute the function ask_username_and_password()
            elif(user_input == 2):
                client_id =  ask_username_and_password()
                #if it returns something then insert post function will get executed with the argument
                #containing the client id from the ask_username_and_password()
                if(client_id):
                    insert_post(client_id[0])
                    #if user enters integer 0 or less than 0 OR 4 or greater than 
                    #it will show the message to enter correct value and continue the loop
            elif(user_input <= 0 or user_input >= 4):
                print('Only values from 1 to 3 will show any output, please try again')
                continue
            #if user enters 3 then loop will break and print a goodbye message
            elif(user_input == 3):
                print('Good bye user have a wonderfull day....')
                break
                #if user enters any other option than integer while selecting options 1, 2 or 3
                #then the value error will show the error message
        except ValueError:
            print('You have selected the value which is not included or it is not an integer, please select from the given numbers(1, 2 or 3)')

infinite_ask()