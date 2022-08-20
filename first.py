from os import write
import time,datetime 
def write():
    tarih=datetime.datetime.today()
    zaman_damgası = datetime.datetime.timestamp(tarih)
    #print(zaman_damgası)
    zaman_damgası=round(zaman_damgası,2)
    #print(zaman_damgası)
    writer=open("time.txt","a")
    writer.write("Now: "+str(zaman_damgası)+"\n")
    writer.close()
def read():
    reader = open("time.txt", "r")
    print(reader.readlines())
    reader.close()

write()
read()