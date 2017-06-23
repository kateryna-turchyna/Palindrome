#code to check if a string is a palindrome or not 
while True:
    question=input("do you want to use a palindrom program: yes/no ")
    if question == 'yes':
        test = input("Enter Your word: ")
        test_trim=test.replace(" ", "")
        test_rev = reversed(test_trim)
        if list(test)==list(test_rev):
            print("it is palindrome")
        else:
            print("it`s not a palindrome")
    else:
        print("thank you")


