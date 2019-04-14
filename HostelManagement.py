"""
This is a program to standardise the Hostel Management System.
"""
import getpass
import smtplib
import sys
import io
import os
import re
from os import path
from email.mime.text import MIMEText

#Class Student to define Functionality like Adding and Removing Students from the File System
class Student(object):
    Name=None
    Permanent_Address=None
    Student_Mobile_Number=0
    Parent_Mobile_Number=0
    Date_of_Birth=0
    Class=None
    Department=None

    #Student Class Constructor
    def __init__(self,Name,Permanent_Address,Student_Mobile_Number,Parent_Mobile_Number,Mail,Date_of_Birth,Class,Department):
        self.Name=Name
        self.Permanent_Address=Permanent_Address
        self.Student_Mobile_Number=Student_Mobile_Number
        self.Parent_Mobile_Number=Parent_Mobile_Number
        self.Date_of_Birth=Date_of_Birth
        self.Class=Class
        self.Department=Department
        self.Mail=Mail

    #Function to Add Student to the File System
    def addStudent(self):
        try:

            #Generation of Hostel IDs
            hid=open("Hostel_IDs.txt","r")
            Hostel_Id=0
            for i in hid:
                Hostel_Id=i
            Hostel_Id=int(Hostel_Id)
            Hostel_Id+=1
            f=open("Student"+str(Hostel_Id)+".txt","a")
            f.write("ID: "+str(Hostel_Id)+\
                    "\nName: "+self.Name+\
                    "\nAddress: "+self.Permanent_Address+\
                    "\nS_phNumber: "+str(self.Student_Mobile_Number)+\
                    "\nP_phNumber: "+str(self.Parent_Mobile_Number)+\
                    "\nEmail Address: "+str(self.Mail)+\
                    "\nBirth Date: "+str(self.Date_of_Birth)+\
                    "\nClass: "+self.Class+\
                    "\nDepartment: "+self.Department+"\n"

            )
            Hostel_Id=str(Hostel_Id)
            hid=open("Hostel_IDs.txt","a")
            hid.write("\n"+Hostel_Id)
            print self.Name+" Added Successfully with Hostel ID :"+Hostel_Id

        except:
            print "File Not Found"


    #Method to Remove Student from File System
    def removeStudent(self,hostel_id):

        try:
            if (path.exists("Student"+str(hostel_id)+".txt")):
                file1=open("Student"+str(hostel_id)+".txt","r")
                for i in file1:
                        print i
                file1.close()
                ch=raw_input("Are sure you want to Delete this student?\t Y/N\t")
                if ch=='y' or ch=='Y':
                    os.system('cls')
                    os.remove("Student"+str(hostel_id)+".txt")
                    print "Student with Hostel ID: "+str(hostel_id)+" is Deleted Successfully"
                else:
                    os.system('cls')
                    print "Not Deleted"
            else:
                print "Not Found"

        except:
            print "No Student Found"

