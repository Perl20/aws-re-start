Divisas = {
    "Euro" : "€",
    "Dolar" : "$",
    "Yen" : "¥"
    }

Divisa = input("ingrese divisa")

print(Divisas.get(Divisa.title(), "La divisa no existe"))
if Divisa.title() in Divisas:
    print(Divisas[Divisa.title()])
else:
    print("la divisa no existe")