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
