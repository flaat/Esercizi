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

lista_numeri: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_caratteri: list = ["a", "b", "c", "d", "e"]

print(range(10))

for indice in range(len(lista_numeri)):
    
    if indice < len(lista_caratteri):
        print(f"{lista_numeri[indice]=} -> {indice=}")
        
    print(f"{lista_caratteri[indice]=} -> {indice=}")
