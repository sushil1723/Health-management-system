print("health management system where you can log and retrive your diet and exercise")
import datetime
def gettime():
    return datetime.datetime.now()
def log(n):
    if n==1:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person1-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person1-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==2:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person2-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person2-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==3:
        choice =int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person3-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person3-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==4:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person4-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person4-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==5:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person5-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person5-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==6:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person6-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person6-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==7:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person7-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person7-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==8:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person8-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person8-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==9:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person9-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person9-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n==10:
        choice=int(input("For log the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            Food=input("Type here\n")
            with open("person10-food.txt","a") as f:
                f.write(str([str(gettime())])+":"+Food+"\n")
                print("you have successfully entered the Food\n Thank you!(^.^)")
        elif choice==2:
            Exercise = input("Type here\n")
            with open("person10-exer.txt","a") as f:
                f.write(str([str(gettime())])+":"+Exercise+"\n")
                print("you have successfully entered the Exercise\n Thank you!(^.^)")
        else:
            print("invalid choice\n Thank you for using this system!")
    else:
        print("invalid choice\n Thank you for using this system!")
def ret(n):
    if n==1:
        choice=int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice==1:
            with open("person1-food.txt") as f:
                for i in f:
                    print(i,end="")

        elif choice==2:
            with open("person1-exer.txt") as f:
                for i in f:
                    print(i,end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 2:
        choice=int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person2-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person2-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 3:
        choice=int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person3-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person3-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 4:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person4-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person4-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 5:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person5-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person5-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 6:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person6-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person6-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 7:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person7-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person7-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 8:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person8-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person8-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 9:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person9-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person9-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    elif n == 10:
        choice = int(input("For retrieve the \"Food\" press 1 and For \"Exercise\" press 2 : "))
        if choice == 1:
            with open("person10-food.txt") as f:
                for i in f:
                    print(i, end="")

        elif choice == 2:
            with open("person10-exer.txt") as f:
                for i in f:
                    print(i, end="")
        else:
            print("invalid choice\n Thank you for using this system!")
    else:
        print("invalid choise\n Thank you for using this system!")

print("*********************\"HEALTH MANAGEMENT SYSTEM\"*********************"
      "\n*********************\"HEALTH MANAGEMENT SYSTEM\"*********************"
      "\n*********************\"HEALTH MANAGEMENT SYSTEM\"*********************")
s=int(input("ENTER WHAT YOU WANT TO SAVE!\n For \"Log\" press 1 For \"Retrieve\" press 2 :"))
if s==1:
    t=int(input("enter the person from 1 to 10 : "))
    log(t)
elif s==2:
    t = int(input("enter the person from 1 to 10 : "))
    ret(t)
else:
    print("you have the choise between 1 to 10 only\nThank you very much!")