set title "WISARD error rate chart"
set xlabel "Number of input bits in each RAM"
set ylabel "Number of training examples"
set key off
set pm3d; set palette
splot 'result/final.dat' using 3:4:6 with points palette pointsize 3 pointtype 7
set pm3d map
set size square
replot