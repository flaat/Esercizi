# print("Hello, World!")
# lista_1: list = [1, 2, 3, 4, 5]
# lista_1.append(6)
# print(lista_1)

# matrice: list = [[2, 1], [5, 3]]
# R: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]
# G: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]
# B: list = [[24, 128, 233, 1], [10, 23, 255], [1, 0, 34]]
# B[0].append("Ciao")
# a: list = [1, 2, 3]
# b: list = [4, 5, 6]
# a.append(b)
# print(a[0][0])

# a = ["a", "b", "c"]
# a.remove("b")
# print(a)

# variabile: set = {"Ciao", 1, 1, "Ciao"}

# variabile[0]

# a = a + b
# a: str = "Flavio"
# str_1: str = f"Funzione Extend: {a}, {a}, {a} {b}"
# print(str_1)

# a.append(b)
# print(a)
# print(a[3][1])

# print(a.append(b))
# print(f"Funzione Append: {a}")


# img: list = [R, G, B]
# print(R)


# # Dichiarazione di un dizionario
# m: dict = {"a": 1, "b": 2, "c": 3}
# # Aggiunta di un elemento al dizionario
# m["d"] = 4
# print(m)
# var: int = m["a"]
# print(f"Il valore di {var=}")
# c: dict = {"i": 1, "j": 2, "k": 3}
# m["inner"] = c

# m["inner"]["k"]
# m["lista"] = [1, 2, 3, 4, 5]
# lista_1: list = [1, 2, 3, 4, 5]

# menu: dict = {"menu_estivo":{"Pizza": 15, "Pasta": 10, "Insalata": 5}}
# # print(menu["menu_estivo"]["Pasta"])
# menu_invernale: dict = {"Pizza": 20, "Pasta": 15, "Insalata": 10}
# menu["menu_invernale"] = menu_invernale
# print(menu)
# menu["menu_estivo"]["Bistecca"] = 25
# menu["menu_invernale"]["Bistecca"] = 30
# menu["menu_estivo"]["Pizza"] = 150
# menu["menu_invernale"]["Pasta"] = 213

# lista_1 = {i : i for i in range(0, 10, 2)}
# print(lista_1)
    
# for i in range(len(lista_1) - 1, -1, -1):
#     print(lista_1[i])
    
# lista_2 = ["a", "b", "c", "d", "e"]
# L = [[("a",1), ("a", 2), ("a", 3)], [("b", 1), ("b", 2), ("b", 3)], [("c", 1), ("c", 2), ("c", 3)]]
# for m in range(2):
#     for k in range(2):
#         for z in range(2):
#             for i in range(2):    
#                 for j in range(2):
#                     print(f"binario {m, k, z, i, j} decimale {m*2**4 + k*2**3 + z*2**2 + i*2**1 + j*2**0}")

                
# dict_1 = {
#     "a": {
#         "a": 1,
#         "b": 2,
#         "c": {
#             "a": 1,
#             "b": 2,
#             "c": {
#                 "k": 1
#             }
#         }
#     },
#     "b": 2,
#     "c": 3,
#     "d": 4,
#     "e": 5,
#     "f": 6,
#     "g": 7,
#     "h": 8,
#     "i": 9,
#     "j": 10
#     }          
# dict_1["a"]["c"]["b"] = 42   
# print(dict_1["a"]["c"]["b"])


# a: int = 5
# b: int = 1


# if ((a > 1) and (b < 2)) or (a > 2):
    
#     if a > 1:
#         print("Hello") 
#     elif a == 1:
#         print("World")
#     else:
#         print("Ciao")
        
# elif a < 1:
#     if a > 1:
#         print("Hello") 
#     elif a == 1:
#         print("World")
#     else:
#         print("Ciao")    
        
# else:
    
#     if a > 1:
#         print("Hello") 
#     elif a == 1:
#         print("World")
#     else:
#         print("Ciao")
         
# elif a < 1:
#     print("Hello")  

# elif a == 1:
#     print("World")  


# if a > 1:
#     print("Hello")
# elif a == 1:
#     print("World")
# else:
#     print("Ciao")    

