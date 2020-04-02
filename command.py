import os
import getpass

os.system("tput setaf 3")
print("""Press 1: To see date
Press 2: To see calender
Press 3: To see the running process
Press 4: Add User
Press 5: Convert lowercase to uppercase
Press 6: SSH to a server
Press 7: Configure yum
Press 8: Download a software
Press 9: Configure httpd server
Pess 10: Deploy your website into httpd server""")

print("Enter Your Choice: ",end="")
ch = input()
c = int(ch)

os.system("tput setaf 4")

if c==1:
	os.system("date")

elif c==2:
	os.system("cal")
elif c==3:
	os.system("ps -aux")


#Create User
elif c==4:
        print("Enter User Name: ", end = '')
        user_name = input()
        print("Enter Password: ", end = '')
        password = getpass.getpass()
        os.system("useradd {}".format(user_name))
        os.system("id {}".format(user_name))

elif c==5:
	print("Enter the string: ", end = '')
	str = input()
	os.system("tr 'a-z' 'A-Z' < {}".format(str))

#ssh to a server
elif c==6:
	print("Enter the IP address of the system: ", end='')
	ip = input()


#Configure yum
elif c==7:
	print("Do you want to configure yum manually?[Y/N] ", end='')
	yum = input()
	if yum=="Y":
		print("Enter Base Url: ", end='')		
		
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
		

#Install package	
elif c==8:
	print("Make sure your yum is configured, if not press _ to configure your yum")
	print("Enter the package name: ", end='')
	package_name = input()
	os.system("yum install -y {}".format(package_name))


else :
	print("Option not supported")
os.system("tput setaf 7")

