from Modules import functions
import time

x=time.strftime("%b %d, %Y %H:%M:%S")
print("It is now",x)
while True:
    user_action = input("Type add <new to do>, show, edit <to do #>, complete or exit:")

    if user_action.startswith("add"):
        todo = user_action[4:]+"\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item=item.strip('\n')
            print(f"{index+1}- {item.capitalize()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])-1
            new_todo = input("Enter new:")

            todos = functions.get_todos()

            todos[number]=new_todo+'\n'

            functions.write_todos(todos)

        except ValueError:

            print("Your command is not valid")

            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])-1

            todos = functions.get_todos()

            todo_removal = todos[number].strip('\n')
            todos.pop(number)

            todos = functions.get_todos()

            print(f"Todo:{todo_removal} is removed")

        except IndexError:

            print("Item number does not exist")

            continue

    elif user_action.startswith("exit"):

        break

    else:

        print("Command is not valid")

print("Bye!")