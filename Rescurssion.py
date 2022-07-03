#Version: Python 3.9
#Decription: This program will print true and false statements for words considered palindrome or not using a boolean method with recursion. 

def ifPalindrome(word):
    #It only contains letters and no spaces
    if (word.isalpha):
        #change it to lower case
        word = word.lower()
        #This will reverse the words
        reverse=word[::-1]
        #This will verify if the word in reverse is a palindrome.
        if reverse==word:
            return True
        #print flase if not a palindrome. 
        else:
            return False
    else:
        return False
def main():
    while(True):
        #This is asking for user input for word
        print("Enter a word to check: ",end="")
        user_in = input()
        #asking user when to stop
        if(user_in=="stop"):
            print("Exiting Program")
            exit()
        #printing if a palindrome or not
        print(ifPalindrome(user_in))
if __name__ == '__main__':
    main()

Output:

Enter a word to check: Able
False
Enter a word to check: was
False
Enter a word to check: I
True
Enter a word to check: ere
True
Enter a word to check: I
True
Enter a word to check: saw
False
Enter a word to check: Elba
False
Enter a word to check: A
True
Enter a word to check: man
False
Enter a word to check: a plan
False