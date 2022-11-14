import NDIlib as ndi
import time
from layout import layyout


class InputsNDI:

    def __init__(self):
        self.getout = None
        self.status = None
        self.sources = None
        self.tempo = None
        self.ndi_find = None
        self.lista_inputs = []

    def listar_inputs_ndi(self):

        if not ndi.initialize():
            self.status = "Sem SDK"
        self.ndi_find = ndi.find_create_v2()

        if self.ndi_find is None:
            self.status = "NDI vazio"

        self.tempo = time.time()

        # print(tempo)
        while time.time() - self.tempo < 1.0 * 60:
        #for i in range(2):
            if not ndi.find_wait_for_sources(self.ndi_find, 4000):
                break
                print('Nenhuma entrada NDI encotrada')
            self.sources = ndi.find_get_current_sources(self.ndi_find)
            print('Entradas encontradas: %s' % len(self.sources))
            # for s in self.sources:
            for s in self.sources:

                self.lista_inputs.append(s.ndi_name)
                # self.getout = self.lista_inputs
                #print(s.ndi_name)
                # continue
                # return self.lista_inputs


            # layyout(self.lista_inputs)
            # return self.getout

        ndi.find_destroy(self.ndi_find)
        ndi.destroy()
        retorno = tuple(self.lista_inputs)
        return list(self.lista_inputs)
        print(self.status)
        # return 0
