def read_preferences(file_path):
    with open(file_path, 'r') as f:
        num_employees, num_beers = map(int, f.readline().split())
        preferences = f.readline()
    return num_employees, num_beers, preferences


def min_beers(num_employees, num_beers, preferences):
    if not 0 < num_employees < 50:
        return -1

    if not 0 < num_beers < 50:
        return -1

    if not len(preferences) == num_employees * num_beers + (num_employees - 1):
        return -1

    converted_line = convert_line(preferences, num_beers)
    adjacency_list_of_preferences = transform_preferences(converted_line)
    result = calculate_min_preferences(num_employees, adjacency_list_of_preferences)

    return result


def convert_line(line, num_beers):
    array = []
    current_row = []

    for char in line:
        if char == 'Y':
            current_row.append(1)
        elif char == 'N':
            current_row.append(0)
        else:
            continue

        if len(current_row) == num_beers:
            array.append(current_row)
            current_row = []

    return array


def transform_preferences(preferences):
    preferences_list = [[] for _ in range(len(preferences[0]))]
    for employee_idx, preference in enumerate(preferences):
        for beer_idx, likes_beer in enumerate(preference):
            if likes_beer:
                preferences_list[beer_idx].append(employee_idx + 1)

    return preferences_list


def calculate_min_preferences(num_employees, adjacency_list):
    preferences_set = set(range(1, len(adjacency_list) + 1))
    satisfied_employees = [0] * num_employees

    for preference, employees in enumerate(adjacency_list, start=1):
        for employee in employees:
            satisfied_employees[employee - 1] += 1

    for preference, employees in enumerate(adjacency_list, start=1):
        if all(satisfied_employees[employee - 1] > 1 for employee in employees):
            preferences_set.discard(preference)
            for employee in employees:
                satisfied_employees[employee - 1] -= 1

    return len(preferences_set)
