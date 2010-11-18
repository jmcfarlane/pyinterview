import os

debug = os.environ.get('debug')
discs = int(os.environ.get('discs', 3))

def towers(disc, src, aux, dest, depth, rcall=0, moves=0):
    if debug:
        fmt = 'call: tower(%s, %s, %s, %s) rcall=#%s, depth=%s'
        print(fmt % (disc, src, aux, dest, rcall, depth))

    if disc > 0:
        # Recursive call #1
        moves += towers(disc - 1, src, dest, aux, depth + 1, 1)

        print 'Move disc', disc, 'from', src, 'to', dest,
        if debug:
            print 'rcall=#%s' % rcall
        print
        moves += 1

        # Recursive call #2
        moves += towers(disc - 1, aux, src, dest, depth + 1, 2)

    return moves

moves = towers(discs, 'Source', 'Auxillary', 'Destination', 0)

print
print 'Total moves: %s' % moves
