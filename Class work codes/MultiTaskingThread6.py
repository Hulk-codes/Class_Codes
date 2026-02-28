import threading                

def display():                         
                   
    for i in range(10):
        print("inside display : ",threading.get_ident())                                 

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