import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):

    Border = "-" * 50

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
    print("Log File gets created with name: " , FileName)

    fobj = open(FileName, "w")
    fobj.write(Border+"\n")
    fobj.write("-----Marvellous Platform Surveillance System------\n")
    fobj.write("Log Created at: "+time.ctime()+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("------------------System Report-------------------\n")

    # print("CPU usage: ", psutil.cpu_percent())
    fobj.write("CPU usage : %s %%\n" %psutil.cpu_percent())

    fobj.write(Border+"\n")

    mem = psutil.virtual_memory()
    # print("RAM Usage: ", mem.percent)
    fobj.write("RAM Usage: %s %%\n" %mem.percent)

    fobj.write(Border+"\n")

    fobj.write("\n Disk Usage Report")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            # print(f"{part.mountpoint} used {usage.percent}%%")
            fobj.write("%s --> %s %% Used \n" %(part.mountpoint, usage.percent))
        except:
            pass

    fobj.write(Border+"\n")


    net = psutil.net_io_counters()
    fobj.write("\nNetwork Usage Report\n")
    fobj.write("Sent : %.2f MB\n" %(net.bytes_sent /(1024 * 1024)))
    fobj.write("Recv : %.2f MB\n" %(net.bytes_recv /(1024 * 1024)))
    fobj.write(Border+"\n")

    #Process LOG
    Data = ProcessScan()    
    for info in Data:
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("PUserName : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("StartTime : %s\n" %info.get("create_time"))
        fobj.write("CPU %% : %.2f\n \n" %info.get("cpu_percent"))
        fobj.write("Memory %% : %.2f\n \n" %info.get("memory_percent"))
        fobj.write(Border+"\n")


    fobj.write(Border+"\n")
    fobj.write("----------------End Of Log File-------------------\n")
    fobj.write(Border+"\n")

def ProcessScan():
    listProcess = []
    
    # Warm up for CPU percent
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent()
        except:
            pass

    time.sleep(0.2)

    for proc in psutil.process_iter():
        try:
            info = proc.as_dict(attrs=["pid" , "name" , "username" , "status" , "create_time"])
            # Convert create_time
            try:
                info["create_time"] = time.strftime("%Y-%m-%d %H;%M;%S", time.localtime(info["create_time"]))
            except:
                info["create_time"] = "NA"
            
            info["cpu_percent"] = proc.cpu_percent(None)
            info["memory_percent"] = proc.memory_percent()
            listProcess.append(info)
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listProcess
        
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
        

        #Apply the schedular

        schedule.every(int(sys.argv[1])).minutes.do(CreateLog, sys.argv[2])
        print("Platform Surveillance System Started Successfully")
        print("Directory Created with name: ", sys.argv[2])
        print("Time Interval in minutes: ", sys.argv[1])
        print("Press Ctrl + C to Stop the Execution")


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