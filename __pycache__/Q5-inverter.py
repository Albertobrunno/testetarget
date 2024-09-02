#string  invertida
string_original = input("Digite uma string para inverter: ")
string_invertida = ""
for caractere in string_original:
    string_invertida = caractere + string_invertida
print("String invertida:", string_invertida)
