import threading

def display():
    print("inside display function: ", threading.get_ident())

def main():
    print("inside main: ", threading.get_ident())
   
    t = threading.Thread(target=display)    
    t.start()
    
    print("End of main")
    
if __name__ == "__main__":
    main()