#Questão 1

def progressaoAritmeticaOuGeometrica(num1, numx, razao):
    ''' 
        input(int) --> output(list)

        This function recieves three variables, all of them numbers, the first one num1 define the start
        if it is a arithetic progression or an geometrical progression. How does it work?
        If the number is even it does solve it as a AP, otherwise it is going to solve it as a GP.
        At the same time, the second variable(numx) is the limit, both of the progressions aren't going
        to surpass the limit numeber. The third one is a ratio, how much does the AP and GP increases 
        per step.
    '''

    if (num1,numx,razao) != (int(num1), int(numx), int(razao)):
        print('Esse número não é um inteiro')
        return None

    else:

        resto = num1%2

        if resto == 0 or num1 == 0:
            progressaoAritimetica = []

            for i in range(num1, numx, razao):
                progressaoAritimetica.append(i)
            return progressaoAritimetica

        else:
            progressaoGeometrica = [num1]

            while num1 < numx:
                num1 = num1*razao
                if num1 <= numx:
                    progressaoGeometrica.append(num1)
            return progressaoGeometrica

#QUESTÃO 2

def somaInteirosBinario(inteiro):
    '''
    input(int) --> output(int)
    This fuction does take an integer and return the sum of the algarism of the binary resultant of
    the same number.
    '''
    if inteiro < 0:
        print("O inteiro tem que ser não negativo")
        return None
    else:
        binario = format(inteiro, "b")
        soma_dos_algarismos = 0

        for i in range(len(binario)):            
            soma_dos_algarismos += int(binario[i])
        return soma_dos_algarismos

#QUESTÃO 3


'''
In england exits 8 coins avaiable, in this question we show how many possibilities are possible
to arrange these coins to get 2 pounds.
'''
libras = 2
moedas = {'1p':1, '2p':2, '5p': 5, '10p':10, '20p':20, '50p': 50, '1L':100, '2L':200}
pence = libras*100




#QUESTAO 4

somatorio = 0
for i in range(1, 1000 + 1):
    somatorio += i**i
print(somatorio)
somatorio_str = str(somatorio)
print(somatorio_str[-10:])
