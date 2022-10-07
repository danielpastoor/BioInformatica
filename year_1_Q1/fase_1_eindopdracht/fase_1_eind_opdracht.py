""" Function for getting the average of a value in a csv file

Raises:
    FileExistsError: Error if file doesn"t exists
    Exception: Error if file is not a csv

Returns:
    The average of the given columns in a csv file
"""

from csv import DictReader
from os import path
from sre_constants import ANY
from statistics import mean
from argparse import ArgumentError, ArgumentParser
from typing import Any


def let_user_pick_single(input_text: str, options: list[str]) -> str:
    """Let the user pick option out of multiple options

    Args:
        input_text (str): Text that needs te be shown to the user
        options (list[str]): Options list where the user can choose from

    Returns:
        str: returns the chosen value
    """

    return let_user_pick(input_text, options, False)[0]


def let_user_pick(input_text: str, options: list[str], multiple=True) -> list[str]:
    """Let the user pick multiple options out the options

    Args:
        input_text (str): Text that needs te be shown to the user
        options (list[str]): Options list where the user can choose from

    Returns:
        list[str]: returns the chosen values
    """

    input_user = ""
    # while loop for checking if the user has given any valid input
    while not input_user:
        # print input text
        print(input_text)

        add_index = 1

        # add an all option
        if multiple:
            print("1) All")
            add_index = 2
        # for loop for printing options
        for idx, element in enumerate(options):
            # print option
            print(f"{idx + add_index}) {element}")
        # set the variable with the given input of the user
        if multiple:
            input_user = input("Enter numbers sepperated by: ")
        else:
            input_user = input("Enter number: ")

        # check if the chosen options are valid
        if 0 < len(input_user):
            # change output if user can choose multiple
            if not multiple and "," in input_user:
                print("You can't choosse multiple")
                input_user = ""

            # if value is 1 then return all options
            if "1" in input_user and multiple:
                return options
            else:
                # split input by coma so we can get the value later
                chosen_numbers = [
                    int(x) for x in input_user.replace(" ", "").split(",")
                ]

                # get all options that were chosen
                return_list = [
                    options[i - add_index]
                    for i in chosen_numbers
                    if (i - add_index) < len(options)
                ]

                if len(return_list) <= 0:
                    print("Chosen numbers were out of index")
                    input_user = ""

                return return_list


def main():
    """Main function when calling this python script

    Raises:
        FileExistsError: Error if file doesn"t exists
        Exception: Error if file is not a csv
    """

    # adding argument so the arguments can be set at the command execution
    parser = ArgumentParser(
        description="Function for getting the average of a value in a csv file.")
    # argument for the file name/ location
    parser.add_argument("--file_name", type=str,
                        action="store",
                        dest="file_name",
                        help="The location of the file")
    # argument for the type that we need
    parser.add_argument("--group_column", type=str,
                        action="store",
                        dest="group_column",
                        help="group type. Must be a column with string value")
    # argument for th column where we are calculation the average
    parser.add_argument("--value_column", type=str,
                        action="store",
                        dest="value_column",
                        help="value type that must be calculated for average. Must be a column with int or float value")
    # argument for the typed values where we need to group on
    parser.add_argument("--type_values", type=str,
                        action="store",
                        dest="type_values",
                        help="values of the group type that needs to be calculated")

    args = parser.parse_args()
    # pre define variables
    file_dir = args.file_name
    group_column = args.group_column
    value_column = args.value_column
    type_values = []
    # check if there are given values and split it as you can give multiple values
    if args.type_values != None:
        type_values = str(args.type_values).lower().replace(" ", "").split(",")

    # while loop to check if the file_dir is empty so it will be filled by the user
    while not file_dir:
        # ask for file location
        file_dir = input("File name:")

        # check if the given input isn"t empty
        if not file_dir:
            print("The given output is empty please try again")

    # check if the file is a csv file
    if not file_dir.lower().endswith(".csv"):
        raise Exception("The given file is not a csv")

    # check if file exists otherwise throw error
    if not path.exists(file_dir):
        raise FileExistsError(f"The file {file_dir} doesn't exists")

    field_names = []
    csv_data = []

    # open the file and get it"s content
    with open(file_dir, "r", encoding="UTF-8") as file_data:
        # read the content of the file and convert it to csv
        csv_file = DictReader(file_data, delimiter=",")

        # defines a variable with fieldnames
        field_names = list(csv_file.fieldnames)

        # defines a variable with the csv content
        csv_data = list(csv_file)

    # list that contains all field names with value a string
    list_field_names_string_value = list(
        filter(lambda x: csv_data[0].get(x) != None and csv_data[0].get(x).replace(".", "").isdigit()
               == False, field_names))

    # list that contains all field names with value a int or float
    list_field_names_int_value = list(
        filter(lambda x: csv_data[0].get(x) != None and csv_data[0].get(x).replace(".", "")
               .isdigit(), field_names))

    # ask the user to chose a group type
    if not group_column:
        group_column = let_user_pick_single(
            "Please select one of the following key's as group type",
            list_field_names_string_value
        )
    elif group_column not in list_field_names_string_value:
        # check if the given type exists in the field list
        raise ArgumentError(
            None, "The given value for group_column does not exists in the field list that contains as value a string. Valid columns: "
            + ",".join(list_field_names_string_value))

        # ask the user to give the value column
    if not value_column:
        value_column = let_user_pick_single(
            "Please select one of the following key's as the value column for the average calculation",
            list_field_names_int_value
        )
    elif value_column not in list_field_names_int_value:
        # check if the given type exists in the field list
        raise ArgumentError(
            None, "The given value for value_column does not exists in the field list that contains as value a number. Valid columns: "
            + ",".join(list_field_names_int_value))

    grouped_values = list(set(map(lambda x: x.get(group_column), csv_data)))

    # ask the user to give the values of the group type that needs to be calculated
    if len(type_values) <= 0:
        type_values = let_user_pick(
            "Please select one of the following key's as group values",
            grouped_values
        )
    elif "all" in type_values:
        # if the given argument is all then use all types
        type_values = grouped_values
    else:
        # filter grouped values that does not exists
        not_exists_in_list = list(filter(
            lambda x: x not in grouped_values, type_values))
        print(type_values)
        # if it has values that does not exists than raise a error for it
        if len(not_exists_in_list) > 0:
            raise ArgumentError(
                None, "The given following values given for type_values does not exists in the list: " +
                ",".join(not_exists_in_list)
                + ". Please use on of the following values: "
                + ",".join(grouped_values))

        # check if there were types given
    if len(type_values) <= 0:
        print("There were no types given")
    else:
        # loop the given types values
        for type_value in type_values:
            # calculate the average from the list by the group_column
            average = mean(
                list[int](
                    map(
                        lambda x: float(x[value_column]),
                        filter(lambda y: y[group_column]
                               == type_value, csv_data),
                    )
                )
            )

            # print the average of the chosen column
            print(
                f"The average {value_column} of {type_value} is {average:.2f}")


if __name__ == "__main__":
    main()
