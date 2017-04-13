print("First Module's name: {}".format(__name__))

def main():
    print('executed directly')

if __name__ == '__main__':
    main()

a = 3

def fn():
    print('function called from another module')