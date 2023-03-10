# PHSX815_Project2
Contains the code, figures, and pdfs related to project 2


This is contains my references and instructions for how to run the codes.

Firstly: the code for this project was taken from several locations:

1. My own code and homeworks from this class
2. Prof Rogan's github, https://github.com/crogan?tab=repositories
3.The Wikipedia for "log-normal disributions", https://en.wikipedia.org/wiki/Log-normal_distribution#Properties
4. Wikipedia for "Gamma Distributions", https://en.wikipedia.org/wiki/Gamma_distribution
5. stackoverflow https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib
6. https://www.geeksforgeeks.org/how-to-generate-random-numbers-from-a-log-normal-distribution-in-python/



Now... How to run my code.

First you will need to put the Random.py code into a folder and specify the location in the "Proj2Gen.py" code, so that import knows where to find it. Next you will need to use Proj2Gen.py to make some .txt files containing randomly generated data. Proj2An.py takes 3 files, so 3 will be sufficient. I added -mux, -alpha, and -beta commands to the Proj2Gen.py file, so mux, alpha, and beta can be changed from the commandline, to achieve distributions with different parameter values. When I run it, I preform: python3 Proj2Gen.py -mux 40 -alpha 5 -beta 1 > H1.txt . I do this to make 3 data files (changing the parameters).

Next you want to run Proj2An.py, which will make the histogram used in the project. This program will take the 3 data files made from Proj2Gen.py, read them, and make 3 arrays, which are made into a histogram comparing all 3 data sets. To run the code, here is an example: python3 Proj2An.py -input1 H1.txt -input2 H2.txt -input3 H3.txt
