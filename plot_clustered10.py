#!/usr/bin/env python

import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
cm = matplotlib.cm.get_cmap('YlOrRd')

def create_plot(x,y, colros, plotfile): 
	plt.scatter(x, y, c=colors, s=10, lw=0)
	plt.axis('scaled')
	plt.xlim(1, 24)
	plt.ylim(1,24)
        
        #change to colors? 
        #for i in range(len(nr)):
        #    plt.annotate(str(nr[i]),xy=(x[i],y[i]))
        
        
        
        
	#plt.colorbar()
	plt.savefig(plotfile)

if __name__ == "__main__":
    plotfile = sys.argv[1]
    
    x = [5,11,4,4,10,6,6,9,12,12,12,12,7]
    y = [13,7,7,12,3,14,13,8,2,6,5,4,4]
    
    colors = ["grey", "orange", "red", "orange", "blue", "blue", "blue", "orange", "purple", "grey", "grey", "green", "grey"]

    
    create_plot(x, y, colors, plotfile)