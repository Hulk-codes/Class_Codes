import threading                

def display():                         
    print("inside display function: ", threading.get_ident())               
    for i in range(100):
        print("inside display")                                 

def main():
    print("inside main: ", threading.get_ident())
   
    t = threading.Thread(target=display)    
    t.start()           
    t.join()
    
    print("End of main")
    
if __name__ == "__main__":                                  
    main()