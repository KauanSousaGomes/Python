
numero_placa= input ("Digite o numero final da placa do veiculo: ")

match numero_placa:
    case "1"| "2": print("Rodizio na segunda")
    case "3"| "4": print("Rodizio na terça")
    case "5"| "6": print("Rodizio na quarta")
    case "7"| "8": print("Rodizio na quinta")
    case "9"| "0": print("Rodizio na sexta")
    case _:print("Final de plava invalido")

