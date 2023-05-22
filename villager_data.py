"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    file = open(filename)
    for line in file:
        data_list = line.split("|")
        species.add(data_list[1])

    return species


filename = "villagers.csv"
print(all_species(filename))


def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    file = open(filename)
    for line in file:
        villager = line.split("|")
        species = villager[1]
        villager2 = villager[0]

        if search_string in [species]:
            villagers.append(villager2)
        elif search_string == "All":
            villagers.append(villager2)

    return sorted(villagers)


print(get_villagers_by_species(filename, "Anteater"))


def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    hobby = []

    file = open(filename)
    for line in file:
        hobby1 = line.split("|")
        hobby.append([hobby1[0], hobby1[3]])

    return hobby


print(all_names_by_hobby(filename))


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    file = open(filename)
    for line in file:
        all_data1 = line.split("|")
        all_data.append([tuple(all_data1)])

    return all_data


print(all_data(filename))


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    file = open(filename)
    for line in file:
        motto = line.split("|")
        name = motto[0]
        villagers_motto = motto[4]

        if villager_name == name:
            return villagers_motto

    return None


print(find_motto(filename, "Audie"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded_villagers = set()

    file = open(filename)
    for line in file:
        like_minds = line.split("|")
        name = like_minds[0]
        personality = like_minds[2]

        if personality == villager_name:
            likeminded_villagers.add(name)

    return likeminded_villagers


print(find_likeminded_villagers(filename, "Cranky"))
