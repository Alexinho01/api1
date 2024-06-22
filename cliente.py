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
            print("4. Terminar con la ejecucion del cliente")
            resp = input("Elige: ")
            
            if resp == "1":
                info_correo = input("Ingrese correo que desea informacion: ")
                res = requests.get(api_url+"/api1-1/informacion/"+info_correo)
                print("\n" +res.text+ "\n")
                
            
        
    
    
