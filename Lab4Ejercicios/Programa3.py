def paréntesis_balanceados(cadena):
    pila = []
    paréntesis_abiertos = {'(', '[', '{'}
    paréntesis_cerrados = {')', ']', '}'}
    paréntesis_correspondientes = {')': '(', ']': '[', '}': '{'}

    for caracter in cadena:
        if caracter in paréntesis_abiertos:
            pila.append(caracter)
        elif caracter in paréntesis_cerrados:
            if not pila or pila.pop() != paréntesis_correspondientes[caracter]:
                return False

    # La cadena está balanceada si la pila está vacía al final
    return not pila

# Ejemplo de uso
cadena_ejemplo = input("Ingrese una cadena de paréntesis: ")
if paréntesis_balanceados(cadena_ejemplo):
    print("Los paréntesis están balanceados.")
else:
    print("Los paréntesis no están balanceados.")