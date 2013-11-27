import sys
import json
def jason_reader(data_path):
    # reads the json file and returns a list of reads numbers
    out_list=[]
    json_data=open(data_path).read()
    data = json.loads(json_data)
    return data
        
        
def dimention_finder(data):
    #gets data from json and finds the maximum x and y dimentions
    max_x=0
    max_y=0  
    genes_set=set([])
    for cell in data:
        if int(cell['x'])>max_x:
            max_x=int(cell['x'])
        if int(cell['y'])>max_y:
            max_y=int(cell['y'])    
        if cell['gene'] not in genes_set:
            genes_set.add(cell['gene'])       
    return max_x,max_y,genes_set

if __name__=='__main__':
    data_path=sys.argv[1]
    data=jason_reader(data_path)
    x,y,genes=dimention_finder(data)
    print 'Dimentions are x: '+str(x)+' and y: '+str(y)