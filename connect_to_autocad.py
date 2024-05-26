from pyautocad import Autocad

def connect_autocad():
    try:
        acad = Autocad()
        return acad
    except:
        print("Error al conectarse a AutoCad")

