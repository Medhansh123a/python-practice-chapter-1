import os
#can enter directory you want to see contents of
path = input("Enter directory path: ")
#lists all files and directories in the specified paths
contents = os.listdir(path)
#print each file and directory name
print("Contents of directory:")
for item in contents:
    print(item)