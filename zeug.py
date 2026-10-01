def Taschenrechner():
   zahl1 = float(input("gebe operator nummer 1 ein:"))

   operator = input("gebe operator ein (+, -, *, /):")

   zahl2 = float(input("gebe operator nummer 2 ein:"))

   if operator == "+":
      ergebnis = zahl1 + zahl2
   elif operator == "-":
      ergebnis = zahl1 - zahl2
   elif operator == "*":
   