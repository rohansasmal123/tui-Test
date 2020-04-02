import os

f=open(os.path.join("/etc/yum.repos.d", 'hi.repo'), 'w')
f.write('This is hi file')
f.close()
