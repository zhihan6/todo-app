# from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        print("add something!")
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            print(f"{index + 1}-{item}")

    elif user_action.startswith('edit'):
        try:
            todos = functions.get_todos()
            number = int(user_action[5:]) - 1
            todos[number] = input("THe new todo is: ") + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:]) - 1
            todos = functions.get_todos()
            todo_to_remove = todos.pop(number).strip('\n')
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

            functions.write_todos(todos)

        except IndexError:
            print("There is no such index")
            continue

    elif user_action.startswith('exit'):
        break




