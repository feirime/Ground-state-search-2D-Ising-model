#set terminal png font "Times New Roman,24" size 1000, 1000
set terminal "postscript" eps font ",64" size 8, 8
set output '_multiplot_dos_new2_J0.dat.eps'
set multiplot
set size 1, 0.5
set origin 0, 0.5 
#set title "gEMgsH_dos_new2_J0.dat" textcolor lt 3
set ylabel "M_{gs} / N" #font "Times New Roman,38"
#set ylabel "M_{gs}/N, a.u." #font "Times New Roman,38"
set xlabel "h/J" #font "Times New Roman,38"
set ytics 0.4
plot [-0.5:5.5][:1.1] 'gEMgsH_dos_new2_J0.dat' using 1:4 with lines lw 5 dt 0 lc -1 notitle, 'gEMgsH_dos_new2_J0.dat' using 1:4 pt 7 lc -1 ps 2 notitle
set size 1, 0.5
set origin 0, 0 
#set title "HGS_dos_new2_J0.dat" textcolor lt 3
set ylabel "ln(g_{gs})" #font "Times New Roman,38"
set xlabel "h/J" #font "Times New Roman,38"
#set boxwidth 0 
set ytics 0.4
plot [-0.5:5.5][] 'HGS_dos_new2_J0.dat' using 1:($2/10) with lines lw 5 dt 0 lc -1 notitle, 'HGS_dos_new2_J0.dat' using 1:($2/10) pt 7 lc -1 ps 2 notitle
unset multiplot
