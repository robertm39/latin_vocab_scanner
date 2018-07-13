# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:45:55 2018

@author: rober
"""

import latin_vocab_scanner as lvs
def dict_test():
    dicts = lvs.get_possible_entries('os')
    print(dicts)

def clean_test():
    dirty = 'Āā sic aqua. Ǣ: ǣĒ, \"\" ē'
    print(lvs.clean_text(dirty))

def poss_test():
    text = 'Et hi quidem terra militiae duces sive capitanei. Mari, navium praefecti isti: Martinus Frobicher viceadmirallius, vir rei maritimae peritissimus, qui ante aliquot aliis expeditionibus etiam toti classi praefuerat; Franciscus Knollis, Thomas Frenar, Gulielmus Cicel, Iacobus Carleil, Henricus Whyte, Thomas Drake, Thomas Seely, capitaneus Rivers, capitaneus Martinus, capitaneus Baylie, capitaneus Crosse, capitaneus Fortescus, capitaneus Carlese, capitaneus Hauukins, capitaneus Erizo, capitaneus Moone, capitaneus Vaghan, capitaneus Varney, capitaneus Gilman, nobilesque alii multi, quorum nomina hic non recensentur.'
    possibilities = lvs.get_all_entry_possibilities(text)
    for poss in possibilities:
        for p in poss:
            print(p)
        print('')

def get_text(file, encoding='utf8'):
    return ''.join(list(open(file, encoding=encoding)))

def all_test(text, verbose=True):
#    text = ''.join(list(open('in_cat_iv.txt')))
#    text = get_text('in_cat_i.txt')
#    text = get_text('aeneid_1.txt')
#    text = get_text('bell_gall_1.txt')
    print('LEN: ' + str(len(text)))
    possibilities = lvs.get_all_entry_possibilities(text, verbose=verbose)
    all_p = lvs.all_possible_entries(possibilities)
    for entry in all_p:
        print(entry)
    print('')
    print(str(len(all_p)) + ' words')

#dict_test()
#clean_test()
#poss_test()
#all_test(True)

def scan(name):
    print('***********************')
    print('')
    print('SCANNING ' + name)
    print('')
    print('***********************')
    all_test(get_text(name))

going = True

while going:
    print('********** STARTING **********')
    try:
        scan('in_cat_i.txt')
        scan('in_cat_ii.txt')
        scan('in_cat_iii.txt')
        scan('in_cat_iv.txt')
        for i in range(1, 13):
            scan('aeneid_' + str(i) + '.txt')
        for i in range(1, 5):
            scan('georgic_' + str(i) + '.txt')
        for i in range(1, 9):
            scan('bell_gall_' + str(i) + '.txt')
        for i in range(1, 4):
            scan('bello_civili_' + str(i) + '.txt')
        going = False
    except Exception:
        pass