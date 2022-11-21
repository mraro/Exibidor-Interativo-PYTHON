import sys
import numpy as np
import cv2 as cv
import NDIlib as ndi
from listar import InputsNDI
from layout import layyout


def show_ndi():


    if not ndi.initialize():
        return 0

    ndi_find = ndi.find_create_v2()

    if ndi_find is None:
        return 0

    sources = []
    while True:
        if not ndi.find_wait_for_sources(ndi_find, 4000):
            print('Nenhuma nova entrada NDI encotrada')
            break
        print('Looking for sources ...')
        ndi.find_wait_for_sources(ndi_find, 1000)
        sources = ndi.find_get_current_sources(ndi_find)
    # sources = layyout(objects.listar_inputs_ndi())
    #sources2 = []
    #sources2.append(layyout(objects.listar_inputs_ndi()))
    #print(type(sources2),"   ",len(sources2),"   ",sources2)

    print(type(sources),"   ",len(sources),"   ",sources)
    sources[0] = layyout(sources)
    print(f'Found NDI src: {sources[0].ndi_name}') #url_address
    ndi_recv_create = ndi.RecvCreateV3()
    ndi_recv_create.color_format = ndi.RECV_COLOR_FORMAT_BGRX_BGRA

    ndi_recv = ndi.recv_create_v3(ndi_recv_create)

    if ndi_recv is None:
        return 0

    ndi.recv_connect(ndi_recv, sources[0])

    ndi.find_destroy(ndi_find)

    cv.startWindowThread()

    while True:
        t, v, _, _ = ndi.recv_capture_v2(ndi_recv, 5000)

        if t == ndi.FRAME_TYPE_VIDEO:
            print('Video data received (%dx%d).' % (v.xres, v.yres))
            frame = np.copy(v.data)
            cv.imshow('ndi image', frame)
            ndi.recv_free_video_v2(ndi_recv, v)

        if cv.waitKey(1) & 0xff == 27:
            break

    ndi.recv_destroy(ndi_recv)
    ndi.destroy()
    cv.destroyAllWindows()

    return 0


objects = InputsNDI()
objects.listar_inputs_ndi()
sources = objects.sources
# ndi = objects.ndi
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    show_ndi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

