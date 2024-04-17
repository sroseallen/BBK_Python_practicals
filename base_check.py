def get_dna_base_code(name):
    """Return one-letter DNA base code given its name"""
    if name.lower() == 'adenine':
        return 'A'
    if name.lower() == 'guanine':
        return 'G'
    if name.lower() == 'cytosine':
        return 'C'
    if name.lower() == 'thymine':
        return 'T'
    else:
        return None

def get_rna_base_code(name):
    """Return one-letter RNA base code given its name"""
    if name.lower() == 'adenine':
        return 'A'
    if name.lower() == 'guanine':
        return 'G'
    if name.lower() == 'cytosine':
        return 'C'
    if name.lower() == 'uracil':
        return 'U'
    else:
        return None

def get_dna_base_name(letter):
    """Return DNA base name given its one-letter code"""
    if letter.lower() == 'a':
        return 'adenine'
    if letter.lower() == 'g':
        return 'guanine'
    if letter.lower() == 'c':
        return 'cytosine'
    if letter.lower() == 't':
        return 'thymine'
    else:
        return None
    
def get_rna_base_name(letter):
    """Return RNA base name given its one-letter code"""
    if letter.lower() == 'a':
        return 'adenine'
    if letter.lower() == 'g':
        return 'guanine'
    if letter.lower() == 'c':
        return 'cytosine'
    if letter.lower() == 'u':
        return 'uracil'
    else:
        return None
    
def is_subseq(s, seq):
    """Return True if s is a sub-sequence of seq, otherwise False."""
    seq = seq.lower()
    if s.lower() in seq:
        return True
    return False