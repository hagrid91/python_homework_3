'''
Python Homework Assignment 3
'''

def numbers_comp(num1,num2,num3):
    if (int(num1)==int(num2)) or (int(num2)==int(num3)) or (int(num3)==int(num1)):
        return True
    else:
        return False

print(numbers_comp(6,"6",5))


