#Version: Python 3.9
#Description: This is a GUI mortgage calculator that will calculate monthly payments and total payments with:
#Description: Annual Interest Rate, Number of Years, Loan Amount from user input. 

from tkinter import *
class LoanCalculator:
 
    def __init__(self):

        #Creating the window
        window = Tk()
        window.title("Loan Calculator")
        # Boxes of saying what each area is
        Label(window, text = "Annual Interest Rate").grid(row = 1,
                                          column = 1, sticky = W)
        Label(window, text = "Number of Years").grid(row = 2,
                                      column = 1, sticky = W)
        Label(window, text = "Loan Amount").grid(row = 3,
                                  column = 1, sticky = W)
        Label(window, text = "Monthly Payment").grid(row = 4,
                                      column = 1, sticky = W)
        Label(window, text = "Total Payment").grid(row = 5,
                                    column = 1, sticky = W)
 
        # use input
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar,
                     justify = RIGHT).grid(row = 1, column = 2)
        self.numberOfYearsVar = StringVar()
 
        Entry(window, textvariable = self.numberOfYearsVar,
                 justify = RIGHT).grid(row = 2, column = 2)
        self.loanAmountVar = StringVar()
 
        Entry(window, textvariable = self.loanAmountVar,
              justify = RIGHT).grid(row = 3, column = 2)
        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, textvariable =
                           self.monthlyPaymentVar).grid(row = 4,
                           column = 2, sticky = E)
 
        self.totalPaymentVar = StringVar()
        lblTotalPayment = Label(window, textvariable =
                       self.totalPaymentVar).grid(row = 5,
                       column = 2, sticky = E)
         
        # GUI button calculator for user
        btComputePayment = Button(window, text = "Calculate Payments",
                                  command = self.computePayment).grid(
                                  row = 6, column = 2, sticky = E)
        window.mainloop()
        #looping the event
 
 
    #this will calculate the total amounts
    def computePayment(self):
                 
        monthlyPayment = self.getMonthlyPayment(
        float(self.loanAmountVar.get()),
        float(self.annualInterestRateVar.get()) / 1200,
        int(self.numberOfYearsVar.get()))
 
        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get()) * 12 \
                                * int(self.numberOfYearsVar.get())
 
        self.totalPaymentVar.set(format(totalPayment, '10.2f'))
 
    def getMonthlyPayment(self, loanAmount, monthlyInterestRate, numberOfYears):
        # compute the monthly payment.
        monthlyPayment = loanAmount * monthlyInterestRate / (1
        - 1 / (1 + monthlyInterestRate) ** (numberOfYears * 12))
        return monthlyPayment;
        root = Tk()
        # don't forget the widget
 
 # this will call the class for calculations
LoanCalculator()
