def calculate_area(Shape_Type,B,H):
    if Shape_Type=="Rectangle":
        A=B*H
    else:
        A=(1/2)*B*H
    return A
shape=input("Enter the Type of Shape: ")
if shape.lower() in ("rect","rectangle","r","sqaure","s"):
    shape="Rectangle"
elif shape.lower() in ("triangle","t","tri"):
    shape="Triangle"
else:
    print("Shape NOT DEFINED")
    quit()
    
b=float(input("Enter the Dimensions: "))
h=float(input("Enter the Dimensions: "))
print("The Area of the given Figure is",calculate_area(shape,b,h))
