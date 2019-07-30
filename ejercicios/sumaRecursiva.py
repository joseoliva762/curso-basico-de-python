def recursive_sum():
    num_input = int(input("Escribe el número a sumar:"))
    if (num_input == 0):
        return 0
    else:
        return (int(num_input)) + int(recursive_sum())

def main():
        print("La suma es: {}".format(str((recursive_sum()))))

if __name__ == '__main__':
    main()
