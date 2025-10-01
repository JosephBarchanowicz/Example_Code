FILEPATH = 'todos.txt'

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file:
        todo_list = file.readlines()
    return todo_list


def write_todos(todos_list, filepath=FILEPATH):
    """ Writes to-do items to a text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_list)


if __name__ == "__main__":
    print(get_todos())