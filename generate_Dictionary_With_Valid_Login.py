#!/usr/bin/python

# This program will generate a list of username and password by inserting 
# valid USERNAME and PASSWORD after every input dictionary username/password 
# and saves as new_Dictionary_Username and new_Dictionary_Password

# AUTHOR: CHANDRA SRIKANTH PRATHI

#Input
valid_Username = raw_input("Enter the valid Username: ")
valid_Password = raw_input("Enter the valid Password: ")
username_Dictionary = raw_input("Enter the path of Username Dictionary: ")
password_Dictionary = raw_input("Enter the path of the Password Dictionary: ")

#Printing User Inupt
print("Valid Username: " + valid_Username)
print("Valid Password: " + valid_Password)
print("Path of Username Dictionary: " + username_Dictionary)
print("Path of Password Dictionary: " + password_Dictionary)

#Open the username and password Dictionary Files
username_File = open(username_Dictionary, "r")
password_File = open(password_Dictionary, "r")

#Read the username and password dictionaries line by line
username_Line = username_File.readlines()
password_Line = password_File.readlines()

#Writing the Files
new_Username_File = open("new_Username_Dictionary.txt", "w+")
new_Password_File = open("new_Password_Dictionary.txt", "w+")

#Generating the new dictionary with a dictionary username and appending the legitimate username
for line in username_Line:
        new_Username_File.write(valid_Username)
        new_Username_File.write(line)
new_Username_File.close()

for line in password_Line:
        new_Password_File.write(valid_Password + "\n")
        new_Password_File.write(line)
new_Password_File.close()

print("new_Dictionary_Username.txt and new_Dictionary_Password.txt got created in the current directory")
