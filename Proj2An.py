import sys
import numpy as np
import matplotlib.pyplot as plt

#takes a .txt file, reads it, and makes a list
if __name__ == "__main__":
    
    haveH1 = False
    haveH2 = False
    haveH3 = False

    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-input2' in sys.argv:
        p = sys.argv.index('-input2')
        InputFile2 = sys.argv[p+1]
        haveH2 = True
    if '-input3' in sys.argv:
        p = sys.argv.index('-input3')
        InputFile3 = sys.argv[p+1]
        haveH3 = True

    if haveH1:
        with open(InputFile1, "r") as f:
            myArray1 = f.read().split()

        for i in range(0, len(myArray1)):
            myArray1[i] = float(myArray1[i])
    
    if haveH2:
        with open(InputFile2, "r") as f:
            myArray2 = f.read().split()

        for i in range(0, len(myArray2)):
            myArray2[i] = float(myArray2[i])
    
    if haveH3:
        with open(InputFile3, "r") as f:
            myArray3 = f.read().split()

        for i in range(0, len(myArray3)):
            myArray3[i] = float(myArray3[i])
        
# creates a histogram of our lognorm datas
    if haveH1:
        n, bins, patches = plt.hist(myArray1, 50, facecolor='green', alpha=0.50, label="Plague Data")
        
    if haveH2:
        n, bins, patches = plt.hist(myArray2, 50, facecolor='blue', alpha=0.50,label="Serum 1")
       
    if haveH3:
        n, bins, patches = plt.hist(myArray3, 50, facecolor='red', alpha=0.50, label="Serum 2")
    plt.xlabel('Week')
    plt.ylabel('New Infections (1,000s of People)')
    plt.title('Rakghoul Plague Spread Data Vs Simulations With Anti-Plague Serum')
    plt.grid(True)
    plt.legend(loc="upper right")

            

    plt.show()
