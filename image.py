import numpy as np
import pandas as pd
import math

def find_correction(csvFile):

    csvDataFrame = pd.read_csv(csvFile)
    numpyArr = csvDataFrame.values
    numpyArr = np.delete(numpyArr,(0),axis=0)
    numpyLength = len(numpyArr)
    firstBottom = True
    firstRight = True
    
    for i in range(0,numpyLength):
        for j in range(0,numpyLength):  
            
            if(numpyArr[i][j] == 1 and firstBottom):
                bottom = [j,i] #top
                firstBottom = False   
            if(numpyArr[j][i] == 1 and firstRight):
                right=[i,j]
                firstRight=False
    
    slope = (bottom[1] - right[1]) / (bottom[0]-right[0]) #  m = (y2-y1)/(x2-x1)
    correction_angle = math.degrees(math.atan(slope)) 

    return correction_angle   
    
	
if __name__ == "__main__":
	angle=find_correction('rotated.csv')
	print(angle)