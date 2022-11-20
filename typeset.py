# coding: utf-8

import re


bib_fname_l = [
    'Project-IDDvSD.bib', 'Project-IDDvSD-ap.bib'
    ]

bib2re_d = {
    'Project-IDDvSD-ap.bib': r'\1_a,',
}

remove_url = re.compile('url = {.*?}', re.I|re.M)

remove_rssn = re.compile('issn = {.*?}', re.I|re.M)
remove_rsbn = re.compile('isbn = {.*?}', re.I|re.M)
remove_doi = re.compile('doi = {.*?}', re.I|re.M)
remove_note = re.compile('note = {.*?}', re.I|re.M)
remove_address = re.compile('address = {.*?}', re.I|re.M)
remove_publisher = re.compile('publisher = {.*?}', re.I|re.M)
remove_series = re.compile('series = {.*},\n', re.I|re.M)

sep_bib = re.compile("@(.*?)\{.*?\n(?=@)", re.S)
bib_type = re.compile("@(.*?){")

add_suffix = re.compile('(@.*?{.*?),', re.I)

for bib_fname in bib_fname_l:

    with open(f"./{bib_fname}", 'r', encoding='utf-8') as f:
        big_str_1 = f.read()

    big_str_1 = remove_url.sub('url = {}', big_str_1)

    big_str_1 = remove_rssn.sub('issn = {}', big_str_1)
    big_str_1 = remove_rsbn.sub('isbn = {}', big_str_1)
    big_str_1 = remove_doi.sub('doi = {}', big_str_1)
    big_str_1 = remove_note.sub('note = {}', big_str_1)
    big_str_1 = remove_address.sub('address = {}', big_str_1)
    
    big_str_1 = remove_series.sub('series = {},\n', big_str_1)
    
    
    # big_str_1 = remove_publisher.sub('publisher = {}', big_str_1)

    # don't remove publisher when the bib entry is book
    bib_l = []
    for one_bib in sep_bib.finditer(big_str_1):
        bib_text = one_bib.group(0)
        if one_bib.group(1) != 'book':
            bib_text = remove_publisher.sub('publisher = {}', bib_text)
        bib_l.append(bib_text)
    
    # deal with last bib entry
    bib_text = big_str_1[one_bib.span()[1]:]
    if bib_type.match(bib_text).group(1) != 'book':
        bib_text = remove_publisher.sub('publisher = {}', bib_text)
    bib_l.append(bib_text)
    
    
    big_str_1 = ''.join(bib_l)
    
    if bib_fname == 'Project-IDDvSD-ap.bib':
        big_str_1 = add_suffix.sub(bib2re_d[bib_fname], big_str_1)
    with open(bib_fname, 'w', encoding='utf-8') as f:
        f.write(big_str_1)

