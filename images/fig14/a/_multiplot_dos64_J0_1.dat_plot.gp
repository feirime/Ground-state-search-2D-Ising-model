#set terminal png font "Arial,24" size 1000, 1000
#set output '_multiplot_dos64_J0_1.dat.png'
set terminal "postscript" eps font ",64" size 8, 8
set output '_multiplot_dos64_J0_1.dat.eps'
set multiplot
set size 1, 0.5
set origin 0, 0.5 
#set title "gEMgsH_dos64_J0_1.dat" textcolor lt 3
set ylabel "M_{gs} / N" #font "Arial,38"
#set ylabel "M_{gs}/N, a.u." #font "Arial,38"
set xlabel "h/J" #font "Arial,38"
plot [-0.5:5.5][:1.1] 'gEMgsH_dos64_J0_1.dat' using 1:4 with lines dt 0 lw 5 lc -1 notitle, 'gEMgsH_dos64_J0_1.dat' using 1:4 pt 7 lc -1 ps 2 notitle
#plot [-0.5:5.5][] 'gEMgsH_dos64_J0_1.dat' using 1:4 pt 7 lc 7 ps 2 notitle
set size 1, 0.5
set origin 0, 0 
#set title "HGS_dos64_J0_1.dat" textcolor lt 3
set ylabel "ln(g_{gs})" #font "Arial,38"
set xlabel "h/J" #font "Arial,38"
#set boxwidth 0 
#set ytics 1
#plot [-0.5:5.5][] 'HGS_dos64_J0_1.dat' using 1:2 with boxes lw 2 notitle, 'HGS_dos64_J0_1.dat' using 1:2 pt 7 lc 7 ps 2 notitle
plot [-0.5:5.5][] 'HGS_dos64_J0_1_dots.dat' using 1:2 with lines dt 0 lw 5 lc -1 notitle, 'HGS_dos64_J0_1.dat' using 1:2 pt 7 lc -1 ps 2 notitle
#plot [-0.5:5.5][] 'HGS_dos64_J0_1.dat' using 1:2 pt 7 lc 7 ps 2 notitle
unset multiplot
