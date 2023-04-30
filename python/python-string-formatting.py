# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:05:54 2023

@author: chenxy

ref: https://realpython.com/python-f-strings/
"""

# Option #1: %-formatting
'''
This is the OG of Python formatting and has been in the language since the very beginning. 
You can read more in the Python docs. 
Keep in mind that %-formatting is not recommended by the docs, which contain the following note:

“The formatting operations described here exhibit a variety of quirks that lead to a number of 
common errors (such as failing to display tuples and dictionaries correctly).

Using the newer formatted string literals or the str.format() interface helps avoid these errors. 
These alternatives also provide more powerful, flexible and extensible approaches to formatting text.”

How to Use %-formatting
String objects have a built-in operation using the % operator, 
which you can use to format strings. Here’s what that looks like in practice:
'''
myname = 'Chen Xiaoyuan'
print("Hello, I am %s." % myname)

'''
In order to insert more than one variable, you must use a tuple of those variables. 
Here’s how you would do that:
'''
myage = 50
print("Hello, I am %s, I am %s " % (myname, myage) )

myname = 'Chen Xiaoyuan'
profession = '​chip architect'
years  = 20
print("Hello, I am %s. I am a %s, with more than %s years experience" % (myname,profession,years))

'''
Why %-formatting Isn’t Great
The code examples that you just saw above are readable enough. 
However, once you start using several parameters and longer strings, 
your code will quickly become much less easily readable. 
Things are starting to look a little messy already:
'''
first_name = "Xiaoyuan"
last_name  = "Chen"
age        = 50
profession = "chip architect"
city   = "Shanghai"
print("Hello, I am %s %s. I am %s. I am a %s. I am living in %s." % (first_name, last_name, age, profession, city))

# Option #2: str.format()
"""
This newer way of getting the job done was introduced in Python 2.6. 
How To Use str.format()

str.format()  is an improvement on %-formatting. 
It uses normal function call syntax and is extensible through the __format__() method 
on the object being converted to a string.

