'''
Created on Jun 27, 2015

@author: puneeth
'''

#!/usr/bin/python

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "h", ["ifile=", "ofile="])
        for opt, arg in opts:
            if opt == '-h':
                print 'test.py -i <inputfile> -o <outputfile>'
                sys.exit()
            elif opt in ("-i", "--ifile"):
                inputfile = arg
            elif opt in ("-o", "--ofile"):
                outputfile = arg
        print 'Input file is "', inputfile
        print 'Output file is "', outputfile
    except getopt.GetoptError:
        print 'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
