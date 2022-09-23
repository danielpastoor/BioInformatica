"""
Module for nucleotides
"""


class Nucleotide:
    """
    Class representing the nucleotides
    """

    A = "A"
    C = "C"
    T = "T"
    G = "G"
    U = "U"


def calucate_nucleotide_ratio(dna: str, list_ratio_nucleotide=None) -> object:
    """Function for finding the count of the given nucleotide

    Args:
        dna (str): dna string
        listRatioNucleotide (list, optional): list of nucleotied that needs to be counted.
        Defaults to [Nucleotide.A, Nucleotide.C, Nucleotide.T, Nucleotide.G].

    Returns:
        object: Return a object with the found nucleotide and the count
    """

    if list_ratio_nucleotide is None:
        list_ratio_nucleotide = [Nucleotide.A,
                                 Nucleotide.C, Nucleotide.T, Nucleotide.G]

    return_object = {"total": 0}

    if len(dna) <= 0:
        print("DNA is empty")
        return return_object

    for list_char in list_ratio_nucleotide:
        tmp_count = dna.count(list_char)

        return_object["total"] += tmp_count
        return_object[list_char] = tmp_count

    return return_object


def main() -> None:
    """ Useless function
    """


if __name__ == "__main__":
    main()
