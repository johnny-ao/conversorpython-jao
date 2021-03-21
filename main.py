# Menu de opções para conversor
print('Selecione a unidade de medida para conversão:')
print('1. Comprimento.\n2. Massa.')
option = input()

# função converter comprimentos
def convert_lenght(num):
    if select == '1':
        result = num * 1000
        print('{} Km equivale a {} m.\n'.format(num, result))
    elif select == '2':
        result = num / 1000
        print('{} m equivale a {} Km.\n'.format(num, result))
    elif select == '3':
        result = num * 100
        print('{} m equivale a {} cm.\n'.format(num, result))
    elif select == '4':
        result = num / 100
        print('{} cm equivale a {} m.\n'.format(num, result))
    elif select == '5':
        result = num * 10
        print('{} cm equivale a {} mm\n'.format(num, result))
    elif select == '6':
        result = num / 10
        print('{} mm equivale a {} cm.\n'.format(num, result))

#função converter massa
def convert_weight(num):
    if select == '1':
        result = num * 1000
        print('{} T equivale a {} kg.\n'.format(num, result))
    elif select == '2':
        result = num / 1000
        print('{} Kg equivale a {} T.\n'.format(num, result))
    elif select == '3':
        result = num * 1000
        print('{} Kg equivale a {} g.\n'.format(num, result))
    elif select == '4':
        result = num / 1000
        print('{} g equivale a {} kg.\n'.format(num, result))
    elif select == '5':
        result = num * 1000
        print('{} g equivale a {} mg.\n'.format(num, result))
    elif select == '6':
        result = num / 1000
        print('{} mg equivale a {} g.\n'.format(num, result))

# Menu opções de conversão
if option == '1':
    print('1. Km -> m\n2. m -> Km\n3. m -> cm\n4. cm -> m\n5. cm -> mm\n6. mm -> cm')
    select = input()
    print('Digite o comprimento:')
    num = float(input())
    print(convert_lenght(num))
elif option == '2':
    print('1. T -> Kg\n2. Kg -> T\n3. Kg -> g\n4. g ->Kg\n5. g -> mg\n6. mg -> g')
    select = input()
    print('Digite a massa:')
    num = float(input())
    print(convert_weight(num))