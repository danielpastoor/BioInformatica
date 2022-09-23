def show_molecule_structure(var_molecule):
    """
    Show the given molecule structure

    :param string of the molecule
    :return nothing
    """

    def count_and_calculate(molecule, key, electrons):
        """
        Counting atoms in string

        :param string of the molecule 
        :param key that needs to be found
        :param elektrons
        :return count of the found key
        """
        molecule = molecule.upper()
        var_tmp_elektrons_count = molecule.count(key) * electrons
        return var_tmp_elektrons_count

    def count_and_print_elektrons(molecule, key, electrons):
        """
        Function for counting atoms in string and print the value

        :param string of the molecule 
        :param key that needs to be found
        :param elektrons
        :return count of the found key
        """
        var_tmp_elektrons_count = count_and_calculate(molecule, key, electrons)
        print(f"Het {key} atoom levert {var_tmp_elektrons_count} elektronen")
        return var_tmp_elektrons_count

    var_o = 2
    var_c = 4
    var_h = 1
    var_s = 2
    var_n = 3

    print(var_molecule)

    var_totaal_elektrons = 0

    var_totaal_elektrons += count_and_print_elektrons(var_molecule, "H", var_h)
    var_totaal_elektrons += count_and_print_elektrons(var_molecule, "C", var_c)
    var_totaal_elektrons += count_and_print_elektrons(var_molecule, "S", var_s)
    var_totaal_elektrons += count_and_print_elektrons(var_molecule, "N", var_n)
    var_totaal_elektrons += count_and_print_elektrons(var_molecule, "O", var_o)

    var_covalente_bindingen = 2

    var_covalente_count = 0
    var_covalente_count += count_and_calculate(
        var_molecule, "|", (1 * var_covalente_bindingen))
    var_covalente_count += count_and_calculate(
        var_molecule, "-", (1 * var_covalente_bindingen))
    var_covalente_count += count_and_calculate(
        var_molecule, "=", (2 * var_covalente_bindingen))
    var_covalente_count += count_and_calculate(
        var_molecule, "≡", (3 * var_covalente_bindingen))
    var_covalente_count += count_and_calculate(
        var_molecule, "‖", (2 * var_covalente_bindingen))
    var_covalente_count += count_and_calculate(
        var_molecule, "⦀", (3 * var_covalente_bindingen))

    print("Total covalente bindingen count ", var_covalente_count)

    print("Total elektrons ", var_totaal_elektrons)

    print("Structure is equal: ", (var_covalente_count == var_totaal_elektrons))


var_molecule = """
            H               H   O - H
            |               |   |
    O = C - C = C - C ≡ C - C - C - H
        |       |           |   |
    H - O   H - C - H       H   N - H
                |               |
                H               H
    """
show_molecule_structure(var_molecule)

var_second_molecule = """
                                                        H               H   O - H
                                                        |               |   |
                                                O = C - C = C - C ≡ C - C - C - H
                                                    |       |           |   |
                                                H - O   H - C - H       H   N - H
                                                            |               |
                                                            H               H
    """
show_molecule_structure(var_second_molecule)
