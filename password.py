import string
import random

if __name__ =="__main__":
    s1 = string.ascii_lowercase
    s2= string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    plen = int(input("\n enter password lenght: \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("enter user name:")
    print("enter your password:" )
    print("".join( random.sample(s,plen)))
    
  