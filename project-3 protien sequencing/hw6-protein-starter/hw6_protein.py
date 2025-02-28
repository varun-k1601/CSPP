"""
15-110 Hw6 - Protein Sequencing Project
Name:
AndrewID:
"""

import hw6_protein_tests as test
import numpy as np

project = "Protein" # don't edit this

### WEEK 1 ###

'''
readFile(filename)
#1 [Check6-1]
Parameters: str
Returns: str
'''
def readFile(filename):
    with open(filename, 'r') as file:
        data = file.read()
        clean_data = data.replace("\n", "")
    return clean_data



'''
dnaToRna(dna, startIndex)
#2 [Check6-1]
Parameters: str ; int
Returns: list of strs
'''
def dnaToRna(dna, startIndex):
    stop_codons = ['UAA', 'UAG', 'UGA']
    codons = []
    for i in range(startIndex, len(dna), 3):
        codon = dna[i:i+3]
        if len(codon) < 3:
            break
        rna_codon = codon.replace('T', 'U')
        codons.append(rna_codon)
        if rna_codon in stop_codons:
            break
    
    return codons



'''
makeCodonDictionary(filename)
#3 [Check6-1]
Parameters: str
Returns: dict mapping strs to strs
'''
def makeCodonDictionary(filename):
    import json
    with open(filename, 'r') as file:
        amino_acid_to_codons = json.load(file)
    codon_amino_acid = {}
    for amino_acid, codons in amino_acid_to_codons.items():
        for codon in codons:
            rna_codon = codon.replace('T', 'U')
            codon_amino_acid[rna_codon] = amino_acid
    return codon_amino_acid



'''
generateProtein(codons, codonD)
#4 [Check6-1]
Parameters: list of strs ; dict mapping strs to strs
Returns: list of strs
'''
def generateProtein(codons, codonD):
    protein = []
    start_found = False 
    for codon in codons:
        if not start_found:
            if codon == "AUG":
                protein.append("Start")
                start_found = True
            continue
        if codon in codonD:
            amino_acid = codonD[codon]
            if amino_acid == "Stop":
                protein.append("Stop")
                break
            protein.append(amino_acid) 
    return protein



'''
synthesizeProteins(dnaFilename, codonFilename)
#5 [Check6-1]
Parameters: str ; str
Returns: 2D list of strs
'''
def synthesizeProteins(dnaFilename, codonFilename):
    dna = readFile(dnaFilename)
    codonD = makeCodonDictionary(codonFilename)    
    total_bases = len(dna)
    unused_bases = 0
    proteins = []   
    i = 0
    while i < total_bases:
        if dna[i:i+3] == "ATG":
            rna_sequence = dnaToRna(dna, i)
            protein = generateProtein(rna_sequence, codonD)
            proteins.append(protein)
            i += 3 * len(rna_sequence)
        else:
            i += 1
            unused_bases += 1
    print(f"Total bases: {total_bases}")
    print(f"Unused bases: {unused_bases}")
    print(f"Total proteins synthesized: {len(proteins)}")
    return proteins



def runWeek1():
    print("Human DNA")
    humanProteins = synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    print("Elephant DNA")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")


### WEEK 2 ###

'''
commonProteins(proteinList1, proteinList2)
#1 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs
Returns: 2D list of strs
'''
def commonProteins(proteinList1, proteinList2):
    common_proteins = []
    for protein in proteinList1:
        if protein in proteinList2 and protein not in common_proteins:
            common_proteins.append(protein)
    return common_proteins



'''
combineProteins(proteinList)
#2 [Check6-2]
Parameters: 2D list of strs
Returns: list of strs
'''
def combineProteins(proteinList):
    combined_amio_acids = []
    for protein in proteinList:
        combined_amio_acids.extend(protein)
    return combined_amio_acids


'''
aminoAcidDictionary(aaList)
#3 [Check6-2]
Parameters: list of strs
Returns: dict mapping strs to ints
'''
def aminoAcidDictionary(aaList):
    aa_dict = {}
    for aa in aaList:
        if aa in aa_dict:
            aa_dict[aa] += 1
        else:
            aa_dict[aa] = 1
    return aa_dict


'''
findAminoAcidDifferences(proteinList1, proteinList2, cutoff)
#4 [Check6-2]
Parameters: 2D list of strs ; 2D list of strs ; float
Returns: 2D list of values
'''
def findAminoAcidDifferences(proteinList1, proteinList2, cutoff):
    aaList1 = combineProteins(proteinList1)
    aaList2 = combineProteins(proteinList2)
    countDict1 = aminoAcidDictionary(aaList1)
    countDict2 = aminoAcidDictionary(aaList2) 
    total1 = len(aaList1)
    total2 = len(aaList2)
    amino_acid_frequencies = []
    all_amino_acids = set(countDict1.keys()).union(countDict2.keys())
    for aa in all_amino_acids:
        if aa in ["Start", "Stop"]:
            continue
        freq1 = countDict1.get(aa, 0) / total1
        freq2 = countDict2.get(aa, 0) / total2
        if abs(freq1 - freq2) > cutoff:
            amino_acid_frequencies.append([aa, freq1, freq2])
    return amino_acid_frequencies



