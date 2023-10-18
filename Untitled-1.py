nombre = input("Su nombre es: ")
print (f"{len(nombre)} son las letras en total de su nombre")

profesion = input("Cual es su profesion: ")
payaso = 1,500
doctor = 6,000
profesor = 2,500

if profesion == "payaso" or profesion == "Payaso":
    confirmacion= input("Trabaja usted en el entretimiento. si o no? ")
    if confirmacion == "si":
        print (f"Usted es payaso, con un sueldo en total de ${payaso} pesos.")
    else:
        print("Espero que le este yendo bien en su trabajo.")