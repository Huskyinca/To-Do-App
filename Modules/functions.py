def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as filex:
        todosx = filex.readlines()
    return todosx

def write_todos(todos_arg,filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
    return todos_arg
