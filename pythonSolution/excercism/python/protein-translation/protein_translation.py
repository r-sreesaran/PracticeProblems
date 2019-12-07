from textwrap import wrap


def proteins(strand):
    proteinMap = {"Methionine": "AUG", "Phenylalanine": ["UUU", "UUC"], "Leucine": ["UUA", "UUG"],
                  "Serine": ["UCU", "UCC", "UCA", "UCG"], "Tyrosine": ["UAU", "UAC"],
                  "Cysteine": ["UGC", "UGU"], "Tryptophan": "UGG", "STOP": ["UAA", "UAG", "UGA"]
                  }
    items = wrap(strand, 3)
    proteinName = []
    for el in items:
        for protein, acronym in proteinMap.items():

            if type(acronym) is str:
                if acronym == el:
                    proteinName.append(protein)

            if type(acronym) is list:
                 if el in acronym:
                      if(protein=='STOP'): return proteinName
                      proteinName.append(protein)

    return proteinName
