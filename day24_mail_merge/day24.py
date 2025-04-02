# Open, reading and writing files

# in built method open
file = open('day24/my_file.txt')
print(file)

content = file.read()
print(content)

#we need to add the close method, because it will still use pc resources
file.close()



# with() method we don't need the close() method

with open('day24/my_file.txt') as file:
    content = file.read()
    print(content)


# for writing, we add mode= w
#It also creates a new file if it doesn't exist
with open('day24/my_file.txt',mode = "w") as file:
    #it deletes the content that we previously had in our text file
    file.write("new text")


# for appending content, we add mode= a
with open('day24/my_file.txt',mode = "a") as file:
    #it deletes the content that we previously had in our text file
    file.write("\nhola")


# Absolute path
with open('C:/Users/Cogito ergo sum/Documents/100DaysOfPython/day24/day24.txt',mode = "a") as file:
    #it deletes the content that we previously had in our text file
    file.write("\nhola Mundo")

