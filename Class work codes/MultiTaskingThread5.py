import threading                

def display():                         
    print("inside display function: ", threading.get_ident())               
    for i in range(10):
        print("inside display")                                 

def main():
    print("inside main: ", threading.get_ident())
   
    t1 = threading.Thread(target=display)    
    t1.start()           
    
    t2 = threading.Thread(target=display)    
    t2.start()
   
    t1.join()           
    t2.join()

    
    
    print("End of main")
    
if __name__ == "__main__":                                  
    main()