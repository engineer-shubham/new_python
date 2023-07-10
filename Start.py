x=5
y=10
summation = x+y
z = [5,10,15]
a = sum(z)
print(summation)
print(a)

print(type(sum))

tuple = ("apple", "banana", "cherry")
print(type(tuple))

dictionary = {"shubham" : 8, "shivani" : 9}
print(type(dictionary))

print(dictionary["shubham"])

boolean = True
print(type(boolean))

d=5
d=float(d)
print(d)

e=5.7
e=int(e)
print(e)

f=5
f=complex(f)
print(f)

length="hello world"
print(len(length))

first_value = length[0]
any_value = length[4]
middle_string_1 = length[0:5]
middle_string_2 = length[0:7]
truncate = length.strip()
uppercase = length.upper()
lowecare = length.lower()
replacement = length.replace("h","bh")
print(first_value)
print(any_value)
print(middle_string_1)
print(middle_string_2)
print(truncate)
print(uppercase)
print(lowecare)
print(replacement)

main_line = "Shubham is learning Python"
text1 = "{} and he is doing great in it."
text2 = "Shradha don't want to know about this but {}"
print(text1.format(main_line))
print(text2.format(main_line))

print(text1.format(text2))

print(10 > 9)
print(10 < 9)
print(bool("ab"))

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is fruit")
    
    
if "cola" in fruits:
    print("nothing should be printed")
    print("hello")