#!/usr/bin/python2.7
-------------------------------------------------------------------
-------------------------------------------------------------------

#reading a file

file1 = open("test.txt","r")
file1.read()
#output
'This is a Python File\n\n\nPython is fantastic language.\n\n\nMac OS ia a fantastic OS\n'
#run again
file1.read()
#output
''
#after read the cursor stays at the end of the file so we cant see nothing new on second read
-------------------------------------------------------------------
-------------------------------------------------------------------

file1.lell() #command telling us the lenth of the file in characters
#output
84
#that means file got 84 characters
-------------------------------------------------------------------
-------------------------------------------------------------------

#in that case positioning command will help us
file1.seek(0,0) #puts cursor on 0 position in the file
file1.read()
#output
'This is a Python File\n\n\nPython is fantastic language.\n\n\nMac OS ia a fantastic OS\n'
file1.seek(0,0) #puts cursor on 0 position in the file
file1.read()
#output
'This is a Python File\n\n\nPython is fantastic language.\n\n\nMac OS ia a fantastic OS\n'

file1.read(21) #that mens read only 21 charactes from file
#output
'This is a Python File'
#in that case the cursor stay on position of character 21 and on next read..
file1.read(21) #that mens read only 21 charactes from file
#output
'\n\n\nPython is fantastic '

-------------------------------------------------------------------
-------------------------------------------------------------------

#
#
#write to file methods
#
#overwrite

f=open("test.txt","w") #allows only write no reading from file
f.write("i have entered some text into this file \n let's see if this works")
f.close()
#now the intire file was overwriten with new text
-------------------------------------------------------------------
-------------------------------------------------------------------

## 
#there is lots of different methods how to open file check in internet
##
-------------------------------------------------------------------
-------------------------------------------------------------------

#append
f=open("test.txt","a") #allows only append no reading from file
f.write("i have entered some text into this file \n let's see if this works")
f.close()
#this command appends text to the file without any spaces or different marks between previous text and new text
-------------------------------------------------------------------
-------------------------------------------------------------------

#example for complex access method a+ allows append and read in the same time
f=open("test.txt","a+") #allows only append and read no reading from file
f.write("i have entered some text into this file \n let's see if this works")
f.seek(0,0)
f.read()
f.close()
-------------------------------------------------------------------
-------------------------------------------------------------------

#
#copy file option
#

ufn=input("Enter your filename: ")
file1=open(ufn,"r")
file2=open("copied.txt","w")
file2.write(file1.read())
file1.close()
file2.close()

-------------------------------------------------------------------
-------------------------------------------------------------------
