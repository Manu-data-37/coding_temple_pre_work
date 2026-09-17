# Storing personal data on variables

first_name = 'Manuel'
age = 29
city = 'Mexico City'
previous_career = 'Operations Intern at TikTok'
fun_fact = 'I am creating a farm of schnauzer dogs'
why_code = 'I want to learn to build AI and start a new career'


print('=' * 40)
print('Student Profile')
print('=' * 40)

# Manipulating the data with an f-string
print(f''' Name: {first_name}'
      'Age: '{age} 
      'City: '{city}
      'Previous career: ' {previous_career}''')

# using an escape sequene \ to debug the first print statement
print("Why I\'m learning to code:")
print(why_code)
print('Fun fact!',fun_fact)



