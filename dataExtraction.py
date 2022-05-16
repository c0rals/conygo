import pandas as pd

## size sheet = 362 x 83

filename = 'excel_input/FORMULARIO PARA CONTROL DE SALUD ADOLESCENTE (AUTOAPLICABLE) 2022 (Respuestas).xlsx'
file = pd.read_excel(filename)

def sheet_size(sheet):
    tam = 0
    for cell in sheet:
        tam = tam + 1
    return tam

def find_name(name):
    target = file['¿Cuál es tu nombre completo?'] == name
    return file[target].values


if __name__ == '__main__':
    persona = find_name('Sofia anigelica torres bahamondes ')
    print(persona)