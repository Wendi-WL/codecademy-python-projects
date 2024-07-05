"""
This program calculates the area of circles and triangles.
"""

print("The calculator is starting now")

option = input("Enter C for circle or T for Triangle: ")

if option == "C":
  radius = float(input("Input the radius of the circle: "))
  area = 3.14159 * radius ** 2 
  print("The area of the circle is: %f" % (area))
elif option == "T":
  base = float(input("Enter the base of the triangle: "))
  height = float(input("Enter the height of the triangle: "))
  area = base * height / 2
  print("The area of the triangle is: %f" % (area))
else:
  print("You've entered an invalid shape, please enter 'C' or 'T'.")

print("Program terminated, exiting...")