#Class Room which inherits Student
class Room(Student):

    #Room Class Constructor
    def __init__(self,Room_Id,Room_Capacity,Price):
        self.Room_Capacity=Room_Capacity
        self.Room_Id=Room_Id
        self.Price=Price

    #Method to Add New Room to the File Database
    def addRoom(self,roomcapacity,price):
        try:
            rid=open("Room_Id.txt","r")
            Room_Id=0
            for i in rid:
                Room_Id=i
            Room_Id=int(Room_Id)

            Room_Id+=1
            f=open("Room"+str(Room_Id)+".txt","a")
            f.write("ID: "+str(Room_Id)+\
                    "\nCapacity: "+str(roomcapacity)+\
		    		"\nPrice: "+str(price)+"\n"
            )
            Room_Id=str(Room_Id)
            rid=open("Room_Id.txt","a")
            rid.write("\n"+Room_Id)
            print "New Room with Room Number : "+str(Room_Id)+" Added Successfully"
        except:
            print "File Not Found"

    #Method to Remove Student
    def removeRoom(self,Room_id):

        try:
            if (path.exists("Room"+str(Room_id)+".txt")):
                file1=open("Room"+str(Room_id)+".txt","r")
                for i in file1:
                        print i
                file1.close()
                ch=raw_input("Are sure you want to Delete this room?\t Y/N\t")
                if ch=='y' or ch=='Y':
                    os.system('cls')
                    os.remove("Room"+str(Room_id)+".txt")
                    print "Room Number : "+str(Room_id)+" Deleted Successfully"
                else:
                    os.system('cls')
                    print "Room Not Deleted"
            else:
                os.system('cls')
                print "Not Found"

        except:
            os.system('cls')
            print "No room Found"


    #Change Existing Room's Capacity
    def updateCapacity(self):
                try:
                    rn=input("Enter Room Number to be Updated:\t")
                    if (path.exists("Room"+str(rn)+".txt")):
                        rid=open("Room"+str(rn)+".txt", 'r')
                        print "\n"
                        for i in rid:
                            print i
                        rid.close()
                        print "\n"
                        cap=input("Enter New Capacity for this Room:\t")
                        with open("Room"+str(rn)+".txt", 'r') as file:
                            data = file.readlines()
                            file.seek(1)
                        data[1] = "Capacity: "+str(cap)+"\n"
                        with open("Room"+str(rn)+".txt", 'w') as file:
                            file.writelines( data )
                        os.system('cls')
                        print "\nRoom Id: "+str(rn)+" Updated with its Cpacity: "+str(cap)
                        rid=open("Room"+str(rn)+".txt", 'r')
                        print "\n"
                        for i in rid:
                            print i
                        print "\n"
                        rid.close()
                    else:
                        print "Room Not Found"
                except:
                    print "File Not Found"

    def assignRoom(self):
            try:
                    print "\nAvailable Rooms"
                    print "-"*10
                    with open("Room_Id.txt","r") as rooms:
                        data=rooms.readlines()
                    for i in range(1,(len(data))):
                        if (path.exists("Room"+str(i)+".txt")):
                            print "Room"+str(i)
                    print "-"*10
                    
                    rn=input("Enter Room Number to be Assigned:\t")
		    os.system('cls')		
		
					
                    if (path.exists("Room"+str(rn)+".txt")):
                        rid=open("Room"+str(rn)+".txt", 'r')
                        print "\n"
                        for i in rid:
                            print i
                        rid.close()
			with open("Room"+str(rn)+".txt", 'r') as file:
                            data = file.readlines()
                            file.seek(1)
                        capacity = data[1].split(':')[1]
                        capacity=int(capacity)
                        if len(data)<capacity+3:
                            print "\n"
                            print "\nAvailable Students"
                            print "-"*10
                            with open("Hostel_Ids.txt","r") as studs:
                                data=studs.readlines()
                            for i in range(1,(len(data))):
                                if (path.exists("Student"+str(i)+".txt")):
                                    print "Student"+str(i)
                            print "-"*10
                            
                            stud=input("Enter Student ID to be Assigned :\t")
                            os.system('cls')
                            if (path.exists("Student"+str(stud)+".txt")):
                               
                                with open("Student"+str(stud)+".txt", 'r') as sid:
                                    data = sid.readlines()
                                    
                                if len(data)>10:
                                    print "Student Already Assigned."
                                else:
                                    sid=open("Student"+str(stud)+".txt", 'r')
                                    print "\n"
                                    for i in sid:
                                        print i
                                    sid.close()
                                    print "\n"
                                    ch=raw_input("Are you sure want to assign this student to Room"+str(rn)+" ?\tY/N :\t")
                                    if ch=='Y' or ch=='y':
                                        rid=open("Room"+str(rn)+".txt", "a")
                                        rid.write("Student Assigned :Student"+str(stud))
                                        sid=open("Student"+str(stud)+".txt","a")
                                        sid.write("\nRoom Assigned: Room"+str(rn))
                                        print "\n"
                                        os.system('cls')

                                        print "Assignment Done Successfully"
                                        sid.close()
                                        rid.close()
                                                                
                                
                            else:
                                print "Student Not Found"
                        else:
                            print "\nThis Room is Full\n\nPlease Check for Another Room"
                    else:
                        print "Room Not Found"
            except:
                print "File Not Found"

    def unassignRoom(self):
        try:
                    print "\nAvailable Rooms"
                    print "-"*10
                    with open("Room_Id.txt","r") as rooms:
                        data=rooms.readlines()
                    for i in range(1,(len(data))):
                        if (path.exists("Room"+str(i)+".txt")):
                            print "Room"+str(i)
                    print "-"*10
                    
                    rn=input("Enter Room Number to be Viewed:\t")
		    os.system('cls')					
                    if (path.exists("Room"+str(rn)+".txt")):
                        rid=open("Room"+str(rn)+".txt", 'r')
                        for i in rid:
                            print i

                        with open("Room_Id.txt","r") as rooms:
                            data=rooms.readlines()
                        if len(data)>=2:
                            sid=input("Enter Student ID to be Removed:\t")

                            with open("Room"+str(rn)+".txt", 'r') as file:
                                data = file.readlines()
                                file.seek(3)
                            data[3]=""
                            with open("Room"+str(rn)+".txt", 'w') as file:
                                file.writelines(data)

                            with open("Student"+str(sid)+".txt", 'r') as file:
                                data = file.readlines()
                                file.seek(10)
                            data[10]=""
                            with open("Student"+str(sid)+".txt", 'w') as file:
                                file.writelines(data)

                            print "Student"+str(sid)+" Removed From the Room"+str(rn)

                            
                            
                        else:
                            print "No Students Assigned"
                    else:
                        print "File Does Not Exist"
        except:
            print "File Not Found"
                    

