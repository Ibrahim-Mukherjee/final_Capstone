# Task Manager Program
# By Asabeneh

# files
# user.txt
# username1,password1
# username2,password2

# tasks.txt
# username,task_title,task_description,due_date,completion_status

# helper functions

def display_options():
    print('''
        r - register new user
        a - add task
        va - view all tasks
        vm - view my tasks
        s - display statistics
        e - exit
    ''')

def get_username_password():
    username = input('Enter your username:')
    password = input('Enter your password:')
    return username, password

def validate_user(username, password):
    with open('user.txt', 'r') as file:
        users = file.readlines()
        for user in users:
            user_info = user.split(',')
            if username == user_info[0] and password == user_info[1].strip():
                return True, user_info[0]
        return False, ''

# Function to read user data from user.txt file
def read_user_data():
    with open("user.txt") as file:
        users = {}
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password
    return users

# Function to read task data from tasks.txt file
def read_task_data():
    with open("tasks.txt") as file:
        tasks = []
        for line in file:
            task_data = line.strip().split(",")
            tasks.append(task_data)
    return tasks

# Function to write task data to tasks.txt file
def write_task_data(task_data):
    with open("tasks.txt", "a") as file:
        file.write(",".join(task_data) + "\n")

# Function to register a new user
def register_user(users):
    while True:
        username = input("Enter a new username: ")
        if username in users:
            print("That username is already taken. Please choose another username.")
        else:
            break
    password = input("Enter a password: ")
    users[username] = password
    with open("user.txt", "a") as file:
        file.write(username + "," + password + "\n")
    print("User registered successfully!")

# Function to display all tasks
def view_all_tasks(tasks):
    for task in tasks:
        print(f"Assigned to: {task[0]}")
        print(f"Title: {task[1]}")
        print(f"Description: {task[2]}")
        print(f"Due date: {task[3]}")
        print(f"Completed: {task[4]}")
        print()

# Function to display tasks assigned to the user who is logged in
def view_my_tasks(username, tasks):
    user_tasks = []
    for task in tasks:
        if task[0] == username:
            user_tasks.append(task)
    if not user_tasks:
        print("No tasks assigned to you.")
    else:
        for task in user_tasks:
            print(f"Title: {task[1]}")
            print(f"Description: {task[2]}")
            print(f"Due date: {task[3]}")
            print(f"Completed: {task[4]}")
            print()

# Function to display statistics
def display_statistics(users, tasks):
    num_users = len(users)
    num_tasks = len(tasks)
    print(f"Number of users: {num_users}")
    print(f"Number of tasks: {num_tasks}")
    
# Main function
def main():
    print("Welcome to the task manager.")
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if validate_user(username, password):
            break
        else:
            print("Incorrect username or password. Please try again.")
    while True:
        print("Menu:")
        print("r - Register new user")
        print("a - Add task")
        print("va - View all tasks")
        print("vm - View my tasks")
        print("e - Exit")
        choice = input("Enter your choice: ")
        if choice == "r":
            register_user()
        elif choice == "a":
            add_task()
        elif choice == "va":
            view_all_tasks()
        elif choice == "vm":
            view_my_tasks(username)
        elif choice == "e":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please try again.")

    users = read_user_data()
    tasks = read_task_data()
    logged_in = False
    username = ""

    while not logged_in:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in users and password == users[username]:
            logged_in = True
        else:
            print("Invalid username or password. Please try again.")
    
    print(f"Welcome, {username}!")

    if username == "admin":
        while True:
            choice = input("Enter r to register a new user, a to add a task, va to view all tasks, vm to view your tasks, s to display statistics, or e to exit: ")
            if choice == "r":
                register_user(users)
            elif choice == "s":
                display_statistics ()

          



