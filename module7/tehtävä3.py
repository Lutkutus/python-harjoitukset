gallona = float(input("Annappa bensiinin määrä gallonoina: "))

def litrat(gallona):
    litra = gallona * 3.785
    return litra

while gallona >= 0:
    print(f"{litrat(gallona):.2f} litraa")
    gallona = float(input("Annappa uusi määrä gallonoina: "))

