# creating your own Python module or package

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")
    
def goodbye(name):
    print(f"goodbye, {name}")
    

# special variable whose value is automatically set in python to be
# "main" when you run a file from the command line
if __name__ == "__main__":
    main()    
