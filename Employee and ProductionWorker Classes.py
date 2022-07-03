#Version: Python 3.9
#Description: This program will let you enter an employees name and number.  Then you will be asked to enter hourly pay and shift number which then will be stored as data. 
 
class Employee(object):
   
    def __init__(self, name, number):
        self._name = name
        self._number = number
 
    def getName(self):
        return self._name
  
    def getNumber(self):
        return self._number

class ProductionWorker (Employee):

    def __init__(self, name, number, shift,payRate):
        Employee.__init__(self, name, number)
        self._shift = shift
        self._rate = payRate

    def getShift(self):
        return self._shift

    def getRate(self):
        return self._rate

def main():
  
    empName=input('Enter employee name :')
    empNumber=int(input('Enter employee number :'))
    
    empObject=Employee(empName,empNumber)
    
    print('Employee Name: ',empObject.getName())
    print('Employee Number: ', empObject.getNumber())
  
    productionWorkerName = input('Enter ProductionWorker name :')
    productionWorkerNumber = int(input('Enter ProductionWorker number :'))
    shiftNumber = input('Enter shiftNumber :')
    hourlyPayRate = int(input('Enter hourly rate,$ :'))
  
    productionWorkerObject = ProductionWorker(productionWorkerName,
                                                        productionWorkerNumber,
                                                         shiftNumber,
                                                         hourlyPayRate)

    print('ProductionWorker Name: ', productionWorkerObject.getName())
    print('ProductionWorker Number: ', productionWorkerObject.getNumber())
    print('ProductionWorker Shift: ', productionWorkerObject.getShift())
    print('ProductionWorker Pay rate,$: ', productionWorkerObject.getRate())

if __name__ == '__main__':
    main()