import sys
import json
import numpy


def jsonIterator(json_file):
    with open(json_file) as fh:
        for line in fh:
            yield json.loads(line)
            
def findBarcodesAndGenes(infile):
    xys = []
    genes = []
    barcode_gene_corr = {}
    for row in jsonIterator(infile):
        #print row
        xy = "x" + str(row["x"]) + "y" + str(row["y"])
        if not xy in xys:
            xys.append(xy)
            barcode_gene_corr[xy] = {}
        barcode_gene_corr[xy][row["gene"]] = 1
        if not row["gene"] in genes: 
            genes.append(row["gene"])
    #bid = dict([(id, i) for (i, id) in enumerate(barcodes)]) #get new list from dict
    gid = dict([(id, i) for (i, id) in enumerate(genes)])
    
    print len(xys)
    
    trimmed_barcode_gene_corr = {}
    
    trimmed_barcode_list = []
    
    for barcode, gene_hits in barcode_gene_corr.iteritems():
        #print barcode
        #print gene_hits
        if len(gene_hits) > 500:
            #print gene_hits
            trimmed_barcode_gene_corr[barcode] = gene_hits
            trimmed_barcode_list.append(barcode)
    
    print len(trimmed_barcode_list)
    
    bid = dict([(id, i) for (i, id) in enumerate(trimmed_barcode_list)])
    
    #bid = dict([(id, i) for (i, id) in enumerate(barcodes)])
    
    #expression_per_feature = numpy.zeros([len(barcodes)+1, len(genes)+1]) #plus one for column and row headers
    
    expression_per_feature = numpy.zeros([len(trimmed_barcode_list), len(genes)])
    
    #adding row headers (barcode IDs)
    #for i in range(len(barcodes)): 
    #    expression_per_feature[i+1, 0] = bid[barcodes[i]]
    
    #adding column headers (gene IDs)
    #for i in range(len(genes)): 
    #    expression_per_feature[0, i+1] = gid[genes[i]]
    
    for barcode, gene_hits in trimmed_barcode_gene_corr.iteritems():
        for gene in genes:
            if gene in gene_hits:
                #print int(gene_hits[gene])
                #expression_per_feature[bid[barcode]+1, gid[gene]+1] = gene_hits[gene] #plus one for column and row headers
                expression_per_feature[bid[barcode], gid[gene]] = gene_hits[gene] #plus one for column and row headers
                
    print expression_per_feature.shape
    
#    for i in range(len(genes)):
#        if expression_per_feature[:,i] == 0:
            
    
                
    return expression_per_feature.astype(int), trimmed_barcode_list, genes

def saveExpressions(expression_matrix, outfile, barcodes, genes):
        print expression_matrix
        numpy.savetxt(outfile + "_matrix.txt", expression_matrix, delimiter = "\t")
        #outfile.close()
        
        with open(outfile + "_genes.txt", "w") as fh:
            for gene in genes:
                fh.write(gene + "\n")
        
        with open(outfile + "_barcodes.txt", "w") as fh:
            for barcode in barcodes:
                fh.write(barcode + "\n")
            

if __name__ == "__main__":
    infile, outfile_prefix = sys.argv[1], sys.argv[2]
    expression_matrix, barcodes, genes = findBarcodesAndGenes(infile)
    saveExpressions(expression_matrix, outfile_prefix, barcodes, genes)