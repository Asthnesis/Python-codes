""""Program with two methods, 1. convert_fahrenheit that coverts celcius to fahrenheit and
2. convert_celcius that converts fahrenheit to celcius"""
#To githuhb
class Temperature:
 def __init__(self,celcius,fahrenheit):
    self.fahrenheit = fahrenheit
    self.celcius = celcius

 def convert_to_fahrenheit(self):
   print((9/5*self.celcius)+32," F")

 def convert_to_celcius(self):
   print((self.fahrenheit-32)*5/9," C")

T = Temperature(30,86)
T.convert_to_celcius()
T.convert_to_fahrenheit()