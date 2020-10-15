#dump file sizes, names, and PFPackedCandidates size (compressed/uncompressed)

for f in *.root; 
  do a=$(basename $PWD) && b=($(edmFileUtil file:${f})); echo ${b[4]}" "${b[6]}" "${b[8]}" "${a: -2}" "${f::-5}" "$(edmEventSize -d ${f} --verbose | grep packedPF) >> sizes & 
done > sizes &

