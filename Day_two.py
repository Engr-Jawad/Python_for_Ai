# Problem one 
# Using conditional statements,
# calculate the final tax rate based on these rules:
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