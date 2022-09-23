import random

from modules.nucleotide import Nucleotide


def generate_dna_sequence(length=100) -> str:
    """Function for generating string

    Args:
        length (int, optional): length of the dna. Defaults to 100.

    Returns:
        str: return the random generated dna
    """

    return (''.join(random.choice([
        Nucleotide.A,
        Nucleotide.C,
        Nucleotide.T,
        Nucleotide.G
    ]) for _ in range(length))).upper()


def main() -> None:
    """ Useless function
    """


if __name__ == "__main__":
    main()
