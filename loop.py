'''Loops in python'''

''' Q1 In Given list Count how many number are postive,negativ ,ZerO and non-zero'''

# number_list=[0,1,-2,3,-4,5,6,0,-7,-8,9,10]

# postive_no_count=0
# Negative_no_count=0
# zero_value=0
# non_zero=0

# for numbe_list in number_list:

#  if numbe_list>0:
#     postive_no_count+=1
#  elif numbe_list<0 :
#     Negative_no_count+=1

#  else :
#     zero_value+=1


# print('Postive Number in a list :',postive_no_count)
# print('Negative Number in a list :',Negative_no_count)
# print('Zero in a list :',zero_value)
# print('non-zero value in a list :',postive_no_count + Negative_no_count)

'''Q2.Sum of even number till n'''

# n=int(input())
# sum_of_even=0

# for i in range(1,n+1):
#     if(i%2==0):
#         sum_of_even+=i

# print(sum_of_even)


'''Q3.print the multiplication table for a given number upto 10,but skip the fifth iteration'''

# number=int(input("enter no you want to get table of\n"))

# #2x1=2
# #2x2=4

# for i in range(1,11):
   
#     if i==5: 
#      continue
#     print(number,"x",i ,'=',number*i)
      


'''Q3.Reverse a string'''


# str=input("string you want to reverse\n")
# reverse_str=""

# for char in str:
#     reverse_str=char+reverse_str


# print(reverse_str)


'''Q.4 Find the first Non Reapted character in a String'''
 
# str=input()

# for char in str:
#     print(char)
#     if str.count(char)==1:
#          print("first non repeated character is :"+ char)

#          break


'''Q.5 compute the factorial of given number'''
 
# n=5
# fact=1
# # for i in range(1,n+1):
# #  fact*=i
# # print(fact)

# while n >0:
#     fact=fact*n
#     n-=1

# print(fact)

'''Q.6 validate input keepasking the user for input until they enter a number between 1 and 10'''



# while True:
#     a=int(input("enter a number\n"))
#     if a<=10:
#         break


'''Q7.No prime Number or Not'''

 
# no=int(input("enter number \n"))
# print("--------------")
# for i in range(2,no):
#    if no%i==0:
#       print(no,"Not prime")
#       break

#    else: 
#       print(no,"is Prime")  
#       break


'''Q.8. Take a list of name from these list you need which name contain higher no of character'''

#exmple :input
#name_list=["sanskar","ankit","abhieshk","sajalpandeyhioklp"]
#:output :abhieshk

# names_list = ['John', 'Emma', 'Michael', 'Jessica', 'William']

# Find the name with the highest number of characters
#max_name = max(name_list, key=len)

# print("Name with the highest number of characters:", max_name)


# nam_list=list(input())
# print(nam_list.split())
# print(type(nam_list))


# name=["aman","sanskar","muskan"]
# for i in name:
#     print(i.count())
#     b=i.split()
#     print(i,"contain no character",b.count())

'''Q.9 Check all element in a list are unique ,if duplicate is found,exit the loop and print the duplicates'''
# a=["mango","banana","kivi",'banana',"mango"]
# unique_item=set()

# for item in a:
#     if item in unique_item:
#         print("duplicates in a list :",item)

#     unique_item.add(item)    
# # print('unique items are ',unique_item)



# 

# for i in range(10):
#     print(i)


# a=['sanskar','mishra','from','bhopal']

# a[1:2]="pandey".split()
# # behind the scene loops
# print(a)

