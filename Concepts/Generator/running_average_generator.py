"""
4) ------ Running average coroutine
Build a generator averager() that, after being primed with next(g), receives 
numbers via g.send(value) and yields the current arithmetic mean after each new value. 
Keep track of a running total and count inside the generator.
"""
def main():
    avr = average()
    next(avr)
    print(avr.send(10))
    print(avr.send(1))
    print(avr.send(4))
    print(avr.send(9))
  
def average():
    total, count = 0, 0
    average = None
    while True:
        total += yield average
        count += 1
        average = total / count
        

if __name__ == "__main__":
    main()