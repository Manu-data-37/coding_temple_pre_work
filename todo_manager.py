# TODO: Start with a pre-populated list of 3 tasks
# TODO: Display the current to-do list (numbered, starting from 1)
# TODO: Let the user add a new task (append)
# TODO: Let the user remove a task by number (pop)
# TODO: Display the updated list after each operation
# TODO:Show the total number of tasks remaining


# DONE: Start with a pre-populated list of 3 tasks
list_of_tasks = ["Clean room", "Go to the doctor", "Washo dishes"]

# DONE: Display the current to-do list (numbered, starting from 1)
for number, task in enumerate(list_of_tasks, start=1):
  print(f'{number} {task}')


# TODO: Let the user add a new task (append)
print('Do you want to ADD or REMOVE a task?')
user_input = input('Type what you want to do')

if user_input.upper() == 'ADD':
  new_task = input('What do you want to add?')
  list_of_tasks.append(new_task)
  print(f'Added: {new_task}')

# TODO: Let the user remove a task by number (pop)

elif user_input.upper() == 'REMOVE':
  try:
    remove_task = int(input('Enter the number of the task you want to remove'))
    removed_task = list_of_tasks.pop(remove_task - 1)
    print(f'Removed: {remove_task}')
  except ValueError:
    print('Type a number, not  text')
  except IndexError:
    print('That number is not on the list')
else:
  print('An error has occured. Restart the program!')

# TODO: Display the updated list after each operation
# TODO:Show the total number of tasks remaining

# Updated list of tasks
print(f'Your tasks are: {len(list_of_tasks)}')
print(f'Updated list of tasks {list_of_tasks}')


