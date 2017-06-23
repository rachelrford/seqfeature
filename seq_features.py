def n_neg(seq):
    """Number of negative residues a protein sequence"""

    #Convert sequence to uppercase
    seq = seq.upper()

    #Count Es and Ds, the negative residues
    return seq.count('E') + seq.count('D')
