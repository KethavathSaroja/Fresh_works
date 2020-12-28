import threading 
from threading import*
import time

d={} 

def create(key,value,timeout=0):
    if key in d:
        print("error: this key already")
    else:
        if key.isalpha():
            t=len(d)
            #print(t,value)
            #print(type(value))
            v=int(value)
            if t<(1024*1020*1024) and value<=(16*1024*1024): 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
        flag()
def flag():
    return 1

#for read operation
#use syntax "read(key_name)"
            
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key_name:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:

             # def r():
                  stri=str(key)+":"+str(b[0])
                  return stri
              #r()
            

#for delete operation
#use syntax "delete(key_name)"

def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del d[key]
            print("key is successfully deleted")


def modify(key,value):
    b=d[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in d:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                d[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #
    else:
        if key not in d:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            d[key]=l
create("saroja",21)
create("saroja",20,100) 

def r():
    r=read("saroja")
    if(r=='saroja:20'):
        pass
    return 1
#print(r)
#print(type(r))
read("saroja")
def m():
    modify("saroja",45)
    
    return 1
def dele():
     
  delete(45)
  return 1
create("preeti",34)
t1=Thread(target=(create or read or delete),args=("avb",50000000,1)) 
t1.start()
#t1.sleep()
t2=Thread(target=(create or read or delete),args=("adc",56787600000,1)) 
t2.start()
#t2.sleep()
t3=Thread(target=(create or  read or delete),args=("sfg",56687600000,1))
t3.start()
#t3.sleep()
