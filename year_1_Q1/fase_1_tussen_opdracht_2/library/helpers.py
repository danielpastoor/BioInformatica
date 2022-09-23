"""Helpers
"""


def list_contains_string(char_key: str, list_data: list) -> bool:
    """Function checking if list contains a string

    Args:
        char_key (str): string to be found
        list_data (list): list data

    Returns:
        bool: return bool if string found
    """

    if len(char_key) <= 0:
        print("char_key is empty")
        return False

    if len(list_data) <= 0:
        print("list_data is empty")
        return False

    for item_char in list_data:
        if char_key == item_char:
            return True

    return False


def string_chunk_to_list(string: str, chuck_by_number=1, check_string_length=True) -> list[str]:
    """ Function chuck a string by the given number to list

    Args:
        string (str): string that needs to be chucked
        chuck_by_number (int, optional): the
        count of how many chars there needs to be in a chunk. Defaults to 1.
        check_string_length (bool, optional): bool
        for checking if it is posible to have a full chunk. Defaults to True.

    Returns:
        List[str]: returns the chunked string in a list
    """

    if len(string) <= 0:
        print("string is empty")
        return []

    if check_string_length:
        if len(string) % chuck_by_number:
            print(
                "The string can not be chucked \
exactly because the total length\
is or to short or to long")

    return [string[i:i+chuck_by_number] for i in range(0, len(string), chuck_by_number)]


def search_replace_list(key: str, value: str, list_data: list) -> list[str]:
    """ Function for search replacing a string value in a list

    Args:
        key (str): string key that needs to be found
        value (str): value were the key needs to be replaced with
        list_data (list): the list where the data needs to be replaced

    Returns:
        list[str]: return list with the replaced data
    """

    if len(list_data) <= 0:
        print("list_data is empty")
        return []

    return [listValue.replace(key, value) for listValue in list_data]


def main() -> None:
    """ Useless function
    """


if __name__ == "__main__":
    main()
