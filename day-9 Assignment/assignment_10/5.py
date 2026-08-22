# Write a python script which takes a three digit number from the user and displays only its middle digit.

user = int(input("Enter a three digit number: "))

result = user // 10 % 10
print(result)

