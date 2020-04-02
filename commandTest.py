import os;
import getpass;

def localRun():
    os.system("tput setaf 3")
    while(True):
        print("""
        Press 1: To see date
        Press 2: To see calender
        Press 3: To see the running process
        Press 4: Add User
        Press 5: SSH to a server
        Press 6: Configure yum
        Press 7: Download a software
        Press 8: Configure httpd server
        Press 9: Deploy your website into httpd server
        Press 10: To exit""")
        
    
        print("Enter your choice: ", end="")
        ch = input()
    
        if int(ch)==1:
            os.system("date")
        elif int(ch)==2:
            os.system("cal")
        elif int(ch)==3:
            os.system("ps -aux")
    
    
        #Create User
        elif int(ch)==4:
            print("Enter User Name: ", end = '')
            user_name = input()
            print("Enter Password: ", end = '')
            password = getpass.getpass()
            os.system("useradd {}".format(user_name))
            os.system("id {}".format(user_name))
        #ssh to a server
        elif int(ch)==5:
            print("Enter the string: ", end = '')
            str = input()
            os.system("tr 'a-z' 'A-Z' < {}".format(str))

        #Configure yum
        elif int(ch)==6:
            print("Do you want to configure yum manually?[Y/N] ", end='')
            yum = input()
            if yum=="Y":
                print("Enter Base Url: ", end='')
                base_url = input()


            else:
                f=open(os.path.join("/etc/yum.repos.d", 'dvd.repo'), 'w')
                f.write("""[dvd1]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0""")
                f.close()
                os.system("yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm")
        
        #install package
        elif int(ch)==7 :
            print("Is your yum is configured?(Y/N): ",end='')
            c = input()
            if c=="Y":
                print("Enter the package name you want to install: ",end='')
                package_name = input()
                os.system("yum install -y {0}".format(package_name))

        elif int(ch)==8:
            os.system("rpm -q httpd > ws.txt")
            global data
            with open('ws.txt', 'r') as file:
                data =  file.read().replace('\n', '')
            x=data.split("-")
            if x[0] != "httpd":
                os.system("yum install -y httpd")
            isPerm = input("Do you want to keep the service running permenantly?(Y/N)")
            if isPerm == "Y":
                os.system("systemctl enable httpd")
                os.system("systemctl stop firewalld")
            else :
                os.system("systemctl stop httpd")
            os.system("systemctl status httpd")

                
        elif int(ch)==10:
            exit()
        os.system("tput setaf 7")

        
        input("Press enter to continue...")
        os.system("clear")

def remoteRun():
    

ch = input("Where do you want to run the software(local/remote)?")
if ch=='local':
    localRun()
elif ch=='remote':
    remoteRun()
