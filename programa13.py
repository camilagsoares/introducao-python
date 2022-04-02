media = 0
nota = 0

for contador in range(1,6):
  print(contador)

  print("Digite a nota...")
  nota = int(input())
  media = nota + media
  print("Soma das notas:",media)

media = media / (contador+1)
print('Media:', media)

if (media >= 6):
  print("Hoje é sexta")

if (media < 6):
  print("Sábado é a nova segunda ")
