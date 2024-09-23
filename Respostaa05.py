# Função para inverter uma string
def inverter_string(s):
    string_invertida = ""
    for caractere in s:
        string_invertida = caractere + string_invertida  # Adiciona o caractere no início
    return string_invertida

# Entrada de dados pelo usuário
entrada_usuario = input("Digite uma string para inverter: ")

# Inversão da string informada pelo usuário
resultado_usuario = inverter_string(entrada_usuario)
print(f"String invertida: {resultado_usuario}")

# Exemplo com string previamente definida
#string_pre_definida = "Olá, Mundo!"
#resultado_pre_definido = inverter_string(string_pre_definida)
#print(f"String invertida (pré-definida): {resultado_pre_definido}")
