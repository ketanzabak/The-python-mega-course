
def convert_celsius_to_fahrenheit(temperatures):
    fahrenheit = []
    least_temp = -273.15
    for temperature in temperatures :
        if temperature >= least_temp :
            value = temperature * 1.8 + 32
            fahrenheit.append(value)
    return fahrenheit

def write_to_file(fahrenheit):
    file = open("example.txt",'w')
    for item in fahrenheit :
        file.write(str(item)+"\n")
    file.close()

def main():
    temperatures = [10,-20,-289,100]
    fahrenheit = convert_celsius_to_fahrenheit(temperatures)
    write_to_file(fahrenheit)


if __name__ == '__main__':
    main()
