import sqlite3
import getpass

# підключення до бази даних
conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# створення таблиць, якщо вони не існують
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')
c.execute('''CREATE TABLE IF NOT EXISTS tasks
             (id integer primary key autoincrement, title text, description text)''')

# функція для створення нового користувача
def register():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hash_password(password)
    c.execute("INSERT INTO users VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("User registered successfully.")

# функція для хешування паролю
def hash_password(password):
    # реалізуйте ваш алгоритм хешування паролю тут
    return password

# функція для перевірки пароля
def check_password(username, password):
    c.execute("SELECT password FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result is not None:
        hashed_password = result[0]
        return hashed_password == hash_password(password)
    else:
        return False

# функція для створення нового завдання
def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    c.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
    conn.commit()
    print("Task created successfully.")

# функція для видалення завдання за ідентифікатором
def delete_task():
    task_id = input("Enter task id: ")
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    print("Task deleted successfully.")

# функція для зміни завдання за ідентифікатором
def edit_task():
    task_id = input("Enter task id: ")
    new_title = input("Enter new task title (press enter to keep the existing title): ")
    new_description = input("Enter new task description (press enter to keep the existing description): ")
    c.execute("UPDATE tasks SET title=?, description=? WHERE id=?", (new_title, new_description, task_id))
    conn.commit()
    print("Task updated successfully.")

# функція для перегляду списку всіх завдань
def view_tasks():
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    for task in tasks:
        print("Task #{}: {} - {}".format(task[0], task[1], task[2]))

while True:
    print("\nWhat would you like to do?")
    print("1. Login")
    print("2. Register")
    print("3. Create new task")
    print("4. Delete task")
    print("5. Edit task")
    print("6. View all tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")
        if check_password(username, password):
            print("Login successful.")
        else:
            print("Invalid username or password.")

    elif choice == "2":
        register()

    elif choice == "3":
        create_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        edit_task()

    elif choice == "6":
        view_tasks()

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
