import requests

api_url = "http://localhost:3000"

flag = True
flag2 = True

while flag == True:
    print("Hola!! Bienvenido al sistema de correos fans de lol")
    mail = input("Ingrese su correo: " )
    contra = input("Ingrese su contraseña: ")
    
    datos = {
        "correo" : mail,
        "password" : contra
    }
    
    res = requests.get(api_url+"/api1-1/verificar",params = datos)
    print(res.text)
    
    if "true" in res.text:
        print("\nLogeado correctamente :D\n")
        
        while flag2 == True:
            print("1. Ver información correo electrónico")
            print("2. Ver correos marcados como favoritos")
            print("3. Marcar correo como favorito")
            print("4. Bloquear correo D:")
            print("5. Terminar con la ejecucion del cliente")
            resp = input("Elige: ")
            
            if resp == "1":
                info_correo = input("Ingrese correo que desea informacion: ")
                res = requests.get(api_url+"/api1-1/informacion/"+info_correo)
                print("\n" +res.text+ "\n")
                
            elif resp == "2":
                info_correo = input("Ingrese su correo: ")
                info_contrasena = input("Ingrese su contraseña: ")
                
                datos = {
                    "correo": info_correo,
                    "password": info_contrasena
                }
                res = requests.get(api_url+"/api1-1/info_favoritos",params = datos)
                print("\n" +res.text+ "\n")
                
            elif resp == "3":
                
                info_correo = input("Ingrese su correo: ")
                info_contrasena = input("Ingrese su contraseña: ")
                info_correo_fav = input("Ingrese correo favorito: ")
                
                datos = {
                    "correo" : info_correo,
                    "password": info_contrasena,
                    "correo_favorito": info_correo_fav
                }
                res = requests.post(api_url+"/api1-1/marcarcorreo",json = datos)
                print("\n" +res.text+ "\n")
                
                
            elif resp == "4":
                
                info_correo = input("Ingrese su correo: ")
                info_contrasena = input("Ingrese su contraseña: ")
                info_correo_bloq = input("Ingrese correo a bloquear: ")
                
                datos = {
                    "correo" : info_correo,
                    "clave": info_contrasena,
                    "correo_bloquear": info_correo_bloq
                }
                
                res = requests.post(api_url+"/api1-1/bloquear",json = datos)
                print("\n" +res.text+ "\n")
                
            elif resp == "5":
                print("Fin del cliente adios viejo")
                flag = False
                flag2 = False
                