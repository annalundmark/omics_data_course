import sys
import json


def jsonIterator(json_file):
    with open(json_file) as fh:
        for line in fh:
            yield json.loads(line)

def corrBarcodesGenes(infile):
    barcodes = []
    genes = []
    barcode_gene_corr = {}
    sum_events = 0
    sum_hits = 0
    for row in jsonIterator(infile):
        sum_events += 1
        if not row["barcode"] in barcodes:
            barcodes.append(row["barcode"])
            barcode_gene_corr[row["barcode"]] = {}
        barcode_gene_corr[row["barcode"]][row["gene"]] = row["hits"]
        sum_hits += row["hits"]
        if not row["gene"] in genes: 
            genes.append(row["gene"])
    
    return barcodes, genes, barcode_gene_corr, sum_events, sum_hits 
   
def createStats(barcodes, genes, corr, sum_events, sum_hits):
    
    nr_genes_per_barcode = 0
    
    for barcode, gene_hits in barcode_gene_corr.iteritems():
        nr_genes_per_barcode += len(gene_hits)
    
    print "Barcodes: ", len(barcodes)
    print "Genes: ", len(genes)
    print "Unique events: ", sum_events
    print "Genes/barcode: ", nr_genes_per_barcode/float(len(barcodes))
    print "Hits/barcode: ", sum_hits/float(len(barcodes))


if __name__ == "__main__":
    infile = sys.argv[1]
    barcodes, genes, barcode_gene_corr, sum_events, sum_hits = corrBarcodesGenes(infile)
    createStats(barcodes, genes, barcode_gene_corr, sum_events, sum_hits)
    