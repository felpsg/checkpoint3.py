def main():
    # Cria a pilha
    stack = [1, 1, 2, 3, 4, 5, 6, 6, 1, 10, 2, 13, 16, 5, 2]

    # Define um número para remover
    number_to_remove = 1

    print(remove_number_stack(stack, number_to_remove))

def remove_number_stack(stack, x):
    # Cria uma nova pilha
    new_stack = []

    while stack:
        # Retira o último elemento da pilha e o salva em uma variável
        element = stack.pop()

        # Adiciona o número na nova pilha apenas se ele for diferente de X
        if element != x:
            new_stack.append(element)

    # Transfere os números da nova pilha para a antiga
    while new_stack:
        element = new_stack.pop()
        stack.append(element)

    # Retorna a pilha
    return stack
    
if __name__ == '__main__':
    main()