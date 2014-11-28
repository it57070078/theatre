'''Test create theatre seat data'''
def write_file():
    '''create new data'''
    f = open('seat_data.txt', 'w')
    for i in xrange(10):
        f.write(str(i)+'\n')
    f.close()
def read_file():
    '''read exiting file'''
    f = open('seat_data.txt', 'r')
    print f.read()
def test_with_statement():
    '''test with'''
    with open('seat_data.txt') as f:
        for line in f:
            print repr(line)
    print type(repr(line))
test_with_statement()
