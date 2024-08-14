#Password guess
Password="THAARANI"
word=input("Enter the password: ")
while Password!=word:
    print("Sorry wrong password")
    word = input("Enter the password: ")
print("Correct password")