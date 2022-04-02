nome = input("Nome:")
altura = input("Altura(m):")
massa = input("Massa(kg):")

imc = massa/(altura*altura)

print("Nome\tAltura\tMassa\tIMC\n{}\t{}\t{}\t{:.2f}",format(nome,altura,massa,imc))