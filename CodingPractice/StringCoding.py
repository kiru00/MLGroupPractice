# Python program to reverse a string using slice method

def reverse(string):
    string = string[::-1]
    return string


inString = input("Please enter the string    ")
rev_str = reverse(inString)
print("Reverse String is : ", rev_str)