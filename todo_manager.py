# 1. Start with a pre-populated list of 3 tasks
list_of_tasks = ["Walk the dog", "Clean room", "wash dishes"]

# 2. Display the current to-do list (numbered, starting from 1)s
print('Current List')
for number,task in enumerate(list_of_tasks, start=1):
 print(f'{number} {list_of_tasks}')

print("Number of current tasks")
print(len(list_of_tasks))

# 3. Let the user add a new task (append)
user_input = input("Enter a new task: ")
list_of_tasks.append(user_input)

# 4. Let the user remove a task by number (pop)
# Add error handling: We are given ValueError
# The plan of attack is...
'''
try:
  CODE. 
except ErrorMessage:
  print('This message is triggred if the error occurs')

'''
try:
    remove_number = int(input("Enter the number of the task you want to remove"))
    remove_task = list_of_tasks.pop(remove_number-1)
    print(f'You removed: ', {remove_task})
except ValueError:
  print('You need to type the number of the task you want to remove. Do not type text.')

# 5. Display the updated list after each operation
print('Updated List')
for number,task in enumerate(list_of_tasks, start=1):
  print(f'{number} {list_of_tasks}')

# 6. Show the total number of tasks remaining.
print(f'Number of current tasks {len(list_of_tasks)}')
