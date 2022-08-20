import os
 
with os.scandir('/home/uguz/Downloads/dosya/') as directory:
    for item in directory:
        if not item.name.startswith('.') and item.is_file():
            with open(item, mode="r+") as file:
                file_text = file.read()
                print(file_text)
                lines = file.readlines()
                file.seek(0)
                file.truncate()
                file.writelines(lines[:-1])
                file.close()


# f = open("/home/uguz/Downloads/dosya/", "r+")
