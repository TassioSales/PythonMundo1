algo = input("Digite algo ?")
print(f'O seu tipo e {type(algo)}')
print(f'E numerico? {algo.isalnum()}')
print(f'E alphanumerico {algo.isalpha()}')
print(f'Esta em maiusculas {algo.isupper()}')
print(f'Esta em minuscula {algo.islower()}')
print(f'Esta caqpitalizado {algo.istitle()}')
print(f'Tem espaços {algo.isspace()}')