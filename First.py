# str1 = "this is my computer hello everyone"
# str2 = 'this is my computer'
# str3 = '''hello everyone'''

# str1 = "This is my string.\n we are craeting it in python."
# print(str1)

# str2 = "This is my string.\t we are creating it in python"
# print(str2)

# str1 = "apna"
# str2 = "collage"

# print(str1+str2)


# str1 = "my"
# str2 = "girl"
# final_str = str1+str2
# print(final_str)

# str1 = "Apna"
# len1 = len(str1)
# print(len1)

# str2 = "Collage"
# len2 = len(str2) 
# print(len2) 

# str1 = "Apna"
# str2 = "Collage"
# final_str = str1 + "  " + str2
# print(final_str)
# print(len(final_str))

# str = "Apna collage"
# print(str[0])

# print(str[7])
  

# str = "Apna collage"
# print(str[1:4])

# str = "Apna collage"
# print(str[:4])
# print(str[2:])


# str = "Apna collage"
# print(str[-6:-2])


# str = "I am studying python from Apna collage"
# print(str.endswith("age"))


# str = "i am ashmita jha studying in parul university"
# print(str.capitalize())
# print(str)

# str = "i am studying from apna college"
# str = str.capitalize()
# print(str)

# str = "i am studying python from apna college"
# print(str.replace("o", "a"))

# str = "i am studying python from apna collage"
# print(str.find("am"))
# print(str.find("python"))

# str = "I am studying javascript from apna college"
# print(str.count("a"))


# name = input("enter your name:")
# print("length of your name is", len(name))

# name = input("enter your college name :")
# print("length of your college name is", len(name))


# str = "my name is $$$ and i am living in newyork $$$ and usa currency $"
# print(str.count("$"))

age = 25

# if(age >= 18):
#     print("can drive vehicles and eligible for voting and license")

num = 8

# if(num > 2):
#     print("greater than 2")

# elif(num > 3):
#     print("greater than 3")

# Light = "pink"

# if(Light == "red"):
#     print("stop")
# elif(Light == "green"):
#     print("go")
# elif(Light == "yellow"):
#     print("look")
# else:
#     print("light is broken")

# print("end of code")           

# marks = int(input("enter student marks : "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "D"

# print("end of grading ->", grade)        

# age = 21

# #nesting
# if(age >= 18):
#     if(age >= 80):
#         print("cannot drive")
# else:
#     print("can drive")


# a = int(input("enter the first number : "))
# b = int(input("enter the second number : "))
# c = int(input("enter the third number : "))

# if(a > b and a > c):
#     print("first number is greater" , a)
# elif(b > c):
#     print("second number is greater", b) 
# else:
#     print("third number is greater" , c)       

# str = int(input("enter a number: "))

# rem = str % 7
# if(rem == 0):
#     print("yes")
# else:
#     print("no")    



# marks1 = 92.1
# marks2 = 88.2
# marks3 = 95.5
# marks4 = 81.5
# marks5 = 94.8
# marks6 = 99.0

# marks = [92.1, 88.2, 95.5, 81.5, 94.8, 99.0]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[5])
# print(len(marks))


# student = ["pravin", 19, 95.2, "kolkata"]
# print(student)
# student[0] = "arjun"
# print(student)

# marks = [55, 89, 90, 92, 96, 58,]
# print(marks[1 : 4])
# print(marks[:5])
# print(marks[2:])
# print(marks[-5:-2])

# list = [2,4,5,8,6,0]
# list.append(1)
# print(list)

# list = [4,6,9,1,0,5]
# list.sort()
# print(list)

# list = [2,9,0,5,8,1]
# print(list.sort(reverse=True))
# print(list)

# list = ['d' , 'h' , 't' , 'o' , 'j' , 'e']
# list.sort(reverse=True)
# print(list)

# list = ['f', 'o', 'g', 'n', 's', 'x']
# list.reverse()
# print(list)

# list = [2,8,4,3,0,1]
# list.insert(2,9)
# print(list)

# list = [3,5,1,9,6,4]
# list.remove(5)
# print(list)

