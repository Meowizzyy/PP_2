import re

#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# findall - Returns a list containing all matches
# sub - Replaces one or many matches with a string

test1 ="aqua abobus"
x=re.findall(r"\S*ab*\S*", test1)
print(x)
print("-----------------------------")

#Напишите программу на Python, которая соответствует строке, содержащей "a", за которой следуют два-три "b".

test1 ="apple aabbus abbberation"
x=re.findall(r"\S*a{2,3}b\S*", test1)
print(x)
print("-----------------------------")

#Write a Python program to find sequences of lowercase letters joined with a underscore.

test1 ="Under_Score notunderscore"
x=re.findall(r"\S*_\S*", test1)
print(x)
print("-----------------------------")

#Write a Python program to find the sequences of one upper case letter followed by lower case letters.

test1 ="Hello world"
x=re.findall(r"\S*[A-Z][a-z]\S*", test1)
print(x)
print("-----------------------------")


#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
test1 ="apasdb asdvsd"
x=re.findall(r"a\w*b", test1)
print(x)
print("-----------------------------")

#Write a Python program to replace all occurrences of space, comma, or dot with a colon.

test1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam lectus risus."
x = re.sub(r"[.',\s]", ":", test1)
print(x)
print("-----------------------------")


#Write a python program to convert snake case string to camel case string.

test1 = "Pine_apple"
x = re.sub(r'_([\w])', lambda x: x.group(1).upper(), test1)
print(x)
print("-----------------------------")

#Write a Python program to split a string at uppercase letters.
test1 = "Hello World."
x = re.findall(r'[A-Z][^A-Z]*', test1)
print(x)
print("-----------------------------")

#Write a Python program to insert spaces between words starting with capital letters.

test1 = "RickAndMorty"
x = re.sub(r'(\w)([A-Z])', lambda x: x.group(1) + " " + x.group(2), test1)
print(x)
print("-----------------------------")

#Write a Python program to convert a given camel case string to snake case.

test1 = "NeverGonnaGiveYouUp"
x = re.sub(r'(\w)([A-Z])', lambda x: x.group(1) + "_" + x.group(2), test1)
print(x)
print("-----------------------------")
