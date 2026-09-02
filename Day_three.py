# problem one 
# Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when we read it forward & backward. Eg -
# “madam”, “racecar” etc.


""" def palindrom(string):
    rev ="" 
    for i in string:
        rev = i + rev 
    if rev == string:
        print("the string is palindrome")
    else:
        print("the string is not palindrome")
    
if __name__ == "__main__":
    string = str(input("enter the string : "))
    palindrom(string) 
    """

# problem two
# Given a list of integers compute the average of all numbers in the list.
"""
def avg_list(list):
  sum = 0 
  for i in list:
     sum = sum + i
     average = sum / len(list)
  print("Average of list : ",average)


if __name__== "__main__":
    list =[1,2,3,4,5,6]
    avg_list(list)
    """

# problem three
# Input two lists of integers from the user. Merge them into one list and sort the result.
# Eg - list1 = [1, 2, 7] , list2 = [2, 4, 5] result = [1,2,4,5,7]
# Take two lists of integers from the user
""" 
list1 = list(map(int,input("enter ist list (separated spaces )").split()))
list2 = list(map(int,input("enter 2nd list (separated spaces )").split()))

merge = list1 + list2
result = sorted(set(merge))   # sorted() guarantees order; set() removes duplicates
print(result)
"""

# problem four 
# Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers
""" numbers = (1,2,3,4,5,6,7,8,9,10)
even  = tuple(n for n in numbers if n % 2 == 0 )
odd = tuple(n for n in numbers if n % 2 != 0 )
print(even)
print(odd)
""" 


# problem five 
#Q5. Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where user presses a key ( A, ‘B , ‘C , ‘D ) depending on the operation they want to perform on the dictionary:
# 1. A - Add a student
#. B - Update marks
# . C - Search for a student
# . D - Display all students and marks

""" 
student = {}
def add_student():
    std_name = input("Enter student name : ").strip()
    if std_name in student:
        print("student already exist .")
        return 
    try:
        marks = int(input(f"enter marks for  {std_name}   "))
    except ValueError:
        print("Invalid input : marks must be integers .")
        return 
    student[std_name] = marks
    print("*"*35)
    print(f"Student Added {std_name } ----> {marks}")
    print("*"*35)




def update_student():
    std_name = input("enter student name :")
    if std_name not in student:
        print("student not found in the record")
        return
    try:
        marks = int(input("enter new marks for the studnet : "))
    except ValueError :
        print("marks must be integers")
        return
    student[std_name] = marks
    print("*"*35)
    print("student marks are update . ")
    print("*"*35)



def search_Student():
    std_name = input("enter the studnet name ").strip()
    if std_name  in student:
        print(f"student  found  {std_name}.")
    else:
       print("student not found in the record .")



def Display_student():
    if not student:
        print("no record found of the student.")
        return
    print("Students marks")
    for std_name, marks in student.items():
        print(f"{std_name}{marks}")
        print("-" * 26)



def main():
    while True:
        print("Welcome to the program")
        print("A. Add student")
        print("B. Update marks")
        print("C. Search for a student")
        print("D. Display all student and  marks")
        print("E. Exit ")
        choice = input("enter your choice : ").strip().upper()
        if choice == "A":
            add_student()
        elif choice == "B":
            update_student()
        elif choice == "C":
            search_Student()
        elif choice == "D":
            Display_student()
        elif choice == "E":
            break



if __name__ == "__main__":
    main()
        
""" 
# problem six
# Create a dictionary that maps each word to its length.
""" 
words =["jawad","Ayesha","zakir","abbas","murad"]
dic = {}
for i in words:
    length = len(i)
    dic[i] = length
print(dic)
"""


# problem 7
# Write a program that takes a string from the user and prints the number of spaces in the string.
"""
user_input = str(input("enter string (this program count the number of space in your string ) : "))
count = 0
for i in user_input:
    if i == " ":
        count+=1
print("number of space in your string   =",count)
"""