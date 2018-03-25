set term png
set output "{output}"

plot "gly_rmsd_bb.dat" lt rgb "#ffdddd", \
     "dummy.txt" using ({x}):({y}) lt rgb "red"
