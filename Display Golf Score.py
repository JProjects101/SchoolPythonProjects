#Version: Python 3.9
#Description: After all the information is inputted into user input area and stored in the golf.txt program, this code will print players name and score.

#This will give you ouput of previous inputted gold score .txt file
def main():

#this will be the ability to only 'read' the file
    infile = open('golf.txt', 'r')

# displays the name in the golf.txt file
    name = infile.readline()

    while name != '':

# displays the score in golf.txt file
        score = infile.readline()

# seperates scores and names
        name = name.rstrip('\n')
        score = score.rstrip('\n')
# prints the names and scores
        print(name + " scored a " + score)

# read field of names
        name = infile.readline()

# end the loops
    infile.close()

# main function loopback
main()
