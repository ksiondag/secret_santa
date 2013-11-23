import unittest as ut

import secret

class TestRandom( ut.TestCase ):
    
    ITERATIONS = 10000

    @classmethod
    def setUpClass( cls ):
        pass

    def test_approximate_percentages( self ):

        possible_pairs = {}

        for santa in secret.PEOPLE:
            for person in secret.PEOPLE:
                possible_pairs[ (santa,person) ] = 0

        for i in range( TestRandom.ITERATIONS ):
            selections = secret.santa_setup()
            self.assertEquals( len( selections ), 7, "Didn't match up everyone." )

            santas, persons = zip( *selections )
            self.assertEquals( sorted(santas), sorted(persons), 
                               "Santas and persons not matched up correctly." )

            for pair in selections:
                possible_pairs[ pair ] += 1

        print 'Chance', '\t|', 'Pair'
        print '---------------------------'
        for pair, count in sorted(possible_pairs.items()):
            print (100./TestRandom.ITERATIONS)*count, '\t|', pair

if __name__ == '__main__':
    ut.main()

