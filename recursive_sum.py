def main():
    # Define um número
    number = 10

    # Printa o resultado e chama a função
    print(calc_total(number))

def calc_total(number):
    # Verifica se o número é menor ou igual a 1
    if number <= 1:
        return number
    else:
        # Soma o número com o seu valor - 1
        return number + calc_total(number - 1)

if __name__ == '__main__':
    main()