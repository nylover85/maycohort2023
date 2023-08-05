import os

directory = os.getcwd()

file_python = []

for filename in os.listdir(directory):
    
    file_size = os.path.getsize(filename)
    modified_time = os.path.getmtime(filename)
    creation_time = os.path.getctime(filename)
    file_path = os.path.realpath(filename)
   
    file_python.append({'name': filename, 'size': file_size, 'time': modified_time, 'path': file_path})

print (*file_python,sep="\n")

