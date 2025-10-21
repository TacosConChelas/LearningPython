def main():
    temperatura = float(input("Type the temperature in Cª: "))
    print(c_to_f(temperatura))
def c_to_f(celcius):
    return celcius * (9/5) + 32

main()