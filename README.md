# pythonScript
In this project we are going to automate some linux tasks using python

# Tasks to do .
- add users
- add groups
- add users to group
- create directory
- assign user and group ownership
- test if user or directory exists, if not create it 

# flow of execution of running some commands locally using python
- first we are going to ssh to scriptbox
- after this create directory
   root@scriptbox:~# mkdir /opt/pyscripts
   root@scriptbox:~# cd /opt/pyscripts
- now time to add users, groups, permissions using python scripts.
   root@scriptbox:/opt/pyscripts# vim ostasks.py
- To make our script excutable   
   root@scriptbox:/opt/pyscripts# chmod +x ostasks.py
  ...................................................
