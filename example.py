import schematax as sx

xs = ['110','100','010']

ss = sx.complete(xs)

print "the schematic completion of xs is:"
print ss


sx.draw(ss,'test') #drawing the schematic lattice in the file "test.pdf"
