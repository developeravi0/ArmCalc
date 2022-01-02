def armcalc():
    print("Activated Armstrong number calculator")
    arm=int(input("Enter number to check if its armstrong or not : "))
    list=[int(a) for a in str(arm)]
    list2=[]
    length=len(list)
    for i in list:
        arm1=i**length
        list2.append(arm1)
    final=int(sum(list2))
    if arm==final:
        print(f"{arm} is an armstrong number")
    else:
        print(f"{arm} is not an armstrong number")
    print("Exited Armstrong number calculator")
if __name__ == "__main__":
    armcalc()