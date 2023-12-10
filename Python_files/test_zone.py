def check_all_keys(nested_dict, key_list):
    for key in key_list:
        if key not in nested_dict:
            return False
        if isinstance(nested_dict[key], dict):
            if not check_all_keys(nested_dict[key], key_list[1:]):
                return False
    return True

def get_nested_value(nested_dict, key_list):
    for key1, value1 in nested_dict.items():
        if key1 not in key_list:
            return None
        if isinstance(value1, dict):
            for value2 in value1.values():
                if isinstance(value2, dict):
                    for value3 in value2.values():
                        return value3
                else:
                    return value2
        elif key1 in nested_dict:
            for i in range(len(key_list)):
                if key_list[i] == key1:
                    return nested_dict[key_list[i]]
            return None
    return None
