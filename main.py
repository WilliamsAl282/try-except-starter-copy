# Alexander Williams
# 11/21/2024
# Try-Except Block Practice




# Doing addition


# try:
#     first_number = int(input('PLease enter and integer:\n'))
#     second_number = int(input('please enter a second number:\n'))
#     result = first_number + second_number
# except ValueError:
#     print("I asked for a number not a word. Please enter a number")
# else:
#     print(f'The sum of {first_number} and {second_number} is {result}')




# Invalid List Element
    
# my_scores =[]

# try:
#     my_scores.append(int(input('Please enter a score:\n')))
#     print(my_scores)
# except ValueError:
#     print('Invalid input! Please enter a valid integer!')


# Invalid Index
    
my_nums = [10,20,30,40,50,60]

try:
    index_number = int(input('Please enter an index numebr between 0-5:\n'))
    print(f'The index number choosen was {index_number} and that matches with {my_nums[index_number]}')
except IndexError:
    print('Index out of range! Enter an index between 0 and 5 only!')
except ValueError:
    print('Invalid input! Enter an integer only!')