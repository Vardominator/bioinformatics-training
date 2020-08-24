# Introduction
* Half a million patients contract *staphylococcus (staph)* infection after surgery. Some contract drug-resistant strains such as *methicillin-resistant _staphylococcus aureus (MRSA)_*.
* By analyzing the genome of over 40 different types of staph bacteria, we must determine which species is causing the staph infection. 
* This can be done by analyzing mutations that have led to antibiotics resistance.

# Assembly
* Assuming we have isolated bacteria in the patient and generated reads for these bacteria, we can assemble the genome from the reads using the *SPAdes* assembler through the *Galaxy* service.

# Definitions
* Contig: a continguous segment of the genome that has been reconstructed by an assembly algorithm
* Scaffold: ordered sequence of contigs (possibly with gaps between them) that are reconstructed by an assembly algorithm.
  - Existing algorithms specify the approximate lengths of gaps between contigs in a scaffold
* N50 statistic: used to measure quality of an assembly
  - maximal contig length for which all contigs greater than or equal to that length comprise at least half of the sum of the lengths of all the contigs
* NGA50 statistic: modified version of NG50, accounting for assembly errors (misassemblies).
  - errors in the contigs are accounted for by comparing contigs to a reference genome
  - misassembled contigs are broken at misassembly breakpoints