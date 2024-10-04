list =[1,2,1]

list_copy = list.copy()
list_copy.reverse()

if(list == list_copy):
    print("Given input is palindrome")
else:
    print("Given input is not a palindrome")
