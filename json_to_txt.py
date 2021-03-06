import sys
import json
import numpy


def jsonIterator(json_file):
    with open(json_file) as fh:
        for line in fh:
            yield json.loads(line)
            
def findBarcodesAndGenes(infile):
    barcodes = []
    genes = []
    sum_hits = 0
    barcode_gene_corr = {}
    for row in jsonIterator(infile):
        #print row
        if not row["barcode"] in barcodes:
            barcodes.append(row["barcode"])
            barcode_gene_corr[row["barcode"]] = {}
        #barcode_gene_corr[row["barcode"]][row["gene"]] = row["hits"]
        barcode_gene_corr[row["barcode"]][row["gene"]] = 1
        sum_hits += row["hits"]
        if not row["gene"] in genes: 
            genes.append(row["gene"])
    gid = dict([(id, i) for (i, id) in enumerate(genes)])
    
    average = sum_hits/float(len(barcodes))
    
    print "average: ", average
    
    print len(barcodes)
    
    trimmed_barcode_gene_corr = {}
    
    trimmed_barcode_list = []
    
    for barcode, gene_hits in barcode_gene_corr.iteritems():
        if len(gene_hits) > 500:
            trimmed_barcode_gene_corr[barcode] = gene_hits
            trimmed_barcode_list.append(barcode)
    
    print len(trimmed_barcode_list)
    
    bid = dict([(id, i) for (i, id) in enumerate(trimmed_barcode_list)])
    
  
    expression_per_feature = numpy.zeros([len(trimmed_barcode_list), len(genes)])

    
    for barcode, gene_hits in trimmed_barcode_gene_corr.iteritems():
        for gene in genes:
            if gene in gene_hits:
                expression_per_feature[bid[barcode], gid[gene]] = gene_hits[gene] #plus one for column and row headers
                
    print expression_per_feature.shape
    
                
    return expression_per_feature.astype(int), trimmed_barcode_list, genes

def saveExpressions(expression_matrix, outfile, barcodes, genes):
        #print expression_matrix
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