class Admin(Room):

    def __init__(self,Username,Password):
        self.Username=Username
        self.Password=Password
	
    def Login(self):
        print "*"*10,
        print "Login Page",
        print "*"*10,
        print "\n"
        self.Username=raw_input("Enter Username: \t")
        self.Password=getpass.getpass("Enter Password: \t")
        r=Room(0,0,0)
        if (self.Username=="admin" and self.Password=="admin"):
            os.system('cls')
            while True:
             
               print "-"*50
               print "Welcome to the ADMIN Page"
               print "-"*50
               print "1.Add Room\n2.Remove Room\n3.Change Room Capacity\n4.Logout"
               choice=input("Enter your choice:\t") #Choice provided for user to perform various operations using menu
               if choice==1:
                   self.cap=input("Enter Capacity of the Room:\t")
                   self.price=input("Enter Price of the Room:\t")
                   os.system('cls')
                   r.addRoom(self.cap,self.price)
                try:

                    elif choice==2:
                             print "\nAvailable Rooms"
                             print "-"*10
                             with open("Room_Id.txt","r") as rooms:
                                 data=rooms.readlines()
                             for i in range(1,(len(data))):
                                 if (path.exists("Room"+str(i)+".txt")):
                                     print "Room"+str(i)
                             print "-"*10
                             id=input("Enter Room Number to be Removed:\t")
                             r.removeRoom(id)

                    elif choice==3:
                         print "\nAvailable Rooms"
                         print "-"*10
                         with open("Room_Id.txt","r") as rooms:
                             data=rooms.readlines()
                         for i in range(1,(len(data))):
                             if (path.exists("Room"+str(i)+".txt")):
                                 print "Room"+str(i)
                         print "-"*10
                         r.updateCapacity()

                    elif choice==4:
                        os.system('cls')
                        print "Admin Logged out Successfully"
                        a=Admin(self.Username,self.Password)
                        a.Login()

                    else:
                   os.system('cls')
                   print "Enter Correct Choice"

        elif (self.Username=="rector" and self.Password=="rector"):


                os.system('cls')
                while True:

                   print "-"*50
                   print "Welcome to the RECTOR Page"
                   print "-"*50
                   print "1.Add Student\n2.Remove Student\n3.Assign Student to a Room\n4.Remove Student from a Room\n5.Logout"


                   choice=input("Enter your choice:\t") #Choice provided for user to perform various operations using menu
                   if choice==1:
                       flag=1
                       while flag==1:
                           name=raw_input('Enter Your Name:\t')
                           if re.match(r'[a-zA-Z\s]',name) and len(name)!=1:
                               flag=0
                           else:
                               print("Invalid Name")
                               flag=1
                               
                       fla=1
                       while fla==1:
                           addr=raw_input('Enter your Permanent Address:\t')
                           if len(addr)!=None:
                               fla=0
                           else:
                               print("Invalid Address")
                               fla=1
                                   
                           
                       flag=1
                       while flag==1:
                           contact_S=raw_input('Enter Your Mobile Number:\t')
                           if re.match(r'[7-9]{1}[0-9]{9}',contact_S) and len(contact_S) == 10:
                               flag=0
                           else:
                               print("Invalid Mobile number")
                               flag=1
                           
                           
                       flag=1
                       while flag==1:
                           contact_P=raw_input("Enter Your parent's Mobile Number:\t")
                           if re.match(r'[7-9]{1}[0-9]{9}',contact_P) and len(contact_P) == 10:
                               flag=0
                           else:
                               print("Invalid Mobile number")
                               flag=1
                          
                           
                           
                       flag=1
                       while flag==1:
                           mail=raw_input('Enter Email Address:\t')
                           if re.match(r'\S+@\S+.[a-z]',mail):
                               flag=0
                           else:
                               print("Invalid Email Address")
                               flag=1
                       flag=1
                       while flag==1:
                           dob=raw_input('Enter Date of Birth:\t')
                           if re.match(r'[0-3]{1}[0-9]{1}-[0-1]{1}[0-9]{1}-[1-2]{1}[0-9]{3}',dob):
            
                                  
                    
                               flag=0
                           else:
                               print("Invalid Date of Birth")
                               flag=1
                           
                           
                       flag=1
                       while flag==1:
                           clss=raw_input('Enter your Class:\t')
                           if re.match(r'[a-zA-Z\s]',clss) and len(clss)!=1:
                               flag=0
                           else:
                               print("Invalid Class Name")
                               flag=1
                           
                           
                       flag=1 
                       while flag==1:
                           dept=raw_input('Enter your Department:\t')
                           if re.match(r'[a-zA-Z\s]',dept) and len(dept)!=1:
                               flag=0
                           else:
                               print("Invalid Department Name")
                               flag=1
                               
                        
                       os.system('cls')
                       s=Student(name,addr,contact_S,contact_P,mail,dob,clss,dept)
                       s.addStudent()
                       msg = MIMEText("Welcome to Hostel Databse")
                       msg['Subject'] = 'Admission'
                       msg['From'] = 'kedar@mitaoe.ac.in'
                       msg['To'] = mail
                       s = smtplib.SMTP('smtp.gmail.com', 587)
                       s.ehlo()
                       s.starttls()
                       s.login(msg['From'], 'kedar1023') 
                       try:
                            
                           s.send_message(msg)
                       except AttributeError:
                            s.sendmail(msg['From'], [msg['To']], msg.as_string())
                            s.quit()

                   elif choice==2:
                            print "-"*10
                            print "Available Students :\n\n"
                            with open("Hostel_IDs.txt","r") as ids:
                                data = ids.readlines()
                                for i in range(1,(len(data))):
                                    if (path.exists("Student"+str(i)+".txt")):
                                        print "Student"+str(i)
                            print "-"*10
                            hostel_id=input('Enter Hostel ID of the Student to be Removed:\t')
                            s=Student("","",0000000000,0000000000,0000000000,"","","")
                            s.removeStudent(hostel_id)
                            

                   elif choice==3:
                       r.assignRoom()
                       
                   elif choice==4:
                       r.unassignRoom()
                            
                   elif choice==5:
                       os.system('cls')
                       print "Admin Logged out Successfully"
                       a=Admin(self.Username,self.Password)
                       a.Login()

        else:
            os.system('cls')
            print "Enter Valid Credentials"
            a=Admin(self.Username,self.Password)
            a.Login()


a=Admin("","")
a.Login()

