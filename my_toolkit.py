


# calculate_average(numbers) — Takes a list of numbers, returns the average. Returns 0 if the list is empty.

nums = [70, 10,80,100]


def calculate_average(numbers):
   if not numbers:
      return 0
   return sum(numbers) / len(numbers)
  

 # find_max_and_min(numbers) — Takes a list of numbers, returns a tuple (max_value, min_value). Do NOT use the built-in max() and min() — implement the logic yourself with a loop.

def find_max_and_min(numbers):
   if not numbers:
      return (None,None)

   max_value = numbers[0]
   min_value = numbers[0]

   for n in numbers:
      if n > max_value:
         max_value = n
      if n < min_value:
         min_value = n

   return (max_value,min_value)
  
# count_occurrences(items, target) — Takes a list and a target value, returns how many times the target appears in the list. Do NOT use the built-in .count() method.
def count_occurrences(items, target):

  count = 0
  for item in items:
     if item == target:
        count += 1
  return count

# is_palindrome(text) — Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces). Examples: "racecar" → True, "hello" → False, "A man a plan a canal Panama" → True.
def is_palindrome(text):
   correct = text.replace(" ","").lower()
   return correct == correct[::-1]

# create_report(title, scores) — Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally. Returns a formatted string report (NOT a print — a return).

def create_report(title, scores):
    average = calculate_average(scores)
    max_value , min_value = find_max_and_min(scores)

    return (

       f'Scores: {scores}\n'
       f'Average: {average:.2f}\n'
       f'Highest: {max_value}\n'
       f'Lowest: {min_value}\n'
    )

report = create_report("Quiz", nums)
print(report)