def towers(disc, src, aux, dest):
    if disc > 0:
        towers(disc -1, src, dest, aux)
        print 'Move disc', disc, 'from', src, 'to', dest
        towers(disc -1, aux, src, dest)

towers(3, 'Source', 'Auxillary', 'Destination')
