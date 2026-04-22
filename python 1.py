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

#4th lecture
#dictionary

#info = {
     

# null_dict = {}
# null_dict["name"] = "apnacollege"
# print(null_dict)

#print(info["key"])   
#print(info["subjects"]) 
#print(info["topics"])
#print(info["name"])
#print(info["learning"]) 

#info["name"] = "Ashmitajha"
# info["name"] = "Ashmita"
# info["surname"] = "jha"
# print(info)

#nested dictionary
# student = {
#         "name" : "ashmita jha",
#         "subjects" : {
#         "phy" : 97,
#         "chem" : 88,
#         "maths" : 99,

#         }


#     }

# #print(student["subjects"]["chem"])
# #print(student.keys())
# print(len(student))
# print(len(list(student.keys())))

# info = { 
#     "key" : "value",
#     "name" : "apnacollege",
#     "learning" : "coding",
#     "age" : "19",
#     "is_adult" : "True",
#     "marks" : "94.4",
#     "subjects" : ["python","c","c++"],
#     "topics" : ("dict","set")
# }

# print(info)
# print(info["name"])
# print(info["topics"])
# print(info["subjects"])
# print(info["age"])

# info["name"] = "Ashmita"
# info["surname"] = "jha"
# print(info)

# null_dict = {}
# null_dict["name"] = "apnacollege"
# print(null_dict)

#nested dictionary
# student = { 
#     "name" : "Ashmita jha",
#     "subjects" : {
#         "physics" : 88,
#         "chemistry" : 90,
#         "maths" : 89

#     }
# }
# print(student["subjects"]["maths"])
# print(student.keys())
# print(list(student.keys()))
# print(len(student.keys()))
# print(len(list(student.keys())))

# print(student.values())
# print(len(list(student.values())))

# print(student.items())
# print(student['name2']) #error
# print(student.get("name")) 
# print(student.get("name2")) #no error

# student.update({"city" : "Gujarat"})
## print(student)
# new_dict = {"name" : "rajashi ghevar" , "age" : "18"}
# student.update(new_dict)
# print(student)

# collection = {1,2,3,2,2,"hello","subjects","total",6}
# print(collection)
# print(len(collection)) #total no of item

# collection = set() #empty set; syntax
# print(type(collection))

# collection = set()
# collection.add(1)
# collection.add(2)
# collection.add(2)
# collection.add(3)
# collection.remove(2)
# collection.clear()
# print(len(collection))

# collection = {"hello","apnacollege","atal",18,"python"}
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())

# set1 = {1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}
# print(set1.union(set2)) 

# set1 = {1,2,3,4,5,6}
# set2 = {3,4,5,6,7}
# print(set1.intersection(set2))

# meanings = {
#     "table" : ["a piece of furniture","list of facts and figure"],
#     "cat" : "a small animal",
#     "notebook" : "a set of papers",
#     "book" : "a lot of knowledge"

# }

# print(meanings["table"])
# print(meanings["cat"])
# print(meanings["notebook"])
# print(meanings["book"])

# sub1 = {"python","java","c++","python","javascript"}
# sub2 = {"java","python","java","c++","c"}
# print(sub1.intersection(sub2))

# marks = {}


# x = int(input("enter phy : "))
# marks.update({"phy" : x})

# x = int(input("enter chem : "))
# marks.update({"chem" : x})

# x = int(input("enter maths : "))
# marks.update({"maths" : x})

# print(marks)

# values = {
#     ("float", 9.0),
#     ("int", 9)
# }

# print(values)

# info = { 
#     "name" : "apnacollege",
#     "subjects" : ["python","C","Java"],
#     "topics" : ("dict","set"),
#     "age" : 35,
#     "is_adult" : True,
#     "marks" : 94.4
# }

# print(info)
# print(type(info))
# print(info["name"])
# print(info["topics"])
# info["name"] = "ashmitajha"
# info["age"] = "55"
# info["surname"] = "jha"
# print(info)

# student = {
#     "name" : "rahul kumar",
#     "subjects" : {
#          "phy" : 97,
#          "chem" : 98,
#         "math" : 93
     
#      }
# }

# print(student)
# print(student["subjects"])
# print(student["subjects"]["chem"])

# loop in python
# count = 1
# while count <= 5 :
#     print("Hello")
#     count += 1

# print(count)    

# i=1
# while i <= 10:
#     print("Ashmita",i)
#     i+=1
      
# i=5
# while i >= 1:
#     print("dedication",i)
#     i -= 1      

#practice Question
#1
# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#2
# i = 100
# while i >= 1:
#     print(i)
#  i-=1

#3


#4
# num = [1,4,9,16,25,36,49,64,81,100]
# i = 1
# while i <= 10:
#     print(i*i)
#     i += 1

#other way
# num = [1,4,9,16,25,36,49,64,81,100]
# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

# heros = ["arnav","ates","rudra","aditya","dev","abir"]
# idx = 0
# while idx < len(heros):
#     print(heros[idx])
#     idx+=1

#5
# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 36
# i=0
# while i < len(nums):
#     print(nums[i])
#     i += 1


#BREAK AND CONTINUE

# i=1
# while i<=5:
#     print(i)
#     if(i==3):
#         break
#     i+=1
# print("end of loop")    

# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

#Q
#  nums = [1,2,2,4,5,6,7,8,9]

# for val in nums:
#   print(val)

#Q
# str = "paruluniversity"
# for char in str:
#     print(char)

#Q,
# tup = [1,2,3,4,5,6,7]

# for num in tup:
#     print(num)

# str = "paruluniversity"

# for char in str:
#     if(char == 's'):
#         print("found s")
#         break
#     print(char)
# else:
#     print("END")

#1. lst = [1,4,9,16,25,36,49,64,81,100]
# for val in lst:
#     print(val)

# 2. list = (1,4,9,16,25,36,49,64,81,100)

# for val in list:
#     if(val == 49):
#         print("found 49")
#         break
#     print(val)
# else:
#     print("End")

# num = (1,4,9,16,25,36,49,64,81,100,49)
# x=49
# idx=0
# for el in num:
#     if(el == x):
#         print("number found at idx",idx)
#         break
#     idx += 1

#RANGE
 
# seq = range(10)
# for i in seq:
#     print(i)

# for i in range(10):  #(range)
#     print(i)


# for i in range(2,10):       #range(start,stop)
#     print(i)

# for i in range(2,10,3):       #range(start,stop,step)
#     print(i)

#qustion 1
# for i in range(1,101):
#     print(i)

#question 2
# for i in range(100,0,-1):
#     print(i)

#question 3
# n =int(input("Enter number: "))
# for i in range(1,11):
#     print(n * i)

#question
# n = 10

# sum = 0
# for i in range(1,n+1):
#     sum += i
#     print("total sum: ",sum)

#question

# n=7
# sum=0
# i=1
# while i <= n:
#     sum += i
#     i += 1
#     print("total sum: ",sum)

# n=5
# mul = 1
# i=1
# while i <= n:
#     mul *= i
#     i += 1
#     print("total multiplication: ",mul)
   
#FUNCTION

# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum  

# calc_sum(5,10)

# #more lines of code

# calc_sum(2,10)

# #more lines of code

# calc_sum(12,17)

def calc_sum(a,b):
    return a+b
sum = calc_sum(178,2221)
print(sum)

