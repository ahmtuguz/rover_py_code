import os, re
 
with os.scandir('/home/uguz/Downloads/dosya/') as directory:
    for item in directory:
        if not item.name.startswith('.') and item.is_file():
            with open(item, mode="r+") as file:
                file_text = file.read()
                print(file_text)
                regex = re.compile('#15')
                file_text = regex.sub('0', file_text)
                print(file_text)
                file.seek(0)
                file.write(file_text)