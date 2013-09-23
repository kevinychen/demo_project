"""
Views.
"""

from django.shortcuts import render

BASE_PAIRING = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}

CODON_PAIRING = {
    'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu', 'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser', 'TAT': 'Tyr', 'TAC': 'Tyr', 'TAA': 'STOP', 'TAG': 'STOP', 'TGT': 'Cys', 'TGC': 'Cys', 'TGA': 'STOP', 'TGG': 'Trp', 'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu', 'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met', 'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr', 'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys', 'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg', 'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val', 'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala', 'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly',
    'GGG': 'Gly',
}

def home(request):
    context = {}

    # Check whether this request includes a query string to translate.
    query_string = request.GET.get('query', None)
    if query_string:
        query_string = query_string.upper()
        new_query_string = ''.join([c for c in query_string if c in 'ACGT'])
        if query_string != new_query_string:
            context['error'] = True
        query_string = new_query_string
        reverse_complement = ''
        amino_acids = []
        for base in query_string:
            reverse_complement += BASE_PAIRING[base]
        for i in range(0, len(query_string) - 2, 3):
            amino_acid = CODON_PAIRING[query_string[i:i+3]]
            amino_acids.append(amino_acid)
            if amino_acid == 'STOP':
                break
        context['query_string'] = query_string
        context['reverse_complement'] = reverse_complement
        context['amino_acids'] = '-'.join(amino_acids)

    return render(request, 'home.html', context)
