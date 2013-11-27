#!/usr/bin/env python

import sys

def fileReader(infile):
    expression_dict = {}
    #save = False
    print "in file reader func"
    for ln in open(infile, 'r'):
        #if save == True:
        print "in open file loop"
        #print ln
        ln = ln.split('\t')
        print ln
	barcode = ln[0]
        #print barcode
        expression_dict[barcode] = ln[1:]
	save = True
    return expression_dict

if __name__ == "__main__":
    infile = sys.argv[1]
    exp_dict = fileReader(infile)
    for key in exp_dict:
        print key