# list = [4,7,1,0,3,2,6]
# list.pop(4)
# print(list)

# tup = (5,7,3,1)
# print(type(tup))

# tup = (5,9,1,0,3)
# print(tup[0])
# print(tup[3])
# tup[2] = 4

# tup = ()
# print(tup)
# print(type(tup))

# tup = (1)
# print(tup)
# print(type(tup))

# tup = (3,7,1,9,0,5)
# print(tup[2:5])

# tup = (2, 8, 1, 6, 0, 5 )
# print(tup.index(6))

# tup = (4, 5, 5, 7, 1, 0 )
# print(tup.count(5))

# movie1 = str(input("enter name 1 movie: "))
# movie2 = str(input("enter name 2 movie: "))
# movie3 = str(input("enter name 3 movie: "))
# list = (movie1, movie2, movie3)
# print(list)

# movies = []
# mov1 = input("enter 1st movie: ")
# mov2 = input("enter 2nd movie: ")
# mov3 = input("enter 3rd movie: ")
 
# movies.append(mov1)
# movies.append(mov2) 
# movies.append(mov3)

# print(movies)

# list1 = [1, 2, 1]
# list2 = [1, 2, 3]

# copy_list1 = list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("palindrome")
# else:
#     print("NOT palindrome")   

# name = "Ashmita"
# age = 19
# price = 29.55
# old = True
# a = None

# print(type(name))
# print(type(age))
# print(type(price))
# print(type(old))
# print(type(a))

# a = 500
# b = 1000
# sum = (a+b)
# print(sum)

# a = 1000
# b = 200
# diff = (a-b)
# print(diff)

# print("hello world")
# Hello everyone i am a comment how are you
"""
multiline 
comment
"""

#arithmetic operator

# a = 10
# b = 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a**b) #a^b
# print(a % b) #remainder

#relational operator
# a = 50
# b = 10

# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)
# print(a > b)
# print(a < b)

#assignment operator
# num = 20
# num = 5
# print("num :", num)

# num = 10
# num += 5
# print("num :" , num)

# num = 10
# num -= 5
# print("num :" , num)

# num = 10 
# num *= 5
# print("num: " , num)

# num = 10
# num **= 5
# print("num:" , num)

# num = 10
# num %= 5
# print("num :" , num)

#logical operator
# a = 50
# b = 60

# print(not(a>b))
# print(not(a<b))

# val1 = True
# val2 = True
# print("and operator:", val1 and val2)
# #true will come when both value are true/ if one of them is false
# # then it will give false

# val1 = False 
# val2 = True
# print("and operator:", val1 and val2)

# val1 = True
# val2 = False 
# print("OR operator:", val1 or val2)
# #if one of them is true it will give true
# #if both are false then it will give false

#type conversion
# a = 4.33
# b = 2
# print(a+b)

# a = "11"
# b = 2
# print(type(a))
# print(a + b )

# coversiona 
# a = int("13")
# b = 3
# print(a + b)
# print(type(a))

# name = input("enter your name: ")
# print("welcome" , name)

# val = input("enter your age: ")
# print(type(val), val)
#whatever value we put in input the type of value will always remain
#str

# mov1 = int(input("enter movie name:"))
# print(type(mov1), mov1)
#if we add int in front bracket of input then it will convert
#str into int or float in any data type we just need to write data type
#in front of input

# name = input("enter your name :")
# age = int(input("enter age :"))
# marks = float(input("enter marks :"))

# print("welcome", name)
# print("age =", age)
# print("marks =", marks)

# num1 = int(input("enter 1st num :"))
# num2 = int(input("enter 2nd num :"))

# print("sum = " ,num1 + num2)

# side = int(input("enter the side of a square :"))
# print("area =", side*side)

# num1 = float(input("enter 1st no :"))
# num2 = float(input("enter 2nd no :"))

# print("average =" , (num1 + num2)/2)

# a = int(input("enter 1st no :"))
# b = int(input("enter 2nd no :"))
# print(a >= b)
                                                                   