"""
Exercise 5 — Smallest Subarray Containing All Unique Elements

Given an array arr, find the length of the smallest contiguous subarray that contains all 
distinct elements present in arr.
Example: arr = [a, b, c, a, b, c, b, a] — the set of unique elements is {a,b,c}; 
the smallest window containing all is [a,b,c] length = 3.
Goal: use set plus two-pointer / sliding window technique for near O(n) time.

Hint: First compute required = len(set(arr)). Then use sliding window with a dictionary of counts 
(or another structure) to know when the window contains all required distinct elements.
"""

def smallest_subarray_with_all_unique(arr: list) -> int:
    """
    Return the length of the smallest contiguous subarray 
    that contains all unique elements of arr.
    Time complexity: O(n)
    """
    # 1 Cantidad total de elementos distintos
    unique_elements = set(arr)
    required = len(unique_elements)
    
    # 2 Variables para la ventana
    window_counts = {}
    formed = 0
    left = 0
    min_length = float('inf')
    
    # 3 Expandimos la ventana con 'right'
    for right, element in enumerate(arr):
        # Agregamos el elemento al diccionario
        window_counts[element] = window_counts.get(element, 0) + 1
        
        # Si este elemento acaba de volverse "activo" (cuenta == 1)
        if window_counts[element] == 1:
            formed += 1
        
        # 4 Si ya tenemos todos los distintos, tratamos de reducir la ventana
        while formed == required:
            current_length = right - left + 1
            if current_length < min_length:
                min_length = current_length
                smallest_window = arr[left:right+1]  # opcional, solo para ver el contenido
            
            # Movemos el límite izquierdo para intentar acortar
            left_element = arr[left]
            window_counts[left_element] -= 1
            if window_counts[left_element] == 0:
                formed -= 1
            left += 1
    
    print(f"Smallest subarray: {smallest_window}")
    print(f"Length: {min_length}")
    return min_length


def main():
    arr = ['a', 'b', 'c', 'a', 'b', 'c', 'b', 'a']
    smallest_subarray_with_all_unique(arr)


if __name__ == "__main__":
    main()
