# Problem one 
# Using conditional statements,
# calculate the final tax rate based on these rules:

"""""
salary = float(input("enter your salary : "))
if salary < 30000:
    tax_rate = 5
elif salary < 70000:
    tax_rate = 15 
else:
    tax_rate = 25

tax_amount = (salary * tax_rate)/100
final_salary = salary - tax_amount
print("Tax Amount : ",tax_amount)
print("Salary : ",final_salary)
"""""



# problem two 
# Write a function that takes two integers a and b and prints all even numbers b/w them.
""""
def print_even(numone,numtwo):
    minn = min(numone,numtwo)
    maxx = max(numone,numtwo)
    for i in range(minn,maxx):
        if i % 2 == 0 :
            print(i," ")


if __name__ == "__main__":
    numone = int(input("Enter the ist number : "))
    numtwo = int(input("Enter the 2nd number : "))


print_even(numone,numtwo)
"""




# problem three
# Q3. Write a function that prints the digits of a number, n .
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.
"""def print_digits(number):
    if number ==  0 :
        print(0)
        return 
    else:
        digits = number % 10
        print(digits)
        number = number // 10



if __name__ == "__main___":
    number = float(input("enter number :"))
    print_digits(number)
    """

# problem four 
# Write a function to return the count the number of digits in a number, n .
""" def count_digits(number ):
    if number ==  0 :
            print(0)
            return 
    digitss = []
    while number > 0 :
          digits = number % 10
          digitss.append(digits)
          number = number // 10
    print("length of number : ",len(digitss))
          
        
number = int(input("enter number :"))
count_digits(number) 
"""

# problem five 
# Write a function to return the sum of digits of a number, n .
""" def sum_of_digits(number):
    if number < 0:
        print(0)
        return 
    sum=0
    while number > 0 :
        dig = number % 10
        sum+=dig
        number = number // 10
    print(sum)
        


if __name__ == "__main__":
    number = int(input("enter number : "))
    sum_of_digits(number)
    """
# problem six
# Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.


""" def div_by_3_and_5(number):
    for i in range (1,101):
        if (i % 3 == 0) | (i % 5 == 0):
            print(i,end = " ")
    

if __name__ == "__main__":
    number = 1 
    div_by_3_and_5(number)
        """

# problem seven
# Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”.
""" def check_positive_negative():
    while True:
        user_input = (input("enter number or (Quit press Q) : "))
        if user_input.lower() == "quit":
            print("your are exit from the program .")
            break 
        
        try:
                number = int(user_input)
                if number < 0:
                    print("number is negative")
                elif number > 0:
                    print("number is postive")
                else:
                    print("number is zero")
        except ValueError:
            print("invalid number or input ")



if __name__ == "__main__":
    check_positive_negative()
"""


# problem 8
# let’s create a Simple Calculator that performs arithmetic operations.
""" def Calculator(numone,operator,numtwo):
    if operator == "+":
        add = numone + numtwo
        print("add : ",add)
    elif operator == "-":
        sub = numone - numtwo
        print("sub :",sub)
    elif operator == "*":
        mul = numone * numtwo
        print("mul : ",mul)
    elif operator == "/":
        div = numone / numtwo
        print("div : ",div)
    else:
        print("invalid operator")

if __name__ == "__main__":
    numone = int(input("ente ist number : "))
    operator = input("enter operator : ")
    numtwo = int(input("enter 2nd operator : "))
    Calculator(numone,operator,numtwo)
   """
    