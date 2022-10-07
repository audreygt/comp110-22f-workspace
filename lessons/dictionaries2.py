def zip(list_1: list[str], list_2: list[str]) -> dict[str, str]:
    new_dict: dict[str, str] = {}
    if len(list_1) == len(list_2):
        for items in range(0, len(list_1)):
            new_dict[list_1[items]] = list_2[items]
    return new_dict



