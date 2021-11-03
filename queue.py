def main():
    # Cria a fila
    my_queue = ['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins', 'Distrito Federal']

    # Define o tamanho da string que será removida
    len_to_remove = 5

    print(remove_str_queue(my_queue, len_to_remove))

def remove_str_queue(my_queue, length):
    # Cria uma nova fila
    new_queue = []

    while my_queue:
        # Retira o primeiro elemento da fila e o salva em uma variável
        element = my_queue[0]
        my_queue.remove(element)

        # Adiciona o número na nova fila apenas se ele for diferente de X
        if len(element) != length:
            new_queue.insert(0, element)

    # Transfere os números da nova fila para a antiga
    while new_queue:
        element = new_queue[0]
        new_queue.remove(element)
        my_queue.insert(0, element)

    # Retorna a fila
    return my_queue
    
if __name__ == '__main__':
    main()