def register():
    print("REGISETRATION")
    regexem = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    regexpass ="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,10}$"
    fptr=open("register.txt","a")
    st=input("enter email address:")
    pas=input("enter password:")
    e=0
    p=0
    if(re.search(regexem,st)):
        e=1
        if(re.search(regexpass,pas)):
            fptr.write(st)
            fptr.write("\n")
            fptr.write(pas)
            fptr.write("\n")
            print("user registered successfully")
    else:
        print("wrong credentials")
    fptr.close()
def login():
    st=input("enter username:")
    pas=input("enter password:")
    lines=[]
    with open("register.txt") as fptr:
        lines=[line.rstrip() for line in fptr]
    ind=-1
    if(st in lines):
        ind=lines.index(st)
    if(ind>=0):
        if(lines[ind+1] == pas):
            print("WELCOME ",st)
        else:
            print("please enter correct password")  
            f=input("forgot password:")
            if(f=="y"):
                print("your password is : ",lines[ind+1])
                login()
            else:
                print("user doesn't exist please register")
                register()
    else:
        print("user doesn't exist please register")
        register()
    
    
import re
options=input("enter register/login:")
if(options=="register"):
    register()
elif options == "login":
    login()