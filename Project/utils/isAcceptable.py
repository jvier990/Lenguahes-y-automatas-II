def isAcceptable():
    inputClient = input('Ingrese la expresion matematica: ')
    showInput = inputClient
    inputClient = inputClient.replace(" ", "")

    numbers = {'0','1','2','3','4','5','6','7','8','9'}
    trueChars = {'*', '/', '+', '-'}
    notAcceptable = []

    for char in inputClient:
        if char not in numbers and char not in trueChars:
            notAcceptable.append(char)

    if notAcceptable:
        #print(f'Comprueba de nuevo tu expresion: {inputClient}')
        print(f'NO PROCEDE: {notAcceptable}')
    else:
        print(f"{showInput}: PROCEDE.")
