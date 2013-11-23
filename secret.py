from collections import deque
import random

from people import PEOPLE, NUMBER_LOOKUP, NOT_ALLOWED
import sms

def generate_graph():
    
    acceptable = {}

    for santa in PEOPLE:
        acceptable[santa] = []
        for person in PEOPLE:
            if santa != person and person not in NOT_ALLOWED.get(santa,[]):
                acceptable[santa].append( person )

    return acceptable

def min_link( acceptable ):

    min_link_count = None
    min_link_santa = None

    acceptable_tuple = acceptable.items()
    random.shuffle( acceptable_tuple )

    for santa, potentials in acceptable_tuple:
        link_count = len( potentials )

        if min_link_count is None or link_count < min_link_count:
            min_link_santa = santa
            min_link_count = link_count

    return min_link_santa

def remove_santa( acceptable, santa ):
    del acceptable[santa]

def remove_person( acceptable, person ):

    for santa in acceptable:
        try:
            acceptable[santa].remove( person )
        except ValueError:
            continue

def santa_setup():
    
    acceptable = generate_graph()

    selections = []

    while len( acceptable ) != 0:
        santa = min_link( acceptable )
        person = random.choice( acceptable[santa] )
        remove_santa( acceptable, santa )
        remove_person( acceptable, person )

        selections.append( (santa, person) )

    return selections

def main():
    selections = santa_setup()

    for santa, person in selections:
        santa_number = NUMBER_LOOKUP[santa]
        santa_text = "%s, you are %s's secret santa." % (santa, person)
        sms.send_text( santa_number, santa_text )

if __name__ == '__main__':
    main()

