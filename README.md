### Scripts, resources, and tools used for data analyses underlying the manuscript,
# Widespread genomic instability in an ancient nutritional endosymbiont of cicadas
by Piotr Łukasik et al.

## Introduction
The ancient heritable nutritional endosymbiotic bacterium of cicadas, *Candidatus* Hodgkinia cicadicola (thereafter: *Hodgkinia*), has several unique characteristics relative to other bacteria. Strains from different cicada species have some of the smallest genomes and gene sets known, and are characterized some of the fastest rates of sequence evolution. Further, in many cicadas, the ancestral symbiont with tiny genomes has evolved ("split") into complexes of genetically and cytologically distinct lineages, whose genomes are particularly hard to assemble and annotate.  
  
Because of this, standard analysis and annotation tools perform poorly on Hodgkinia genomic data. Hence, we designed a set of custom tools for the data analysis, annotation, and visualization.  
  
The current repository contains scripts, reference datasets, and files that were used during the course of processing metagenomic and target enrichment datasets for over 200 cicada species, often hosting Hodgkinia at different levels of complexity.  
  
## Contents

### [ ] 1. Cicadas and their symbionts - supplementary data tables
The file, an Excel spreadsheet, contains three worksheets representing Supplementary Tables S1-S3 in the manuscript. These are:  
   S1. List of all cicada specimens used in this study, including collection metadata, taxonomic information, results of screens for different symbionts, and NCBI accession numbers;
   S2. List of cicada specimens where *Hodgkinia* was identified, with preliminary information about their complexity
   S3. The details of Hodgkinia complex assemblies from different cicada species
   S4. The results of annotation of individual *Hodgkinia* contigs
   S5. The results of annotation of *Hodgkinia* contigs from different cicadas

### [ ] 2. *Hodgkinia* annotation tools
The custom Hodgkinia annotation script was originally developed by Piotr Łukasik and used for three papers that presented the cicada symbionts and their mitochondrial genomes (refs). It was later developed as "symcap" by Diego Castillo Franco, for the purpose of annotating planthopper symbionts. Here, we provide the version of the script that was used for the annotation of the current Hodgkinia dataset, alongside reference files, input and output files, and a script for processing data tables.  

### [ ] 3. Visualization of *Hodgkinia* metagenomic assemblies
Plotting metagenomic contigs in coverage vs. GC contents space, with size and taxonomic assignment indicated, popularized by the [Blobology tool](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3843372/) can be a powerful way of visualizing microbes present in the sample. We reasoned that this approach could be just as helpful for visualizing *Hodgkinia* genomic contigs present in a cicada specimen, with color representing coding density - and present a Python and Processing scripts that were used to make Figure 3 in the manuscript.

### [ ] 4. Visualization of *Hodgkinia* gene contents table
This is a simple Processing script for reading input data tables provided by the annotation script, and outputting a PDF table that was used for Figure 4 in the manuscript.  

### [ ] 5. Visualization of *Hodgkinia* intra-genomic variability
Within even simple Hodgkinia genomes, we observed substantial amounts of variability, including alternatively mapping reads and nucleotide polymorphisms. Here, we present a workflow for the visualization of these patterns (used for Figure 5 in the manuscript).
  
  






