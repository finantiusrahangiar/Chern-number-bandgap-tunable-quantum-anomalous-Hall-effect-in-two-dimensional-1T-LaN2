set encoding iso_8859_1
#set terminal  postscript enhanced color
#set output 'surfdos_l.eps'
#set terminal  pngcairo truecolor enhanced  font ", 60" size 1920, 1680
set terminal  png truecolor enhanced font ", 60" size 1920, 1680
set output 'surfdos_l.png'
set palette defined (-10 "#194eff", 0 "white", 10 "red" )
#set palette rgbformulae 33,13,10
set style data linespoints
set size 0.8, 1
set origin 0.1, 0
unset ztics
unset key
set pointsize 0.8
set pm3d
#set view equal xyz
set view map
set border lw 3
#set cbtics font ",48"
#set xtics font ",48"
set ytics 0.1 font ",48"
#set ylabel font ",48"
set ylabel "Energy (eV)"
#set xtics offset 0, -1
#set ylabel offset -6, 0 
set xrange [0:            1.54843]
set yrange [          -0.40000:           0.4]
set xtics ("G"  0.00000,"X"  0.77422,"G"  1.54843)
#set arrow from  0.77422,  -0.60000 to  0.77422,   0.59701 nohead front lw 3
set pm3d interpolate 2,2
splot 'dos.dat_l' u 1:2:($3-6) w pm3d
set terminal png truecolor enhanced font ", 30" size 1920, 1680
set output 'spindos_l.png'
set multiplot layout 3, 1
set title 'sx'
splot 'spindos.dat_l' u 1:2:3 w pm3d 
set title 'sy'
splot 'spindos.dat_l' u 1:2:4 w pm3d
set title 'sz'
splot 'spindos.dat_l' u 1:2:5 w pm3d
