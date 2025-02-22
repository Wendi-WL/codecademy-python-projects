def rgb_hex():
  invalid_msg = "Error. Invalid values have been entered."
  red = int(input("Enter red (R) value: "))
  if red > 255 or red < 0:
    print(invalid_msg)
    return
  green = int(input("Enter green (G) value: "))
  if green > 255 or green < 0:
    print(invalid_msg)
    return
  blue = int(input("Enter blue (B) value: "))
  if blue > 255 or blue < 0:
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print("%s" % (hex(val)[2:]).upper())

#rgb_hex()

def hex_rgb():
  hex_val = input("Enter the colour as a hexidecimal value (in six hexadecimal digits): ")
  if len(hex_val) != 6:
    print("Invalid hexadecimal value entered.")
    return
  else: 
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val >>= 8
  green = hex_val % two_hex_digits
  hex_val >>= 8
  red = hex_val % two_hex_digits
  print("Red: %s, Green: %s, Blue: %s" % (red, green, blue))

#hex_rgb()

def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print("RGB to Hex...")
      rgb_hex()
    elif option == "2":
      print("Hex to RGB...")
      hex_rgb()
    elif option == "x" or option == "X":
      break
    else:
      print("Error")

convert()