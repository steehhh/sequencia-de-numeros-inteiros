tamanho_sequencia = int(input("\nVamos escrever uma sequência de números inteiros!\nDigite o tamanho da sequência: "))
print("Você digitou",tamanho_sequencia, "como tamanho!\n")

contador = 1

while contador <= tamanho_sequencia:
    print(contador, "-", end=" ")
    contador +=1