import PySimpleGUI as GUI
import NDIlib as ndi


def layyout(args):
    GUI.theme('SandyBeach')
    argos = []
    rp = None
    for s in args:
        argos.append(s.ndi_name)
    # combotext = 'teste','teste1','teste3'
    # print(args)
    # print(type(args))
    # print(len(args))

    layout = [[GUI.InputCombo(argos, default_value=argos[0])],

              [GUI.Button('SALVA', font=('Times New Roman', 12)), GUI.Button('CANCELA', font=('Times New Roman', 12))]]

    win = GUI.Window("Entrada NDI", layout)
    # print(win.read())
    e, v = win.read()
    if e == 'SALVA':
        argos.index(v[0])
        print(v[0], "  ", argos.index(v[0]))
        rp = args[argos.index(v[0])]
        print(rp)
    win.close()

    return rp
