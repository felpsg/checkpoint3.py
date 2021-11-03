def main():
    # Cria um dicionário
    my_dict = {}
    
    # Abre o arquivo com os nomes e o transforma e passa seus valores pro my_dict
    with open('names.txt') as fhand:
        index = 0
        for line in fhand:
            val = line
            my_dict[int(index)] = val
            index += 1

    # Printa o resultado
    print(clean_lst_name(my_dict))

def clean_lst_name(my_dict):
    # Cria um arquivo txt novo
    new_file = open('clean_names.txt', 'a')

    # Cria um set para os nomes diferentes
    name_lst = set()

    # Adiciona no arquivo apenas o nomes diferentes
    for line in my_dict.values():
        # Padroniza o nome para minúsculo
        string = line.strip('\n')
        line_lower = string.lower()

        if line_lower in name_lst:
            pass
        else:
            name_lst.add(line_lower)
            new_file.write(line_lower + '\n')

    # Fecha o arquivo e salva
    new_file.close()

    # Retorna a lista com os nomes diferentes
    return name_lst

if __name__ == '__main__':
    main()