# Sin tener en cuenta el signo, cuál es el número más alto que podemos codificar si tenemos 16 bits?
# Opción 1:
x=pow(2,16)
print(x)

# Opción 2:
n=""
for i in range(16):
    n=n+"1"
print(n, len(n), int(n,2))

# Convierta el número 12345 a binario y a hexadecimal
n=12345
print(format(n,'b'))
print(format(n,'x'))

# Cuántos bits ocuparía el número 12345
n=12345
print(len(format(n,'b')))
