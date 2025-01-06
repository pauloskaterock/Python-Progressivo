# # Operadores de Comparação
# # Esses operadores comparam dois valores e retornam um valor booleano (True ou False).

# == (Igual a): Retorna True se os valores forem iguais.

# x = (5 == 3)  # x será False
# != (Diferente de): Retorna True se os valores forem diferentes.

# x = (5 != 3)  # x será True
# > (Maior que): Retorna True se o primeiro valor for maior que o segundo.

# x = (5 > 3)  # x será True
# < (Menor que): Retorna True se o primeiro valor for menor que o segundo.

# x = (5 < 3)  # x será False
# >= (Maior ou igual a): Retorna True se o primeiro valor for maior ou igual ao segundo.

# x = (5 >= 3)  # x será True
# <= (Menor ou igual a): Retorna True se o primeiro valor for menor ou igual ao segundo.

# x = (5 <= 3)  # x será False

# # 3. Operadores Lógicos
# # Usados para combinar instruções condicionais.

# and (E): Retorna True se ambas as condições forem verdadeiras.

# x = (5 > 3 and 2 < 4)  # x será True
# or (Ou): Retorna True se pelo menos uma das condições for verdadeira.

# x = (5 > 3 or 2 > 4)  # x será True
# not (Não): Inverte o valor booleano.

# x = not(5 > 3)  # x será False
# 4. Operadores de Atribuição
# Usados para atribuir valores às variáveis.

# = (Atribuição): Atribui o valor da direita à variável da esquerda.

# x = 5  # x será 5
# += (Adição e Atribuição): Adiciona o valor da direita ao valor da variável e atribui o resultado à variável.

# x += 3  # x será 8 se x era 5
# -= (Subtração e Atribuição): Subtrai o valor da direita do valor da variável e atribui o resultado à variável.

# x -= 2  # x será 3 se x era 5
# *= (Multiplicação e Atribuição): Multiplica o valor da variável pelo valor da direita e atribui o resultado à variável.

# x *= 3  # x será 15 se x era 5
# /= (Divisão e Atribuição): Divide o valor da variável pelo valor da direita e atribui o resultado à variável.

# x /= 5  # x será 1.0 se x era 5
# %= (Módulo e Atribuição): Aplica o operador módulo e atribui o resultado à variável.

# x %= 2  # x será 1 se x era 5
# **= (Exponenciação e Atribuição): Eleva a variável à potência do valor da direita e atribui o resultado à variável.

# x **= 2  # x será 25 se x era 5
# //= (Divisão Inteira e Atribuição): Aplica a divisão inteira e atribui o resultado à variável.

# x //= 2  # x será 2 se x era 5

# # 5. Operadores de Identidade
# # Usados para comparar objetos, não apenas seus valores.

# # is: Retorna True se as duas variáveis apontarem para o mesmo objeto.

# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]
# print(x is y)  # True
# print(x is z)  # False
# is not: Retorna True se as duas variáveis não apontarem para o mesmo objeto.

# print(x is not z)  # True

# # 6. Operadores de Pertinência (Membresia)
# # Usados para testar se uma sequência contém um valor.

# in: Retorna True se o valor estiver na sequência.

# x = [1, 2, 3]
# print(2 in x)  # True
# not in: Retorna True se o valor não estiver na sequência.

# print(4 not in x)  # True


# # 7. Operadores Bitwise (Operadores de Bits)
# # Operam em bits e realizam operações bit a bit.

# & (AND): Compara cada bit dos operandos. O resultado é 1 somente se ambos os bits comparados forem 1.

# x = 5 & 3  # x será 1 (em binário: 0101 & 0011 = 0001)
# | (OR): Compara cada bit dos operandos. O resultado é 1 se pelo menos um dos bits comparados for 1.

# x = 5 | 3  # x será 7 (em binário: 0101 | 0011 = 0111)
# ^ (XOR): Compara cada bit dos operandos. O resultado é 1 se os bits comparados forem diferentes.

# x = 5 ^ 3  # x será 6 (em binário: 0101 ^ 0011 = 0110)
# ~ (NOT): Inverte todos os bits do operando.

# x = ~5  # x será -6 (em binário: ~0101 = 1010, que é -6 em complemento de dois)
# << (Shift à Esquerda): Desloca os bits do operando para a esquerda pelo número de posições especificado.

# x = 5 << 2  # x será 20 (em binário: 0101 << 2 = 10100)
# >> (Shift à Direita): Desloca os bits do operando para a direita pelo número de posições especificado.

# x = 5 >> 2  # x será 1 (em binário: 0101 >> 2 = 0001)

# Esses são os principais operadores em Python. Eles são ferramentas fundamentais para realizar operações em variáveis, tomar decisões lógicas, e manip








