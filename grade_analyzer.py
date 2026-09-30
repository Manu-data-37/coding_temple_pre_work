
# Starts with this list of student scores:

scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]

# Adding counters
A = 0
B = 0
C = 0
D = 0
F = 0

for score in scores:
  if score  > 90:
    print("A")
    A += 1
  elif score >= 80:
    print("B")
    B += 1
  elif score >= 70:
   print("C")
   C += 1
  elif score >= 60:
   print("D")
   D += 1
  else:
   print("F")
   F += 1

'''
PASS & FAIL SCORES
Scores over 60 pass
Scores below 60 fail
'''
passing_grade = A + B + C + D
failing = F


# Data Manipulation for grade_analyzer

# Total Scores
total_scores = len(scores)
average = round(sum(scores) / len(scores ),1)
highest = max(scores)
lowest = min(scores)


# Grade Analyzer
print('Grade Analyzer')
print('Total Scores', total_scores)
print('Average', average )
print('Highest',highest)
print('Lowest', lowest)
print('Passing', passing_grade)
print('Failing', failing)


# Counts how many students are in each letter grade category
print('Grade Distributions')
print('A', A, 'students')
print('B', B, 'students')
print('C', C, 'students')
print('D', D, 'students')
print('F', F, 'students')

# Adding More Scores
while True:
  user_input = input('Enter a score (or \'done\' to finish): ')

  if user_input.lower() == 'done':
    print('The program has ended')
    break

  try:
    new_input = int(user_input)
  except ValueError:
    print('Enter an Integer')
    continue

  scores.append(new_input)
  updated_avg = round(sum(scores) / len(scores ),1)
  print('Your Updated Average is: ', updated_avg)


 




