#!/usr/bin/python3
import os
userlist = ["alpha", "beta", "gamma"]

print("Adding users to system")
print("################################")

# loop to add user from userlist
for user in userlist:
 exitcode = os.system("id {}".format(user))
 if exitcode != 0:
   print ("user doesnt exist.. adding it".format(user))
   print ("###################################")
   print ()
   os.system("useradd {}".format(user))
 else:
   print("user already exist.")
   print("################################")
   print()
# for groups
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
  print("group science doesnt exist..adding it")
  print("##################################")
  print()
  os.system("groupadd science")
else:
  print("group already exist")
  print("####################################")
  print()

# adding users to group
for user in userlist:
  print("add user {} to science group".format(user))
  print("####################################")
  print()
  os.system("usermod -G science {}".format(user))

# adding directory
print("adding directory")
print("###################################")
print()
if os.path.isdir("/opt/science_dir"):
  print ("dir already exist")
else:
  os.mkdir("/opt/science_dir")

# permissions
print("assign permission and ownership")
print("##################################")
print()
os.system("chown :science /opt/science_dir")
os.system("chmod 770 /opt/science_dir")

