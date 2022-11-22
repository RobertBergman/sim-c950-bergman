def search(option, search_term, env):
    """
    O(n) Time O(n) Space
    Get the packages that match the search term and return the keys
    :param option:
    :param search_term:
    :param env:
    :return:
    """
    option = int(option)
    """
    1. Package ID
    2. delivery address
    3. deliver deadline
    4. delivery city
    5. delivery zip code
    6. package weight
    7. delivery status
    """
    result_keys = []
    # O(n) Time O(n) Space
    for key in env.packages.keys:
        if option == 1:
            if str(env.packages[key].id).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)
        if option == 2:
            if str(env.packages[key].delivery_address).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)
        if option == 3:
            if str(env.packages[key].deadline).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)
        if option == 4:
            if str(env.packages[key].dest_city).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)
        if option == 5:
            if str(env.packages[key].dest_zipcode).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)
        if option == 6:
            if str(env.packages[key].weight).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)
        if option == 7:
            if str(env.packages[key].status.name).lower() == str(search_term).lower():
                result_keys.append(env.packages[key].id)

    return result_keys