# lista_numeri: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lista_caratteri: list = ["a", "b", "c", "d", "e"]

# print(range(10))

# for indice in range(len(lista_numeri)):
    
#     if indice < len(lista_caratteri):
#         print(f"{lista_numeri[indice]=} -> {indice=}")
        
#     print(f"{lista_caratteri[indice]=} -> {indice=}")
    

# for l in range(2):
#     for k in range(2):
#         for z in range(2):
#             for x in range(2):
#                 for y in range(2):
#                     print(f"binario {l, k, z, x, y} decimale {l*2**4 + k*2**3 + z*2**2 + x*2**1 + y*2**0}")

# R: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]
# G: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]
# B: list = [[24, 128, 233], [10, 23, 255], [1, 0, 34]]

# c: int = 15

# img:list = [R, G, B]

# for i in range(len(R)):
#     for j in range(len(R[i])):
#         R[i][j] = R[i][j] - c


# lista_1: list = [1, 2, 3, 4, 5]
# contatore: int = 0

# passwords: dict = {"Flavio": "1234", 
#                    "Giovanni": "5678", 
#                    "Marco": "91011"}

# nome_utente: str = input("Inserisci il nome utente: ")
# password: str = passwords[nome_utente]
# tentativi: int = 0

# while True:
    
#     b = input("Inserisci la password: ")
#     if b == password:
#         print("Password corretta")
#         break
#     elif tentativi == 2:
#         print("Hai esaurito i tentativi")
#         break
#     else:
#         print("Password errata")
#         tentativi += 1
   
# pass


# lista_1: list = ["a", "b", "c", "d", "e"] * 10
# contatore: int = 0

# while contatore < len(lista_1):
    
#     print(lista_1[contatore])
#     contatore += 1
    
# for lettera in lista_1:
#     print(lettera)

# import time

# seconds: int = 60

# while seconds > 0:
    
#     print(f"Mancano {seconds} secondi")
#     time.sleep(1)
#     seconds -= 1


# for i in range(10):
    
#     if i % 2 == 1:
#         continue
    
#     print(i)
    
# contatore: int = 0

# while contatore < 10:

    
#     print(contatore)
#     contatore = contatore - 1
    
# print("Ciao")

# menu: dict = {"Zuppa": 5, "Pizza": 10, "Pasta": 15, "Insalata": 5}
# ordine: dict = {"primo": "Zuppa", "secondo": "Pizza", "contorno": "Insalata"}


# totale = 0.0

# for piatto in ordine.values():
    
#     print(piatto, menu[piatto])
#     totale += menu[piatto]

# print(f"Il totale è {totale}")  

# menu:dict = {"primi":{"Pizza": 9.00, "Pasta": 10.50, "Zuppa": 7.00}}
# menu["secondi"] = {"Hamburger": 15.50, "Cotoletta": 10.00, "Salmone": 20.20}
# menu["contorni"] = {"Patatine Fritte": 5.50, "Patate al forno": 5.50, "Verdura del giorno": 7.00}
# menu["dolci"] = {"Cheesecake": 6.00, "Tiramisu'": 6.00, "Focaccia con Nutella": 6.00}
# menu["bevande"] = {"Coca Cola": 3.50, "Acqua": 1.50, "Vino": 5.00}


# temperatura_far = float(input("Inserisci la temperatura in Fahrenheit: "))

# temperatura_cel = (temperatura_far - 32) * 5/9
# print(temperatura_cel)


# dizionario_amici: dict = {"Flavio": 1, "Giovanni": 2, "Marco": 3, "Luca": 4, "Paolo": 5}

# lista = [("Flavio", 1), ("Giovanni", 2), ("Marco", 3), ("Luca", 4), ("Paolo", 5)]
  
# for key, value in lista:
#     print(f"{key}, {value}")
    
# ordine: dict = {"primi": "Pasta", "secondi": "Cotoletta", "contorni": "Patatine fritte"}
# totale = 0.0

# dict_1: dict = {"KJ 234 MK": "Ford C-Max", "UJ 341 OK": "Ferrari", "WD 431 IL": "Bugatti"}

# for license_plate, models in dict_1.items():

#     print(f"({license_plate}, {models})")
