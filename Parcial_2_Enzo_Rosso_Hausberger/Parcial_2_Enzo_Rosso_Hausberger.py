#Parcial 2 - Alumno: Enzo Rosso Hausberger
#import os
#os.system('cls')

"""
This function searches horizontally for a sequense of four identical letters and adds 1 to 'mutations' (a counter) if it finds such a sequence. 
Args: dna (list): The array that represents the DNA of a subject.
Returns: mutations (int): The counter where the function stores the count of sequences.
"""
def horizontal_search(dna):
    mutations = 0
    for i in dna:
        for j in range(0,3):
            if i[j] == i[j+1] == i[j+2] == i[j+3]:
                mutations += 1
    return mutations

"""
This function searches vertically for a sequense of four identical letters and adds 1 to 'mutations' (a counter) if it finds such a sequence.
Args: dna (list): The array that represents the DNA of a subject.
Returns: mutations (int): The counter where the function stores the count of sequences.
"""
def vertical_search(dna):
    mutations = 0
    for i in range(0,3):
        for j in range(0,6):
            if dna[i][j] == dna[i+1][j] == dna[i+2][j] == dna[i+3][j]:
                mutations += 1
    return mutations

"""
This function searches diagonally for a sequense of four identical letters and adds 1 to 'mutations' (a counter) if it finds such a sequence.
Args: dna (list): The array that represents the DNA of a subject.
Returns: mutations (int): The counter where the function stores the count of sequences.
"""
def diagonals_search(dna):
    mutations = 0
    for i in range(2,-1,-1):
        for j in range(0,3):
            if dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                mutations += 1
            if dna[i][5-j] == dna[i+1][4-j] == dna[i+2][3-j] == dna[i+3][2-j]:
                mutations += 1
    return mutations

"""
This function calculates the sum of alterations from horizontal_search(), vertical_search(), and diagonals_search().
Then it checks if the subject's DNA contains more than two sequences.
Args: dna (list): The array that represents the DNA of a subject.
Returns: True if mutations > 1 or False if mutations < 1 
"""
def is_mutant(dna):
    mutations = horizontal_search(dna) + vertical_search(dna) + diagonals_search(dna) 
    return mutations > 1

#Test cases:
#This 6x6 array represents the dna of cyclops
cyclops =[
    ['A', 'T', 'G', 'C', 'G', 'A'],
    ['C', 'A', 'G', 'T', 'G', 'C'],
    ['T', 'T', 'A', 'T', 'G', 'G'],
    ['A', 'G', 'A', 'A', 'G', 'G'],
    ['G', 'G', 'G', 'G', 'T', 'A'],
    ['T', 'C', 'G', 'C', 'T', 'G']
    ]

#This 6x6 array represents the dna of a common human
human = [
    ['A', 'A', 'A','A', 'G', 'G'],
    ['T', 'T', 'G', 'A', 'A', 'C'],
    ['A', 'G', 'C', 'C', 'T', 'G'],
    ['A', 'T', 'G','T', 'T', 'G'],
    ['T', 'T', 'G', 'A', 'A', 'C'],
    ['A', 'C', 'C','A', 'T', 'G']
] 

#It's a welcome mesage.
print("\033[1;33m" + "> Welcome to the Mutant Test Program" + '\033[0m')
#It print 'Sample: DNA of Cyclops' in blue and "> MUTANT DETECTED" in green if this condition is True, or "> NOT MUTANT" in red if it's Flase.
print("\033[94m" + "Test 1 - Sample: DNA of Cyclops: " + "\033[0m" + ("\033[92;1m" + f"> MUTANT DETECTED " + "\033[0m" if is_mutant(cyclops) else  "\033[91;1m" + f"> NOT MUTANT" + "\033[0m\n"))
#It print 'Sample: DNA of Human' in blue and "> MUTANT DETECTED" in green if this condition is True, or "> NOT MUTANT" in red if it's Flase.
print("\033[94m" + "Test 2 - Sample DNA of a Human: " + "\033[0m" + ("\033[92;1m" + f"> MUTANT DETECTED" + "\033[0m" if is_mutant(human) else  "\033[91;1m" + f"> NOT MUTANT" + "\033[0m\n"))  
