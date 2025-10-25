""" Gere 1 byte em binário e mostre o valor em decimal do número gerado.
Ex: 
Gerado:   01010111
Decimal:  87 """
import random

byte_gerado = ''.join(random.choice('01') for numero in range(8))

valor_decimal = int(byte_gerado, 2)

print(f"Gerado: {byte_gerado}")
print(f"Decimal: {valor_decimal}")