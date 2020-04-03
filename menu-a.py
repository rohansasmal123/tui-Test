import os
import getpass

os.system("clear")
os.system("tput setaf 2");
print("")
print("\t\t\tWelcome to TUI that makes life simple");
os.system("tput setaf 7");
print("\t\t\t~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");

passc="root"
passu=getpass.getpass("\nUSER AUUTHENTICATION -\nenter the password :")
i=3
while i>0:
    if passc==passu:
        break
    else :
        passu=getpass.getpass("incorrect password...{} tries left :".format(i))
        i-=1
else :
    input("authentication failed \npress ENTER to continue....")
    exit()



mode=input("\nenter the MODE OF EXECUTION(remotely / locally) :")

if mode=="remotely":
    ip=input("please enter the ip :")
    x=os.system("arp -a | grep {}".format(ip))
    if x!=0:
        print("invalid ip or ip not present in the network")


while 1:

    if mode=="remotely":

        print("""\nTASKS PRESENT :
    1-> see date
    2->
    3-> configure web server
    4-> configure docker ce
    5-> change the MODE OF EXECUTION
    6-> change the ip
    0-> exit

PLEASE ENTER THE TASK :""",end="")
        c=int(input())
        if c==1:
            os.system("ssh {} date".format(ip))
        elif c==6:
            ip=input("please enter the ip :")
            x=os.system("arp -a | grep {}".format(ip))
            if x!=0:
                print("invalid ip or ip not present in the network")
                exit()

        elif c==3:
            os.system("ssh {} yum install httpd -y".format(ip))
            loc=input("enter the location of website files :")
            os.system("ssh {} cp -r {}/* /var/www/html/".format(ip,loc))
            os.system("ssh {} systemctl stop firewalld".format(ip))
            os.system("ssh {} systemctl start httpd".format(ip))

        elif c==5:
            mode=input("enter the MODE OF EXECUTION(remotely /locally) :")


        else:
            print("wrong input")
            input("\n press ENTER to continue.....")

    elif mode=="locally":

        print("""\nTASKS PRESENT
    1 -> see date
    2 -> configure yum
    3 -> configure web server
    4 -> configure docker ce
    5 -> change the MODE OF EXECUTION
    0 -> exit

PLEASE ENTER THE TASK""",end=" :")
        c=int(input())

        if c==1:
            os.system("date")

        elif c==3:
            x=os.system("yum install httpd -y")
            if x==0:
                print("SUCCESSFULLY COMPLETED INSTALLING HTTPD!!")
            loc=input("please ENTER the location of website files :")
            os.system("cp -r {}/* /var/www/html".format(loc))
            os.system("systemctl stop firewalld")
            os.system("systemctl start httpd")


        elif c==2:
            s="""[doc]
            baseurl=
            gpgcheck="""
            x=os.system("{} | cat > 1".format(s))
            print(x)


        elif c==5:
            mode=input("\n enter the MODE OF EXECUTION (remotely/locally) :")


        elif c==0:
            input("press enter to continue")
            os.system("clear")



        else :
            print("Invalid input")
        input("\n press ENTER to continue.....")

    else :
        print("INVALID INPUT")
