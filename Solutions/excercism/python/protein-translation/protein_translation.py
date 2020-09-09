from textwrap import wrap


def proteins(strand):
    proteinMap = {'AUG': 'Methionine', 'UCU': 'Serine', 'UCC': 'Serine',
             'UCA': 'Serine', 'UCG': 'Serine', 'UUA': 'Leucine', 'UUG': 'Leucine',
             'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine',
             'UAU': 'Tyrosine', 'UAC': 'Tyrosine',
             'UGU': 'Cysteine', 'UGC': 'Cysteine',
             'UGG': 'Tryptophan',
             'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}

    condons = wrap(strand, 3)
    proteinName = []
    for condon in condons:
        if condon in proteinMap.keys():
             if proteinMap.get(condon) == 'STOP': return proteinName
             proteinName.append(proteinMap.get(condon))

    return proteinName
