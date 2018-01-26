dirPath = '/home/lifeisaboutfishtacos/Desktop/build_toil/betterJobDebugging/push/toil'

0.31 sec   getDirSizeRecursively:  28639232<br>
0.31 sec   getDuRecursively:       28639232<br>
0.31 sec   naive_get_du:           28639232
0.00 sec   du:                     28954624
0.00 sec   naive_get_size:         25871030

dirPath = '/home/lifeisaboutfishtacos/Desktop/build_toil/betterJobDebugging'
18.88 sec  getDirSizeRecursively:  412602368
19.20 sec  getDuRecursively:       405217280
18.40 sec  naive_get_du:           405217280
0.07 sec   du:                     412241920
0.19 sec   naive_get_size:         232373028

dirPath = '/home/lifeisaboutfishtacos/Desktop/inputs-topmed'
0.03 sec   getDirSizeRecursively:  866496512
0.02 sec   getDuRecursively:       866496512
0.02 sec   naive_get_du:           866496512
0.00 sec   du:                     866500608
0.00 sec   naive_get_size:         866237210

dirPath = '/home/lifeisaboutfishtacos/Desktop/build_toil'
105.90 sec   getDirSizeRecursively:  2243248128
105.88 sec   getDuRecursively:       2206617600
104.53 sec   naive_get_du:           2206617600
0.47 sec     du:                     2244943872
1.05 sec     naive_get_size:         1201808537

without SUDO
dirPath = '/home/lifeisaboutfishtacos/Desktop'
157.61 sec   getDirSizeRecursively:  76810080256
147.61 sec   getDuRecursively:       76743999488
145.80 sec   naive_get_du:           76743999488
breaks b/c of permissions
1.52 sec     naive_get_size:         75365254310

with SUDO
dirPath = '/home/lifeisaboutfishtacos/Desktop'
146.90 sec   getDirSizeRecursively:  76910432256
145.60 sec   getDuRecursively:       76844351488
143.51 sec   naive_get_du:           76844351488
0.59 sec     du:                     76906373120
1.58 sec     naive_get_size:         75443958670
