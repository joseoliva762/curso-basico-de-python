
def main():
    with open('numeros.txt', 'w') as f:
        for i in range(0,9):
            f.write(str(i))

if __name__ == '__main__':
    main()
