#Programmer: CyberSecurityProfessional
#Run in Python 3.9
#Version: 3.9
#Description: This program will calculate the number of words per sentence by having the user enter the file name in the user input area to calculate. 

def main():
    filename = input('Enter file name: ')
    with open(filename, 'r') as f:
        total = 0
        count = 0
        for line in f:
            total += len(line.strip().split())
            count += 1
        print('Average number of words per sentence is ' + str(total/count))

main()

Output: 

Enter file name: text.txt
Average number of words per sentence is 26.0

Process finished with exit code 0
