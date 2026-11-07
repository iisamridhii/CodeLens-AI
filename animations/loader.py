import time
import sys

def loader(printStatment:str):
    print(printStatment, end="", flush=True)

    spinner = ['|', '/', '-', '\\']


    for i in range(50):
        sys.stdout.write("\b" + spinner[i % 4])
        sys.stdout.flush()
        time.sleep(0.1)

   