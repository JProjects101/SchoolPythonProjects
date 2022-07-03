#Version: Python 3.9
#Description: This program will create a GUI interface for users to enter height in in ft and inches and weight in pounds. 
#Description: It will then calcualte a BMI level from user input from clicking calculate.
#Description: The program will calculate users BMI level and indicate to user if they are overweight, underweight, normal, or obese. 

from tkinter import *

#Tinker class creation
root = Tk()

#Title of program
root.title('BMI Calculator')

#size of GUI interface
root.geometry("300x300")

#label area of height in feet for GUI area
height_lbl_ft=Label (root, text="Height (fts)")
height_lbl_ft.grid(row=0, column=0)

#area of entry for height in feet
height_entr_ft=Entry(root)
height_entr_ft.grid(row=0, column=1)

#label area for height in inches
height_lbl_inches=Label (root, text="Height (inches)")
height_lbl_inches.grid(row=1, column=0)

#entry area for height in inches
height_entr_inches=Entry(root)
height_entr_inches.grid(row=1, column=1)

#label area for weight in pounds
weight_lbl=Label (root, text="Weight (pounds)")
weight_lbl.grid(row=2, column=0)

#entry area for weight in pounds
weight_entr=Entry(root)
weight_entr.grid(row=2, column=1)

#area for BMI to display after calculation 
bmi_lbl=Label (root, text="", width=20)
bmi_lbl.grid(row=3, column=0)

#area of what level of BMI some if before entry
bmi_cat_lbl=Label (root, text="", width=20)
bmi_cat_lbl.grid(row=3, column=1)

#This is call the BMI after user enters information and clicks calculate. 
def calculate_bmi(ft, inches, weight):

   #white space to calculate when all information is entered. 
   if ft and ft.strip() and inches and inches.strip() and weight and weight.strip():
       ftToInches=float(ft)*12 #First convert feet to inches
       totalInches=ftToInches+float(inches); 
       bmi=(703*float(weight))/(totalInches*totalInches) 
       bmi_lbl['text']='BMI is '+str(round(bmi,2))   #this will set BMI level to two decimal places.

       #Pink is the color is someone is underweight. 
       if bmi<18.5:
           bmi_cat_lbl['text']='Category: Underweight'
           bmi_cat_lbl.config(bg="pink")

       #Green is someone is good on normal weight. 
       elif bmi>=18.5 and bmi<25:
           bmi_cat_lbl['text']='Category: Normal weight'
           bmi_cat_lbl.config(bg="green")

       #Yellow on overweight
       elif bmi>=25 and bmi<30:
           bmi_cat_lbl['text']='Category: Overweight'
           bmi_cat_lbl.config(bg="yellow")

       #Red is yelling obese! 
       elif bmi>=30:
           bmi_cat_lbl['text']='Category: Obese'
           bmi_cat_lbl.config(bg="red")

       #After BMI is calculate and displayed.  Area will now be a quit button to end program. 
       bmi_btn.config(text="Quit",command=quit)

#Defining the quit function for window to close. 
def quit():
   root.destroy()

#BMI level called back on same field of entry. 
bmi_btn=Button(root, text="Calculate", command = lambda: calculate_bmi(height_entr_ft.get(), height_entr_inches.get(),weight_entr.get()))
bmi_btn.grid(row=4, column=1)

#event loopback
root.mainloop()

