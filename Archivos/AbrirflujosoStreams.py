stream = open(file, mode = 'r', encoding = None)



try:
    stream = open("C:\Users\User\Desktopile.txt", "rt")
    # El procesamiento va aquí.
    stream.close()
except Exception as exc:
    print("No se puede abrir el archivo:", exc)



import sys




try:
    # Algunas operaciones con streams.
except IOError as exc:
    print(exc.errno)



import errno

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.ENOENT:
        print("El archivo no existe.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    else:
        print("El numero del error es:", exc.errno)
        
#Resultado:
#El archivo no existe.



from os import strerror

try:
    s = open("c:/users/user/Desktop/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    print("El archivo no pudo ser abierto:", strerror(exc.errno))
    
#Resultado:
#El archivo no pudo ser abierto: No such file or directory