# Definición de la función principal
def main():
    # Solicitar al usuario que ingrese los elementos separados por espacios
    input_data = input("Ingrese los elementos separados por espacios: ")
    # Convertir la entrada en una lista de enteros
    arr = list(map(int, input_data.split()))
    # Llamar a la función merge_sort para ordenar la lista
    sorted_arr = merge_sort(arr)
    # Mostrar los datos ordenados
    print("Datos ordenados:", sorted_arr)

# Función de ordenamiento Merge Sort
def merge_sort(arr):
    # Caso base: si la longitud del arreglo es 0 o 1, está ordenado por definición
    if len(arr) <= 1:
        return arr
    
    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Llamada recursiva para ordenar la mitad izquierda
    right_half = merge_sort(arr[mid:])  # Llamada recursiva para ordenar la mitad derecha
    
    result = []  # Lista para almacenar el resultado combinado
    left_idx, right_idx = 0, 0  # Índices para recorrer las mitades izquierda y derecha
    
    # Combinar las dos mitades ordenadas
    while left_idx < len(left_half) and right_idx < len(right_half):
        if left_half[left_idx] < right_half[right_idx]:
            result.append(left_half[left_idx])  # Agregar el elemento de la mitad izquierda
            left_idx += 1
        else:
            result.append(right_half[right_idx])  # Agregar el elemento de la mitad derecha
            right_idx += 1
    
    # Agregar los elementos restantes de la mitad izquierda y derecha (si los hay)
    result.extend(left_half[left_idx:])
    result.extend(right_half[right_idx:])
    
    return result

# Definición de la función principal
def main():
    # Solicitar al usuario que ingrese los elementos separados por espacios
    input_data = input("Ingrese los elementos separados por espacios: ")
    # Convertir la entrada en una lista de enteros
    arr = list(map(int, input_data.split()))
    # Llamar a la función merge_sort para ordenar la lista
    sorted_arr = merge_sort(arr)
    # Mostrar los datos ordenados
    print("Datos ordenados:", sorted_arr)
# Comprobar si el script se ejecuta directamente
if __name__ == "__main__":
    main()  # Llamar a la función principal
