#! /usr/bin/env python3

import sys, glob

if len(sys.argv) != 2:
	sys.exit('For all gff files in a folder, this script computes the % coding density.\n'
	         'Usage: gffs_to_coding_density_table.py <directory_with_gffs> \n')

Script, gff_folder = sys.argv


gff_list = []
for file in glob.glob("%s/*.gff" % gff_folder):
    #print("    " + file.split('/')[-1])
    gff_list.append(file.split('/')[-1].split(".")[0])
if gff_list == []:
    sys.exit("No gff files found in the folder indicated. Aborting.")

"""
Desired output:
Contig_ID Contig_size prop_genes
"""

print("Contig_ID", "Contig_size", "Coding_density", sep = "\t")

for name in gff_list:
    GFF = open("%s/%s.gff" % (gff_folder, name), "r")
    GFF.readline()
    Contig_size = float(GFF.readline().strip().split()[-1])
    
    size_total = 0
    
    for line in GFF:
        if line.strip() == "##FASTA":
            break
        LINE = line.strip().split()
        if LINE[2] in ["CDS", "rRNA", "tRNA", "tmRNA", "ncRNA"] and not "pseudogene" in LINE[8]:
            size_total += max(float(LINE[4]), float(LINE[3])) - min(float(LINE[4]), float(LINE[3])) + 1
    
    print(name, int(Contig_size), size_total/Contig_size, sep = "\t")

