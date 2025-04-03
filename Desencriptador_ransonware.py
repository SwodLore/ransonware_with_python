from cryptography.fernet import Fernet
import os

def retornar_key():
    return open("key.key",'rb').read()

def decrypt(items, key):
    i = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        data = i.decrypt(file_data)
        
        with open(item, 'wb') as file:
            file.write(data)
            

if __name__ == '__main__':
    path = "D:/Python proyect/Ciberseguridad/Prueba de Encriptamiento"
    os.remove(path+"\\"+"Leeme.txt")
    items = os.listdir(path)
    archivos = [path+"\\"+x for x in items]
    
key = retornar_key()
decrypt(archivos,key)