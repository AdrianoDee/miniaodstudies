#dump file sizes, names, and PFPackedCandidates size (compressed/uncompressed)

for f in *.root; 
  do a=$(basename $PWD) 
  printf ${a: -2}" "   
  printf $(ls -s ${f})"  " 
  printf " ${f::-5} "
  echo $(edmEventSize -d ${f} --verbose | grep packedPF) 
done > sizes &

