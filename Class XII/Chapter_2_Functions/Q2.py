def calculate_area(B,H):
    A=(1/2)*B*H
    return A
b=float(input("Enter the Base of Triangle: "))
h=float(input("Enter the Height of Triangle: "))
print("The Area of the given Triangle is",calculate_area(b,h))
