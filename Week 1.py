# -*- coding: utf-8 -*-
"""
Created on Tue Jan  29 14:27:16 2019

@author: Xu Liang

Week 1 Problem Set Question 9
"""

class Student:
    name = ''
    studentid = 0.0
    quiz = 0.0
    project = 0.0
    final = 0.0
    
    def average(self):
        return round((self.quiz + self.project + self.final)/3, 2)
    
    def evaluategrade(self):
        if(self.average() >= 90):
            grade = 'A'
        elif(self.average() >= 80 and self.average() < 90):
            grade = 'B'
        elif(self.average() >= 70 and self.average() < 80):
            grade = 'C'
        elif(self.average() >= 60 and self.average() < 70):
            grade = 'D'
        elif(self.average() < 60):
            grade = 'F'
        return grade

        
def takeinput(target):
    target.name = input("Please enter your full name: ")
    target.studentid = int(input("Please enter your student ID: "))
    target.quiz = float(input("Please enter the grade for your quiz: "))
    target.project = float(input("Please enter the grade for your project: "))
    target.final = float(input("Please enter the grade for your final paper: "))

def display(target):
    print("Student name: " + str(target.name))
    print("Student ID: " + str(target.studentid))
    print("Average mark: " + str(target.average()))
    print("Letter grade: " + str(target.evaluategrade()))
    

Cohort3 = []

while(True):
    me = Student()
    takeinput(me)
    display(me)
    Cohort3.append(me)
    cont = input("Do you want to record another student's information? [Y/N]")
    if(cont == 'N'):
        cont = input("Do you want to display all information? [Y/N]")
        if(cont == 'Y'):
            print(" ")
            for i in range(0, len(Cohort3)):
                display(Cohort3[i])
                print(" ")
        break
