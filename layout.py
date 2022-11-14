import PySimpleGUI as GUI


def layyout(args):
    GUI.theme('SandyBeach')

    #combotext = 'teste','teste1','teste3'
    print(args)
    print(type(args))
    print(len(args))
    layout = [[GUI.Combo(args)],
              [GUI.Button('SALVA', font=('Times New Roman', 12)), GUI.Button('CANCELA', font=('Times New Roman', 12))]]

    win = GUI.Window("Entrada NDI", layout)

    e, v = win.read()
    if e == 'SALVA':
        print(v[0])
    win.close()


#layyout('var1', 'var2','fasfasf')