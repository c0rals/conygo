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
    answers = file[target].values

    # if answers is empty, len will be 0
    if(len(answers) == 0):
        nameDivided = str(name).split()
        # it search by first + second lastname if the name is not complete
        return file[file['¿Cuál es tu nombre completo?'].str.contains(nameDivided[1]+' '+nameDivided[2])].values     

    return file[target].values

# Search answers from excel by name
def answersForName(nameList):
    for name in nameList:
        nameParsed = parseData(name)
        print(nameParsed)
        print(find_data(nameParsed))

if __name__ == '__main__':
    pass