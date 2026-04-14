import sys
import os
import time
import schedule
import shutil
import hashlib
import zipfile

def make_zip(Folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = Folder + "_" +timestamp + ".zip"

    # Open the ZIP file

    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(Folder):
        for file in files:
            full_path = os.path.join(root, file)
            relative = os.path.relpath(full_path, Folder)

            zobj.write(full_path, relative)

    
    zobj.close()

    return zip_name


def Calculate_hash(path):
    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()

def BackupFiles(Source, Destination):
    Copied_files = []

    print("Creating the Backup folder for backup process")

    os.makedirs(Destination, exist_ok=True)

    for root, dirs , files in os.walk(Source):                          # this loop is to handle nested folders 
        for file in files:                                         
            src_path = os.path.join(root,file)

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination, relative)

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            # Copy the files if its new
            if((not os.path.exists(dest_path)) or(Calculate_hash(src_path) != Calculate_hash(dest_path))):            
                shutil.copy2(src_path, dest_path)               #copy2 function will copy the fill with meta data
                Copied_files.append(relative)

    return Copied_files


def MarvellousDataShieldStart(Source="Data"):
    Border = "-" * 50
    BackupName = "MarvellousBackup"

    print("Backup process started successfully at: " , time.ctime())
    print(Border)

    Files = BackupFiles(Source, BackupName)

    zip_file = make_zip(BackupName)

    print(Border)
    print("Backup completed successfully")
    print("Files copied : ", len(Files))
    print("Zip File gets created : ", zip_file)
    print(Border)

def main():
    Border = "-" * 50
    print(Border)
    print("----------Marvellous Data Shield System------------")
    print(Border)

    if (len(sys.argv)== 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This Script is Used to :")
            print("1: Takes auto backup at given time")
            print("2: Backup only new and updated files")
            print("3: Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the Automation script as")
            print("ScriptName.py TimeInterveal SourceDirectory")
            print("TimeInterval: The time in minutes for periodic Scheduling")
            print("SourceDirectory: Name of directory to backed up")
            
        else:
            print("Unable to proceed as there is no such option")
            print("Please use  --h or --u to get more details")
    
    #python3 Demo.py 5 Data
    elif(len(sys.argv)==3):
        print("Inside Project logic")
        print("Time interval: ", sys.argv[1])
        print("Directory Name: ", sys.argv[2])

        #Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart, sys.argv[2])

        print(Border)
        print("Data Shield System Started Successfully")
        print("Time Interval in minutes: ", sys.argv[1])
        print("Press Ctrl + C to Stop the Execution")
        print(Border)


        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use  --h or --u to get more details")


    print(Border)
    print("----------Thank You for using our script----------")
    print(Border)
if __name__ == "__main__":
    main()