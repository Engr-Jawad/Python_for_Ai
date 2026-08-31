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
    
