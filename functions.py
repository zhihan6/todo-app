def get_todos(filepath="files/todos.txt"):
    """ Read a text file and return the list of to-do items. """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)