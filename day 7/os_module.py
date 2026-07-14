import os
print(f"current working Directory: {os.getcwd()}")
os.chdir("day 7")
print(f"now your dir is {os.getcwd()}")
#os.rmdir("songs")
#os.mkdir("songs")


os.chdir("..")
print(f"now current working Directory: {os.getcwd()}")

print(os.listdir())