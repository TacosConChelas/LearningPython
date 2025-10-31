"""
The yield keyword turns a normal function into a generator function.
Instead of returning all the results at once (like return does),
yield lets your function produce a sequence of values one at a time, pausing after each one.

yield guarda el estado de ese objeto para después mostrarlo 
como en:
def count_up_to(n):
    for i in range(1, n + 1):
        yield i
if you put this:
    gen = count_up_to(5)
    print(gen)
output:
<generator object count_up_to at 0x000002A...>
so, you have to put this:
for num in gen:
    print(num)
ó
gen = list(count_up_to(5))
print(gen)

ya que yield te va entregando el valor de i de uno en uno conforme los vaya agarrando -- dando como resultado --> una lista
"""
def main():
    try:
        number = int(input("Escribe le tamaño dela secuencia de Fibonacci que quieres que se haga: "))
        print(f"Fibonacci sequence:\n{" ".join(str(num) for num in list(generar_fibonacci(number)))}")
    except ValueError:
        print("Enter a valid value")
def generar_fibonacci(n : int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
if __name__ == "__main__":
    main()