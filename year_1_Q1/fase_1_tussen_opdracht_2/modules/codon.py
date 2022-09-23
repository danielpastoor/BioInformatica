"""
Class for the codon
"""


import enum

from library.helpers import list_contains_string


class CodonPositiontype(enum.Enum):
    Start = 0,
    End = 1,
    Between = 2,


class CodonType:
    """ Class that contains the codon types
    """
    codon = ""
    position = 0,
    position_type = CodonPositiontype.Between

    def __init__(self, codon="", position=0, position_type=CodonPositiontype.Between) -> None:
        if len(codon) <= 0:
            print("Codon is empty")

        self.codon = codon
        self.position = position
        self.position_type = position_type


class CodonsRules:
    """
    Class representing the rules about codons
    """
    StartCodons = ["AUG"]
    EndCodons = ["UAA", "UGA", "UAG"]
    CodonCountChar = 3


def get_condon_formatted(codons: list, start_codons=None, end_codons=None) -> list[CodonType]:
    """Function for getting the start and end codons

    Args:
        codons (list): codon list.
        start_codons (_type_, optional): start codons list. Defaults to CodonsRules.StartCodons.
        end_codons (_type_, optional): end codons list. Defaults to CodonsRules.EndCodons.

    Returns:
        list[CodonType]: _description_
    """

    return_list = []

    if len(codons) <= 0:
        print("Codons list is empty")
        return return_list

    if start_codons is None:
        start_codons = CodonsRules.StartCodons

    if end_codons is None:
        end_codons = CodonsRules.EndCodons

    for i, codon in enumerate(codons):
        tmp_codon = CodonType(codon, i)

        if list_contains_string(codon, start_codons):
            print(f"The {codon} is a start codon")
            tmp_codon.position_type = CodonPositiontype.Start
        elif list_contains_string(codon, end_codons):
            print(f"The {codon} is a end codon")
            tmp_codon.position_type = CodonPositiontype.End

        return_list.append(tmp_codon)

    return return_list


def main() -> None:
    """ Useless function
    """


if __name__ == "__main__":
    main()
