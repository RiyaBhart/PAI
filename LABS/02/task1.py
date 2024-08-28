def areoftrapezoid():
    print("data for trapezoid : ")
    b1=int(input("enter base1: "))
    b2=int(input("enter base2 : "))
    h=int(input("enter height: "))
    print("area of trapezoid is: ",((b1+b2)/2)*h)

def areaofparallelogram():
    print("data for parallelogram : ")
    b=int(input("enter base: "))
    h=int(input("enter height: "))
    print("area of parallelogram is: ",b*h)

def volandareaofcylinder():
    print("data for cylinder : ")
    r=int(input("enter radis of cylinder : "))
    h=int(input("enter height: "))
    print("area of cylinder is : ",(2*3.14*r*h)+(2*3.14*r*r))
    print("volume of cylinder is : ",3.14*r*r*h)


areoftrapezoid()
areaofparallelogram()
volandareaofcylinder()

