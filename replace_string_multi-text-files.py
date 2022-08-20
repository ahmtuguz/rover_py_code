import os
import re
  
folder_path = "/home/uguz/Desktop/new_foto/" # your path
target = "15 "
match_object="0 "
def str_counter(match_object):
    str_counter.count += 1
    return str(str_counter.count)
str_counter.count = 0
 
def  do_it(file_name):
    with open(file_name, 'r') as file :
        filedata = file.read()
        print(filedata)
      
        filedata = re.sub(re.escape(target), str_counter, filedata)
     
        print(filedata)
      
        with open(file_name, 'w') as file:
            file.write(filedata)
            file.close()
         
for name in os.listdir(folder_path):
    if name.endswith(".txt"):
        file_name = os.path.join(folder_path, name)
        do_it(file_name)