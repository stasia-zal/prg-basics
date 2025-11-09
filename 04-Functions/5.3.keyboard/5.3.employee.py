###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
import key

# Reads employee's data from keyboard
first_name = key.input_string('Enter name: ')
last_name = key.input_string('Enter last name: ')
age = key.input_integer('Enter age: ')
salary = key.input_real('Enter salary: ')
is_salary_hidden = key.input_boolean('Hide salary? (y/n): ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name: ', last_name)
print('Age: ', age)
if not is_salary_hidden:
    print('Salary: ',salary)