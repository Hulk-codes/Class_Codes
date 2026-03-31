import psutil
import sys
import os
import time

def CreateLog(FolderName):

    Ret = os.path.exists(FolderName)
    
    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to Create Folder")
            return
    else:
        os.mkdir(FolderName)
        print("Directory LogFiles get created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName, "Marvellous_%s.log" %timestamp)
    print(FileName)

    fobj = open(FileName, "w")

    

def main():
    Border = "-" * 50
    print(Border)
    print("-----Marvellous Platform Surveillance System------")
    print(Border)

    if (len(sys.argv)== 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is Used to :")
            print("1: Create Automatic Logs")
            print("2: Executes periodically")
            print("3: Sends Mail with log")
            print("4: Store Information about Processes")
            print("5: Store Information about CPU")
            print("6: Store Information about RAM Usage")
            print("7: Store Information about Secondary storage")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("ScriptName.py TimeInterveal DirectoryName")
            print("TimeInterval: The time in minutes for periodic Scheduling")
            print("DirectoryName: The name of Directory to create auto logs")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use  --h or --u to get more details")
    
    #python3 Demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside Project logic")
        print("Time interval: ", sys.argv[1])
        print("Directory Name: ", sys.argv[2])
        CreateLog(sys.argv[2])

    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use  --h or --u to get more details")


    print(Border)
    print("----------Thank You for using our script----------")
    print(Border)
if __name__ == "__main__":
    main()