string = input("Enter comma seperated integers")
print(string)
list = string.split(",")
print(list)
def convert(list):
    return(*list, )
print(convert(list))

