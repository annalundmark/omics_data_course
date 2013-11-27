#!/usr/bin/env python


import sys
import json

X_MAX = 353
X_MIN = 106
Y_MAX = 439
Y_MIN = 194

CLUSTER_BY = 6

def synthesizeDict():
    
    barcode_dict = {}
    
    k = 0
    for i in range(X_MAX - X_MIN):
        for j in range(Y_MAX - Y_MIN):
            k += 1
            barcode_dict["barcode" + str(k)] = {}
            barcode_dict["barcode" + str(k)]["x"] = i
            barcode_dict["barcode" + str(k)]["y"] = j
    
    return barcode_dict

def jsonIterator(json_file):
    with open(json_file) as fh:
        for line in fh:
            yield json.loads(line)

            
def transformJson(infile, x_dict, y_dict):
    x_lim = int(X_MAX - ((X_MAX-X_MIN) % CLUSTER_BY))
    y_lim = int(Y_MAX - ((Y_MAX-Y_MIN) % CLUSTER_BY))
    with open(infile[:-5] + str(CLUSTER_BY) + "_out.json", "w") as outfile: 
        for row in jsonIterator(infile):
            if row["x"] < x_lim and row["y"] < y_lim:
                row["x"] = x_dict[row["x"]]
                row["y"] = y_dict[row["y"]]
                outfile.write(json.dumps(row) + "\n")

def clusterx():
    
    xs = range(X_MIN, X_MAX)
    
    ys = range(Y_MIN, Y_MAX)
    
    translation_dict_x = {}
    
    x_lim = int(X_MAX - ((X_MAX-X_MIN) % CLUSTER_BY))
    j = 1
    for i in range(X_MIN, x_lim):
        translation_dict_x[i] = j
        if i % CLUSTER_BY == 0 and i != 0:
            #print i
            j += 1
        if (X_MIN +i) in xs:
            xs[xs.index((X_MIN +i))] = j
    
    translation_dict_y = {}
    
    y_lim = int(Y_MAX - ((Y_MAX-Y_MIN) % CLUSTER_BY))
    j = 1
    for i in range(Y_MIN, y_lim):
        translation_dict_y[i] = j
        if i % CLUSTER_BY == 0 and i != 0:
            #print i
            j += 1
        if (Y_MIN +i) in ys:
            ys[ys.index((Y_MIN +i))] = j

    return translation_dict_x, translation_dict_y
    

if __name__ == "__main__":
    infile = sys.argv[1]
    #test_dict = synthesizeDict()
    x_dict, y_dict = clusterx()
    transformJson(infile, x_dict, y_dict)