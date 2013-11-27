#!/usr/bin/env python

import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
cm = matplotlib.cm.get_cmap('YlOrRd')

def create_plot(x,y, colors,plotfile): 
	plt.scatter(x, y, c=  colors, s=10, lw=0)
	plt.axis('scaled')
	plt.xlim(106, 353)
	plt.ylim(194,439)
        
        #change to colors? 
        #for i in range(len(nr)):
        #    plt.annotate(str(nr[i]),xy=(x[i],y[i]))
        
        
        
        
	#plt.colorbar()
	plt.savefig(plotfile)

if __name__ == "__main__":
    plotfile = sys.argv[1]
    
    x = [199, 184, 172, 238, 152, 154, 169, 243, 145, 159, 167, 134, 136, 130, 158, 204]
    y = [215, 256, 252, 244, 316, 330, 317, 243, 209, 219, 321, 310, 306, 282, 204, 260]
    colors = ["black", "lime", "black", "black", "lime", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black", "black"]
    
    nr = range(17)[1:]
    
    create_plot(x, y, colors, plotfile)