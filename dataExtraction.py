import pandas as pd

## size sheet = 362 x 83

filename = 'excel_input/FORMULARIO PARA CONTROL DE SALUD ADOLESCENTE (AUTOAPLICABLE) 2022 (Respuestas).xlsx'
file = pd.read_excel(filename)

# to delete nicknames
def parseData(data):
    isNickname = False
    Nickname = ""

    for character in data:
        if(character == "(" or isNickname):
            isNickname = True
            Nickname = Nickname + character
            if(character == ")"):
                isNickname = False

    nickless = data.replace(Nickname,"")
    resp = ""

    if(nickless[0] == " "):
        for i in range (len(nickless)-1):
            resp = resp + nickless[i+1]
            if(i + 1 == len(nickless)-1):
                break
    else:
        resp = nickless

    return resp

# find data in excel by name and parse it
def find_data(name):
    target = file['¿Cuál es tu nombre completo?'] == name
    return file[target].values


if __name__ == '__main__':
    data = "(almirante) sexo"
    name = parseData(data)
    print (name)