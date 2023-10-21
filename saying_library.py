import sys

from library_creation import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
    
