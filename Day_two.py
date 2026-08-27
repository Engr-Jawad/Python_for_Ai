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

    
           
        

