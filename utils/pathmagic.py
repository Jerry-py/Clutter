from typing import Union, List, Any


def set(main_dict: dict, path: Union[str, List[str]], *, dump: dict) -> dict:
    """Sets the key value pair in the path given. Will override.
    Args:
        main_dict (dict): The dict to modify.
        path (Union[str, List[str]]): The path to follow.
        dump (dict): The key value pairs to set in the last scope.
    Returns:
        dict: The modified dict.
    """

    def magic(alt_dict: dict, key: str) -> dict:
        """Validates the key(dict) in the alt_dict.
        Args:
            alt_dict (dict): The dict to modify.
            key (str): The key to validate(dict).
        Returns:
            dict: The modified dict.
        """
        if key in alt_dict.keys() and isinstance(alt_dict[key], dict):
            return alt_dict

        alt_dict[key] = {}
        return alt_dict

    main_dict_ref, i = main_dict, 0

    if isinstance(path, str):
        path = path.split(".")

    if path == []:
        return dump

    for dict_name in path:
        i += 1
        main_dict = magic(main_dict, dict_name)[dict_name]

        if i == len(path):
            main_dict.update(dump)

    return main_dict_ref


def get(main_dict: dict, path: Union[str, List[str]], *, key: str, default=None) -> Any:
    """Gets the value for the key in the path given. Will return the default kwarg if the key can't be found.
    Args:
        main_dict (dict): The dict to get the value of the key in.
        path (Union[str, List[str]]): The path to follow.
        key (str): The key to get the value of.
        default (Any, optional): The value to return if the key is not found. Defaults to None.
    Returns:
        Any: The value of the key. Will return the default kwarg if the key is not found.
    """
    if isinstance(path, str):
        path = path.split(".")

    for dict_name in path:
        try:
            main_dict = main_dict[dict_name]

        except (KeyError, TypeError, AttributeError):
            return default

    return main_dict.get(key, default)
