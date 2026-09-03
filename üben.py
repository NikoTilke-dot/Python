
def taschenrechner():
    
    zahl1 = float(input("Gib eine erste Zahl ein: "))
    
    operator = input("Gib einen Operator ein (+, -, *, /): ")
    
    zahl2 = float(input("Gib eine zweite Zahl ein: "))
    
    if operator == "+":
        ergebnis = zahl1 + zahl2
    elif operator == "-":
        ergebnis = zahl1 - zahl2
    elif operator == "*":
        ergebnis = zahl1 * zahl2
    elif operator == "/":  
        if zahl2 == 0:
            print("Teilen durch 0 ist nicht erlaubt!")
            return
        ergebnis = zahl1 / zahl2
    else:  
        print("unerlaubter operator!")
        return
    print(f"Ergebnis: {ergebnis}")



taschenrechner()