#!/usr/bin/env python

import sys
import json


def jsonIterator(json_file):
    with open(json_file) as fh:
        for line in fh:
            yield json.loads(line)
            
def CorrBarcodesAndCoords(infile):
    barcodes = []
    x_coords = []
    y_coords = []
    for row in jsonIterator(infile):
        if not row["barcode"] in barcodes:
            #print "adding barcode"
            #print row["barcode"]
            #print row["x"]
            #print row["y"]
            barcodes.append(row["barcode"])
            x_coords.append(row["x"])
            y_coords.append(row["y"])

    return barcodes, x_coords, y_coords

def findBarcodeCoords(barcode, barcode_list, x_coords, y_coords): 
    if barcode in barcode_list:
        print "in if cond"
        print barcode, x_coords[barcode_list.index(barcode)], y_coords[barcode_list.index(barcode)]

def getMax(x_coords, y_coords):
    print max(x_coords)
    print min(x_coords)
    print max(y_coords)
    print min(y_coords)

    
if __name__ == "__main__":
    infile, barcode = sys.argv[1], sys.argv[2]
    barcodes, x_coords, y_coords = CorrBarcodesAndCoords(infile)
    findBarcodeCoords(barcode, barcodes, x_coords, y_coords)
    getMax(x_coords, y_coords)
    