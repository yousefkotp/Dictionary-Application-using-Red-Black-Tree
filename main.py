import DataStructure as ds

tree = ds.RedBlackTree()  # initialize RB-tree
DICTIONARY_NAME = "EN-US-Dictionary"


def readFile(fileName):
    file = open(fileName, "r")
    for i in file:
        if not tree.search(i.rstrip('\n')):
            tree.insert(i.rstrip('\n'))
    file.close()


while True:
    print("What do you want to do?")
    option = input(
        "1- Load \"" + DICTIONARY_NAME + "\"\t2- Print size of the Dictionary\n"
        "3- Insert Word             \t4- Look-up a Word\n"
        "5- Print Tree Height       \t6- Print Black Height of the Tree\n"
        "7- Exit\n"
        "> ")

    if option == '1':
        readFile(DICTIONARY_NAME + ".txt")
        print(DICTIONARY_NAME + " loaded successfully!")

    elif option == '2':
        print(DICTIONARY_NAME + ' currently has ' + str(tree.number_of_nodes) + ' words!')

    elif option == '3':
        s = str(input("Enter the word you want to insert: ")).strip()
        if tree.search(s.lower()):
            print("\"" + s + "\" is already in the dictionary!")
        elif len(s) > 0 and not s.isspace():
            tree.insert(s.lower())
            print('\"' + s + '\" inserted Successfully')
        else:
            print('Invalid entry')

    elif option == '4':
        s = str(input("Enter the word you want to look-up: ")).strip()
        if tree.search(s.lower()):
            print("FOUND \"" + s + '\"!')
        else:
            print("\"" + s + '\" DOES NOT EXIST IN THE DICTIONARY')

    elif option == '5':
        print(tree.heightOfTree(tree.root, 0))

    elif option == '6':
        print(tree.getBlackHeight())

    elif option == '7':
        print("Thank you for using our application! :)")
        break

    print()