With str.format(), the replacement fields are marked by curly braces:
"""
print("Hello, I am {}, I am {} " .format (myname, myage) )

myname = 'Chen Xiaoyuan'
profession = '​chip architect'
years  = 20
print("Hello, I am {}. I am a {}, with more than {} years experience".format(myname,profession,years))

# You can reference variables in any order by referencing their index:
print("Hello, I am {1}, I am {0} " .format (profession, myname) )    

# You can reference the same variable repeatedly
print("\
Hello, I am {1}, I am {0} \n\
       I am {0}, I am {1} \n\
       I am {1}, I am {0} \n\
       -- The important things should be said three times "\
       .format (profession, myname) )    

# If you insert the variable names, you get the added perk of being able to pass objects and then reference parameters and methods in between the braces:
person = {'name' : 'Chen Xiaoyuan', 'age' : 50}
print("Hello, I am {name}, I am {age} " .format (name=person['name'],age=person['age']) )    

print("Hello, I am {name}, I am {age} " .format (**person ) )

import math
print('pi = {0:6.5f}, {0:10.9f}'.format(math.pi))
      
'''
str.format() is definitely an upgrade when compared with %-formatting, but it’s not all roses and sunshine.

Why str.format() Isn’t Great
Code using str.format() is much more easily readable than code using %-formatting, 
but str.format() can still be quite verbose when you are dealing with multiple parameters and longer strings. 
Take a look at this:
'''
first_name = "Xiaoyuan"
last_name  = "Chen"
age        = 50
profession = "chip architect"
city       = "Shanghai"
print(("Hello, I am {last_name} {first_name}. I am {age}. " + 
      "I am a {profession}. I am living in {city}.") \
          .format(first_name=first_name, last_name=last_name, age=age, \
             profession=profession, city=city))
'''
If you had the variables you wanted to pass to .format() in a dictionary, 
then you could just unpack it with .format(**some_dict) and reference the values by key in the string, 
but there has got to be a better way to do this.
'''

# Option #3: f-Strings: A New and Improved Way to Format Strings in Python
'''
They joined the party in Python 3.6. 
You can read all about it in PEP 498, which was written by Eric V. Smith in August of 2015.

Also called “formatted string literals,” f-strings are string literals that have an f 
at the beginning and curly braces containing expressions that will be replaced with their values. 
The expressions are evaluated at runtime and then formatted using the __format__ protocol. 
As always, the Python docs are your friend when you want to learn more.

Here are some of the ways f-strings can make your life easier.
'''
'''
Simple Syntax
The syntax is similar to the one you used with str.format() but less verbose. Look at how easily readable this is:
'''
first_name = "Xiaoyuan"
last_name  = "Chen"
profession = "chip architect"
city       = "Shanghai"
print(f"Hello, I am {last_name} {first_name}. I am living in {city} ")
print(F"Hello, I am {last_name} {first_name}. I am living in {city} ")

'''
Arbitrary Expressions
Because f-strings are evaluated at runtime, you can put any and all valid Python expressions in them. 
This allows you to do some nifty things.
'''
# You could do something pretty straightforward, like this:
print(f'5! = {5*4*3*2*1}')
# You could do function call or method call inside f-string:
print(f'{myname.lower()} is a chip architect and algorithm engineer')    

def factorial(k):
    if k <= 1:
        return 1
    prod = 1
    for i in range(2,k+1):
        prod *= i
    return prod

print(f'20! = {factorial(20)}')    

'''
You could even use objects created from classes with f-strings. Imagine you had the following class:
'''
class Comedian:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f"{self.first_name} {self.last_name} is {self.age}."

    def __repr__(self):
        return f"{self.first_name} {self.last_name} is {self.age}. Surprise!"
new_comedian = Comedian("Eric", "Idle", "74")
print(f"{new_comedian}")

'''
The __str__() and __repr__() methods deal with how objects are presented as strings, 
so you’ll need to make sure you include at least one of those methods in your class definition. 
If you have to pick one, go with __repr__() because it can be used in place of __str__().

The string returned by __str__() is the informal string representation of an object and 
should be readable. The string returned by __repr__() is the official representation and 
should be unambiguous. Calling str() and repr() is preferable to using __str__() and __repr__() directly.

By default, f-strings will use __str__(), but you can make sure they use __repr__() 
if you include the conversion flag !r:
'''
print(f"{new_comedian}")
print(f"{new_comedian!r}")

# Multiline f-Strings

# Speed
'''
The f in f-strings may as well stand for “fast.”

f-strings are faster than both %-formatting and str.format(). As you already saw, f-strings are expressions evaluated at runtime rather than constant values. Here’s an excerpt from the docs:

“F-strings provide a way to embed expressions inside string literals, using a minimal syntax. It should be noted that an f-string is really an expression evaluated at run time, not a constant value. In Python source code, an f-string is a literal string, prefixed with f, which contains expressions inside braces. The expressions are replaced with their values.” (Source)

At runtime, the expression inside the curly braces is evaluated in its own scope and then put together with the string literal part of the f-string. The resulting string is then returned. That’s all it takes.
'''

# Python f-Strings: The Pesky Details
# Now that you’ve learned all about why f-strings are great, I’m sure you want to get out there and start using them. Here are a few details to keep in mind as you venture off into this brave new world.

'''
Quotation Marks
You can use various types of quotation marks inside the expressions. 
Just make sure you are not using the same type of quotation mark on the outside of the f-string 
as you are using in the expression.
'''
'''
Dictionaries
Speaking of quotation marks, watch out when you are working with dictionaries. If you are going to use single quotation marks for the keys of the dictionary, then remember to make sure you’re using double quotation marks for the f-strings containing the keys.
'''

'''
Braces
In order to make a brace appear in your string, you must use double braces:

>>> f"{{70 + 4}}"
'{70 + 4}'
Note that using triple braces will result in there being only single braces in your string:

>>> f"{{{70 + 4}}}"
'{74}'
However, you can get more braces to show if you use more than triple braces:

>>> f"{{{{70 + 4}}}}"
'{{70 + 4}}'
'''

'''
Backslashes
As you saw earlier, it is possible for you to use backslash escapes in the string portion of an f-string. However, you can’t use backslashes to escape in the expression part of an f-string:

>>> f"{\"Eric Idle\"}"
  File "<stdin>", line 1
    f"{\"Eric Idle\"}"
                      ^
SyntaxError: f-string expression part cannot include a backslash
You can work around this by evaluating the expression beforehand and using the result in the f-string:

>>> name = "Eric Idle"
>>> f"{name}"
'Eric Idle'
'''

'''
Inline Comments
Expressions should not include comments using the # symbol. You’ll get a syntax error:

>>> f"Eric is {2 * 37 #Oh my!}."
  File "<stdin>", line 1
    f"Eric is {2 * 37 #Oh my!}."
                                ^
SyntaxError: f-string expression part cannot include '#'
'''

'''
Go Forth and Format!
You can still use the older ways of formatting strings, but with f-strings, you now have a more concise, 
readable, and convenient way that is both faster and less prone to error. 
Simplifying your life by using f-strings is a great reason to start using Python 3.6 if you haven’t already 
made the switch. (If you are still using Python 2, don’t forget that 2020 will be here soon!)

According to the Zen of Python, when you need to decide how to do something, 
then “[t]here should be one– and preferably only one –obvious way to do it.” 
Although f-strings aren’t the only possible way for you to format strings, 
they are in a great position to become that one obvious way to get the job done.
'''