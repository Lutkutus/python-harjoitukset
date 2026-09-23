sukupuoli = input("Sukupuolesi: ").lower()
hemo = float(input("Kerro hemoglobiiniarvosi (g/l): "))

if sukupuoli == "mies":
    if hemo < 134:
        print("Sinulla on alhainen hemoglobiini")
    elif hemo > 195:
        print("Sinulla on korkea hemoglobiini")
    else:
        print("Sinulla on normaali hemoglobiini")
elif sukupuoli == "nainen":
    if hemo < 117:
        print("Sinulla on alhainen hemoglobiini")
    elif hemo > 175:
        print("Sinulla on korkea hemoglobiini")
    else:
        print("Sinulla on normaali hemoglobiini")
else:
    print("Virheellinen sukupuoli") 
