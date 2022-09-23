# region validating

from library.helpers import list_contains_string, search_replace_list, string_chunk_to_list
from modules.dna import generate_dna_sequence
from modules.nucleotide import Nucleotide, calucate_nucleotide_ratio
from modules.codon import CodonPositiontype, CodonsRules, get_condon_formatted


def validate_dna(dna: str, list_validate_nucleotide=None) -> bool:
    """Function for validating a dna string

    Args:
        dna (str): dna string
        list_validate_nucleotide (list, optional): list
        of nucleotides that needs to be checked.
        Defaults to [Nucleotide.A, Nucleotide.C, Nucleotide.T, Nucleotide.G].

    Returns:
        boolean: returns boolean
    """

    if list_validate_nucleotide is None:
        list_validate_nucleotide = [Nucleotide.A,
                                    Nucleotide.C, Nucleotide.T, Nucleotide.G]

    if len(dna) <= 0:
        print("DNA is empty")
        return False

    for dna_char in dna:
        if not list_contains_string(dna_char, list_validate_nucleotide):
            print(f"There was is invalid char: {dna_char}")
            return False

    return True
# endregion


def main():
    list_checking_ratio_nucleotide = [Nucleotide.G, Nucleotide.C]

    print("""
    -----------------------------
    Generated DNA
    -----------------------------""")
    dna_sequence = generate_dna_sequence(750) # "atgcagtcccagttctaggctctctgagagagtctcgagatc"
    print(dna_sequence)

    print("""
    -----------------------------
    Validating DNA
    -----------------------------""")

    result = validate_dna(dna_sequence)

    if not result:
        print("The given DNA sequence is not valid")
    else:
        print("The given DNA sequence is valid")

        print("""
    -----------------------------
    Calculation ration percentage
    -----------------------------""")

        result_ratio = calucate_nucleotide_ratio(
            dna_sequence, list_checking_ratio_nucleotide)

        for ratio_key in result_ratio:
            print(f"The ratio percentage for \
{ratio_key} is \
{round((result_ratio[ratio_key] / len(dna_sequence)) * 100, 2)} %")

        print("""
    -----------------------------
    Chuncking DNA to get the codons
    -----------------------------""")
        codons = string_chunk_to_list(
            dna_sequence, CodonsRules.CodonCountChar, False)
        print("Found codons:")
        print(codons)

        print("""
    -----------------------------
    DNA codons to RNA codons
    -----------------------------""")
        # Transform T to U so that it is RNA
        codons = search_replace_list(Nucleotide.T, Nucleotide.U, codons)

        print("RNA codons:")
        print(codons)
        print("""
    -----------------------------
    Check if codon is start or stop and get position
    -----------------------------""")
        codons_formatted = get_condon_formatted(codons)

        print("""
    -----------------------------
    Codon start and end with position
    -----------------------------""")        
        for codon_formatted in codons_formatted:
            if codon_formatted.position_type == CodonPositiontype.Start:
                print(f"The codon {codon_formatted.codon} is a \
Start codon with the position {codon_formatted.position}")
            elif codon_formatted.position_type == CodonPositiontype.End:
                print(f"The codon {codon_formatted.codon} is a \
End codon with the position {codon_formatted.position}")


if __name__ == "__main__":
    main()
