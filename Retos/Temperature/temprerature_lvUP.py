def main():
    while True:
        try:
            temperatura = input(f"Type the temperature in C: ").strip()
            print(f"{temperatura:.2f} Cº = {c_to_f(temperatura):.2f}")
            break
        except ValueError:
            print("Enter a correct value")
def c_to_f(celcius: float) -> float:
    return celcius * (9/5) + 32

if __name__ == "__name__":
    main()