import os
 
with os.scandir('/home/uguz/Downloads/dosya/') as directory:
    for item in directory:
        if not item.name.startswith('.') and item.is_file():
            with open(item, mode="r+") as file:
                file_text = file.read()
                print(file_text)
                file.seek(1)
                file.truncate()

