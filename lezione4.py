# Definisco la funzione funzione_1
def funzione_1(param1: int, param2: int) -> int:
    
    # Sommo i due parametri
    results: int = param1 + param2
    
    # Resituisco il risultato
    return results


# Chiamo la funzione funzione_1
# risultato: int = funzione_1
# risultato_2: int = funzione_1(3, 4)

# print(f"{risultato=} {risultato_2=}")

def subtraction(param1: int, param2: int) -> str:
    """
    param1: int -> Il primo addendo
    param2: int -> Il secondo addendo
    
    return: str -> La stringa che rappresenta la sottrazione tra param1 e param2
    """
    
    return f"{param1} - {param2} = {param1 - param2}"

result: str = subtraction(3, 4)

print(result)


def division(a: float, b: float) -> float:
    """
    a: float -> Il dividendo
    b: float -> Il divisore
    
    return: float -> Il risultato della divisione tra a e b
    """
    
    return a / b

division_result: float = division(a=0, b=4)
print(f"{division_result=}")
division_result_2: float = division(b=4, a=0)

quadrati: list = [x**2 for x in range(10)]

print(f"{quadrati=}")
