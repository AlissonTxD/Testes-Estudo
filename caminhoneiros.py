caminhoes = [
    {"placa":"base","motorista":"base","empresa":"base"},
    {"placa":"RAW2C09","motorista":"Joel","empresa":"Zamin"},
    {"placa":"QCH7F94","motorista":"Guilherme","empresa":"base"},
    {"placa":"RAO3G78","motorista":"Carlos","empresa":"base"},
    {"placa":"RRW8C79","motorista":"Thiago","empresa":"Zamin"},
    {"placa":"RRJ3B48","motorista":"Anderson","empresa":"Zamin"},
    {"placa":"RRJ6F45","motorista":"Wesley","empresa":"Zamin"},
    {"placa":"RAV5A59","motorista":"Luis Eduardo","empresa":"base"},
    {"placa":"RAO5F50","motorista":"Pietro","empresa":"Zamin"},
    {"placa":"SPN5C87","motorista":"Miguel","empresa":"Nova Frota"},
    {"placa":"RAU6C87","motorista":"Elias","empresa":"Zamin"},
    {"placa":"JAO2D70","motorista":"Elton","empresa":"Zamin"},
    {"placa":"SPN5C37","motorista":"Erivelton"  ,"empresa":"base"},
    {"placa":"JAJ5A98","motorista":"Wesley","empresa":"Zamin"},
    {"placa":"JAH2B68","motorista":"Jhon","empresa":"Zamin"},
    {"placa":"IVS9J5G","motorista":"GAUCHO","empresa":"base"},
    {"placa":"RRJ8F80","motorista":"Ademilson","empresa":"base"},
    {"placa":"RAZGJ61","motorista":"Fernando","empresa":"base"},
    {"placa":"SPO1C32","motorista":"Marcos","empresa":"Nova Frota"},
    {"placa":"JBN8B74","motorista":"Cotonete","empresa":"Zamin"},
    {"placa":"RRI8I59","motorista":"Adevaldo","empresa":"Zamin"},
    {"placa":"base","motorista":"base","empresa":"base"},
    {"placa":"base","motorista":"base","empresa":"base"},
]

encontrado = False

def verifica_caminhao():
    global encontrado
    placa_a_ser_verificada = str(input('coloque a placa que deseja buscar: '))
    placa_a_ser_verificada = placa_a_ser_verificada.strip().upper()
    for caminhao in caminhoes:
        if placa_a_ser_verificada in caminhao['placa']:
            encontrado = True
            print(f'Caminhão da placa {caminhao["placa"]} tem como motorista: {caminhao["motorista"]} - {caminhao["empresa"]}')
    if not encontrado:
        print('Caminhâo nao encontrado')
    encontrado = False
    verifica_caminhao()

verifica_caminhao()   