def does_name_exist(first_names, last_names, full_name):
    name_set = {f"{first} {last}" for first in first_names for last in last_names}

    return full_name in name_set