import json

data = json.load(open("data.json"))
words = str(input("Enter Word: "))
flag=0
for k in data:
    if(words==k):
        for i in data[k]:
            print("\n"+i)
        print("\n")
        flag=1
        break
if(flag==0):
    print("\nCould not loacate word. Kindly check your spelling.")  