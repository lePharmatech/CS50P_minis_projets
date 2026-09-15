import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("ton nom est " + sys.argv[1])
