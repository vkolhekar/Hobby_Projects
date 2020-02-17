import json

data = json.load(open("data.json"))
x_it=0

while(x_it==0):
    print("\n\n\t\t\t   WELCOME TO WEBSTER'S DICTIONARY\n\n")
    words = str(input("Enter Word: "))
    flag=0
    for k in data:
        if(words==k):
            for i in data[k]:
                print("\n>>"+i)
            print("\n")
            flag=1
            break
    if(flag==0):
        print("\nCould not loacate word. Kindly check your spelling.")
    check_flag=0
    while(check_flag==0):
        re_enter=input("Check another word? (Y/N): ")
        if(re_enter=='y'):
            check_flag=1
            x_it=0
        elif(re_enter=='Y'):
            check_flag=1
            x_it=0
        elif(re_enter=='n'):
            check_flag=1
            x_it=1
        elif(re_enter=='N'):
            check_flag=1
            x_it=1
        else:
            print("\nWrong input. Please enter again.\n")
            check_flag=0

