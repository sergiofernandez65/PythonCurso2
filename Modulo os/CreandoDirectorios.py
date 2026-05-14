import os

os.mkdir("my_first_directory")
print(os.listdir())



import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())
