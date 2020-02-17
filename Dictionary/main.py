import json
import difflib

from difflib import get_close_matches
data = json.load(open("data.json"))

def suggestion(word):
    suggested_list = get_close_matches(word,data.keys())
    print("Did you mean '"+suggested_list[0]+"' instead? (Y/N) ")
    primary = input()
    if(primary=='y'or primary=='Y'):
        print("\n"+suggested_list[0]+":")
        translate_word(suggested_list[0])
    else:
        print("\nRecommended: ")
        for i in suggested_list:
            print(i)
    print("\n")


def translate_word(word):
    flag=0
    word = word.lower()
    for k in data:
        if(word==k):
            for i in data[k]:
                print("\n>>"+i)
            print("\n")
            flag=1
            break
    if(flag==0):
        print("\nCould not loacate word. Kindly check your spelling.")
        suggestion(word)



def main():
    x_it=0
    while(x_it==0):
        print("\n\n\t\t\t   WELCOME TO WEBSTER'S DICTIONARY\n\n")
        words = str(input("Enter Word: "))
        translate_word(words)
        check_flag=0
        while(check_flag==0):
            re_enter=input("Check another word? (Y/N): ")
            print("\n")
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

main()
