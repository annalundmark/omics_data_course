#!/usr/bin/env python

import sys
import json

def jsonIterator(json_file):
    with open(json_file) as fh:
        for line in fh:
            yield json.loads(line)
            
def main(infile):
    with open(infile[:-5] +"_out.json", "w") as outfile: 
        for row in jsonIterator(infile):
            row["barcode"] = "hej"
            outfile.write(str(row))

if __name__ == "__main__":
    infile = sys.argv[1]
    main(infile)