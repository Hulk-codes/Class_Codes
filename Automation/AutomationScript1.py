import sys

def main():
    Border = "-" * 40
    print(Border)
    print("------- Marvellous Automation ----------")
    print(Border)

    if (len(sys.argv) == 2):
        if ((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to perform _____")
            print("This is a automation script")

   
        elif ((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1: ______________")
            print("Argument2: ______________")

        else:
            print("Use the given flag as : ")
            print("--u : used to display the usage")
            print("--h : use to display help")

    else:
        print("Invalid number of command line arguments")
        print("Use the given flag as : ")
        print("--u : used to display the usage")
        print("--h : use to display help")

    print(Border)
    print("-----Thank you for using our script-----")
    print("------- Marvellous Infosystems ---------")
    print(Border)


if __name__=="__main__":
    main()