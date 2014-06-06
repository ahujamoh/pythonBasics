import os
import glob

cwdir = os.getcwd()

print cwdir
file_pat = "%s/*.py" %(cwdir)

fl = glob.glob(file_pat)


def iterable_example():
    print "\n\niterable_example"
    for x  in fl:
        print "\t%s" %x 


def yield_example():
    print "\n\nyield_example"
    for x  in fl:
        print "yield x"
        yield x


def yield_test():
    print "\n\nyield_test"
    lis  = yield_example()
    #for x in yield_example():
    for x in lis:
        print lis.next()
        print "\t%s " %x 



iterable_example()
yield_test()
