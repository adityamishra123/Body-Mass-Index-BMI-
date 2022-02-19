Height=float(input("enter your height in cm: "))
Weight=float(input("enter your weight in kg: "))
Height=Height/100
BMI=( Weight/(Height*Weight))
print("ypur body mass index is: ",BMI)
if(BMI>0):
    if (BMI<=16):
        print("you are severaly underweight")
    elif(BMI<=18.5):
        print("you are underweight")
    elif(BMI<=25):
        print("you are healthy")
    elif(BMI<=30):
        print("you are underweight")
    else:
        print("you are severely overweight")
else:
    ("enter valid details")


