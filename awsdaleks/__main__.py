import sys
from awsdaleks import main

if __name__ == "__main__":
    exterminate = len(sys.argv) >= 2
    if exterminate:
        exterminate = "exterminate" == sys.argv[1]
    main(exterminate)