'''
displayTextResults(commonalities, differences)
#5 [Check6-2]
Parameters: 2D list of strs ; 2D list of values
Returns: None
'''
def displayTextResults(commonalities, differences):
    print("The following proteins occurred in both DNA sequences:")
    filtered_common = [protein for protein in commonalities if protein != ["Start", "Stop"]]
    if filtered_common:
        for protein in filtered_common:
            print(" ", "-".join(protein))
    else:
        print(" No significant common proteins found.")
    print("\nThe following amino acids occurred at very different rates in the two DNA sequences:")
    if differences:
        for aa, freq1, freq2 in differences:
            print(f" {aa} : {round(freq1 * 100, 2)}% in Seq1, {round(freq2 * 100, 2)}% in Seq2")
    else:
        print(" No amino acids with significant frequency differences were found.")


def runWeek2():
    humanProteins = synthesizeProteins("data/human_p53.txt", "data/codon_table.json")
    elephantProteins = synthesizeProteins("data/elephant_p53.txt", "data/codon_table.json")

    commonalities = commonProteins(humanProteins, elephantProteins)
    differences = findAminoAcidDifferences(humanProteins, elephantProteins, 0.005)
    displayTextResults(commonalities, differences)


### WEEK 3 ###

'''
makeAminoAcidLabels(proteinList1, proteinList2)
#2 [Hw6]
Parameters: 2D list of strs ; 2D list of strs
Returns: list of strs
'''
def makeAminoAcidLabels(proteinList1, proteinList2):
    aaList1 = combineProteins(proteinList1)
    aaList2 = combineProteins(proteinList2)
    

    unique_amino_acids = set(aaList1).union(aaList2)
    

    return sorted(unique_amino_acids)


'''
setupChartData(labels, proteinList)
#3 [Hw6]
Parameters: list of strs ; 2D list of strs
Returns: list of floats
'''
def setupChartData(labels, proteinList):
    aaList = combineProteins(proteinList)
    aaCounts = aminoAcidDictionary(aaList)
    
    total_aa = len(aaList)
    
    frequencies = []
    for label in labels:
        freq = aaCounts.get(label, 0) / total_aa if total_aa > 0 else 0
        frequencies.append(freq)
    
    return frequencies


'''
createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None)
#4 [Hw6] & #5 [Hw6]
Parameters: list of strs ; list of floats ; str ; list of floats ; str ; [optional] list of strs
Returns: None
'''
def createChart(xLabels, freqList1, label1, freqList2, label2, edgeList=None):
    import matplotlib.pyplot as plt
    bar_width = 0.4
    x = np.arange(len(xLabels))
    plt.bar(x - bar_width / 2, freqList1, width=bar_width, label=label1)
    plt.bar(x + bar_width / 2, freqList2, width=bar_width, label=label2)
    
    plt.xticks(x, xLabels, rotation=90)
    plt.xlabel("Amino Acids")
    plt.ylabel("Frequency")
    plt.title("Amino Acid Frequency Comparison between Genes")
    
    plt.legend()
    
    plt.tight_layout()
    plt.show()


'''
makeEdgeList(labels, biggestDiffs)
#5 [Hw6]
Parameters: list of strs ; 2D list of values
Returns: list of strs
'''
def makeEdgeList(labels, biggestDiffs):
    diff_amino_acids = {item[0] for item in biggestDiffs}  

    edgeList = ["black" if label in diff_amino_acids else "white" for label in labels]
    
    return edgeList


'''
runFullProgram()
#6 [Hw6]
Parameters: no parameters
Returns: None
'''
def runFullProgram():
    dna_file1 = "data/human_p53.txt"  
    dna_file2 = "data/elephant_p53.txt"


    proteinList1 = synthesizeProteins(dna_file1, "data/codon_table.json")
    proteinList2 = synthesizeProteins(dna_file2, "data/codon_table.json")

    common_proteins = commonProteins(proteinList1, proteinList2)

    differences = findAminoAcidDifferences(proteinList1, proteinList2, 0.005)

    displayTextResults(common_proteins, differences)

    labels = makeAminoAcidLabels(proteinList1, proteinList2)
    freqList1 = setupChartData(labels, proteinList1)
    freqList2 = setupChartData(labels, proteinList2)

    edgeList = makeEdgeList(labels, differences)

    createChart(labels, freqList1, "Human p53 Gene", freqList2, "Elephant p53 Gene", edgeList)


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    print("\n" + "#"*15 + " WEEK 1 TESTS " +  "#" * 16 + "\n")
    test.week1Tests()
    print("\n" + "#"*15 + " WEEK 1 OUTPUT " + "#" * 15 + "\n")
    runWeek1()

    ## Uncomment these for Week 2 ##
 
    print("\n" + "#"*15 + " WEEK 2 TESTS " +  "#" * 16 + "\n")
    test.week2Tests()
    print("\n" + "#"*15 + " WEEK 2 OUTPUT " + "#" * 15 + "\n")
    runWeek2()


    ## Uncomment these for Week 3 ##

    print("\n" + "#"*15 + " WEEK 3 TESTS " +  "#" * 16 + "\n")
    test.week3Tests()
    print("\n" + "#"*15 + " WEEK 3 OUTPUT " + "#" * 15 + "\n")
    runFullProgram()