#! /usr/bin/env python3

import sys

if len(sys.argv) != 2:
	sys.exit('This script prints basic statistics of all sequences within a multifasta file.\n'
	         'Usage: GCstats.py <fasta_file> \n')
Script, Fasta = sys.argv

FASTA = open(Fasta, 'r')


Sequence_list = []
Sequence = ''
for line in FASTA:   # Copying the sequence (potentially spread across multiple lines) to a single line
    if line.startswith('>'):
       if Sequence != '':   # Saves the existing Seq_heading and Sequence to a list before overwriting them
          Sequence_list.append([Seq_heading, Sequence])
          Sequence = ''
       Seq_heading = line.strip('\n')
    else:
       Sequence = Sequence + line.strip('\n').upper()

Sequence_list.append([Seq_heading, Sequence]) # Saves the final sequence (Seq_heading and Sequence) to a list
       
FASTA.close()

print("Contig_name", "Contig_length", "GC%", "N%", "Gap%", "Other%", sep = "\t")
for entry in Sequence_list:
    GC_count = 0
    AT_count = 0
    N_count = 0
    Gap_count = 0
    Other_count = 0
    for char in entry[1]:
        if char == "G" or char == "C":
            GC_count += 1
        elif char == "A" or char == "T":
            AT_count += 1
        elif char == "N":
            N_count += 1
        elif char == "-":
            Gap_count += 1
        else:
            Other_count += 1
    
    print(entry[0].strip(">"), len(entry[1]), "{:10.2f}".format(GC_count/(GC_count+AT_count)*100), "{:10.2f}".format(N_count/len(entry[1])*100), "{:10.2f}".format(Gap_count/len(entry[1])*100), "{:10.2f}".format(Other_count/len(entry[1])*100), sep = "\t")