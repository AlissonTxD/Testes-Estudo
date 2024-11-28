from tokens import caminhoes

encontrado = False

def verifica_caminhao():
    global encontrado
    placa_a_ser_verificada = str(input("Coloque a placa do caminhão que deseja buscar: "))
    placa_a_ser_verificada = placa_a_ser_verificada.strip().upper()
    for caminhao in caminhoes:
        if placa_a_ser_verificada in caminhao['placa']:
            encontrado = True
            print(f"Caminhão da placa {caminhao["placa"]} tem como motorista: {caminhao["motorista"]} - {caminhao["empresa"]}.")
    if not encontrado:
        print("Caminhão não encontrado.")
    encontrado = False
    verifica_caminhao()

verifica_caminhao()