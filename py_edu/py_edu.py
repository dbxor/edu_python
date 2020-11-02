"""
This is a comment
written in 
more than just one line
"""
from numpy import random
x=random.randint(100, size=(3, 5, 2))

print(x)
x = random.rand(5,5)

print(x)
x=random.randint(80)

print(x)
x = random.choice([1, 3, 5, 7, 9], size=(3, 5))

print(x)


"""
import numpy as np 


arr = np.array([41, 42, 43, 44])

filter_arr = arr > 42

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)
arr = np.array([1, 2, 3, 4, 5, 6, 7])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is completely divisble by 2, set the value to True, otherwise False
  if element % 2 == 0:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=1)

print(arr)
arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.hstack((arr1, arr2))

print(arr)
arr = np.vstack((arr1, arr2))

print(arr)

arr = np.dstack((arr1, arr2))

print(arr)

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)

newarr = np.array_split(arr, 4)

print(newarr[0])
print(newarr[1])
print(newarr[2])
print(newarr[3])

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3)

print(newarr)
x = np.where(arr == 9)

print(x)

arr = np.array([1, 3, 5, 7])

x = np.searchsorted(arr, [2, 4, 6])

print(x)

arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))

arr = np.array([41, 42, 43, 44])

x = [True, False, True, True]

newarr = arr[x]

print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr = arr[0:6]
narr = arr.reshape(2, 3)
print(narr)
print("narr.base", narr.base)
#print(arr.reshape(2, 4).base)
newarr = arr.reshape(2, 2, -1)

print(newarr)
 
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, 2, -1)

print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])

newarr = arr.reshape(-1)

print(newarr)


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
 
print(arr[1, 1:4])


print(arr[0:2, 2])

print(arr[0:2, 1:4])


a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) 
print(b.ndim) 
print(c.ndim) 
print(d.ndim)

arr = np.array([1, 2, 3, 4,6], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array( [
                [[1, 2, 3], [4, 5, 6], [14, 15, 16]], 
                [[7, 8, 9], [10, 11, 12], [41, 51, 61]], 
                [[17, 18, 19], [110, 111, 112], [141, 151, 161]]
                ])
print(arr[1, 1, 1])
print(arr[2, 1, 2])
print(arr[2, 2, 2]) #161

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])





quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
print("I want %s pieces of item %s for %s dollars." %(quantity, itemno, price))

txt = "We are the so-called \'Vikings\' from the north."

print(txt)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])
print(thislist)
thislist.insert(1, "orangeapple")
print(thislist)
thislist.pop()
print(thislist)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

thistuple = ("apple", "banana", "cherry")
del thistuple


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue#break
  print(x)



def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(10)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

class Person1:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person1("John", 36)
p1.myfunc()



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

x = Student("Mike", "Olsen")
x.printname()

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



import mymodule

a =  mymodule.person1["age"]
print(a)

import platform

x = platform.system()
print(x)


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


"""