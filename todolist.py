todolistdata = []

# Function to display the To-Do List
def todolist(data):
    if not data:
        return []

    result = []

    for idx, item in enumerate(data, start=1):
        status = "Done" if item["status"] == "done" else "Not done"
        result.append(f"{idx}. {item['task']} ({status})")

    return result

# Function to get user input and add task to the list
def user_input():
    task = input("Enter the task you want to do: ")
    status = "not done"
    todolistdata.append({'task': task, 'status': status})

# Function to change task status
def change_status(data):
    if not data:
        print("\nTo-Do list is still empty\n")
        return

    for item in todolist(data):
        print()
        print(item)

    try:
        choice = int(input("Enter the task number: "))
        if 1 <= choice <= len(data):
            user = input("Change to Done or Not Done? (Done/Not): ")

            if user.lower() == "done":
                data[choice - 1]['status'] = 'done' if data[choice - 1]['status'] == 'not done' else 'not done'
            elif user.lower() == "not":
                data[choice - 1]['status'] = 'not done' if data[choice - 1]['status'] == 'done' else 'done'
            else:
                print("Invalid option")

            print("\nStatus updated successfully\n")
        else:
            print("Invalid number")
    except ValueError:
        print("\nInput must be a number\n")

# Function to delete a task from the list
def delete(data):
    if not data:
        print("\nTo-Do list is still empty")

    for item in todolist(data):
        print()
        print(item)

    try:
        choice = int(input("Enter the task number to delete: "))
        if 1 <= choice <= len(data):
            data.pop(choice - 1)
            print("Task successfully deleted")
        else:
            print("Invalid number")
    except ValueError:
        print("\nInput must be a number")

# Main loop
while True:
    print("\n\nTo-Do List\n")
    print("=================================================================")
    for item in todolist(todolistdata):
        print(item)
    print("=================================================================")
    print("\n1. Add Task")
    print("2. Change Task Status")
    print("3. Delete Task")

    user = input("Select an option (1/2/3): ")
    if user == "1":
        user_input()
    elif user == "2":
        change_status(todolistdata)
    elif user == "3":
        delete(todolistdata)
    else:
        print("\nInvalid option\n")
