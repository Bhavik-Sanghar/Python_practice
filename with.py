
# File Append
with open("test1.txt","a") as file:
    file.write("Hello world")
    print('Write Done')

    
with open("test1.txt","r") as file:
    print(file.read())
