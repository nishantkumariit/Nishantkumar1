
treplace(findp('0.5 to 2 % (negative sequence)'),'0.5 to 2 % (negative sequence)','0.5 to 5 % (negative sequence)')
p=findp('J.-K. Jeong, J.-H. Lee and B.-M. Han')
treplace(p,text_of(p)[text_of(p).index('J.-K.'):],'B. Bae, J. Lee, J. Jeong and B. Han, “Line-interactive single-phase dynamic voltage restorer with novel sag detection algorithm,” IEEE Trans. Power Del., vol. 25, no. 4, pp. 2702-2709, Oct. 2010.')
