### controller.py
### Oregon State University - CS 361
### Dylan Allen

from generate import generate_string
import time

def check_contents(var):
    """Verifies line from file contain a valid request
    
    Params: 
        var:: first line from file "key.txt"   

    Returns: 
        bool:: True/False
    """

    try:
        int(var) # If value is int type:: return True
        return True
    
    except ValueError:
        return False # If not int type:: return False

def main():
    """Start listening in key.txt"""

    while True:

        with open("key.txt","r") as pipeline:
            pipeline_contents = pipeline.readline() # Check first line of file

        if check_contents(pipeline_contents) == True: # Check if line from file contains a valid request
            with open("key.txt","w") as pipeline:
                pipeline.write(generate_string(int(pipeline_contents))) # Responce

        time.sleep(1) # Easily lowered to ~10ms (.01) if desired 

if __name__== "__main__":
    main()