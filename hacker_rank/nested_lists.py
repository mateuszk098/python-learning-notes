if __name__ == '__main__':

    records: list = []

    for _ in range(int(input())):
        name: str = input()
        score: float = float(input())
        records.append([name, score])

    # Using set we have only sub-list with unique values, ignorig names
    sorted_unique_grades: list = sorted(set(grade for _, grade in records))
    second_lowest_score: float = sorted_unique_grades[1]
    # Check if grade is equal the second lowest value and append name to list if yes
    results: list = [name for name, grade in records if grade == second_lowest_score]
    results.sort()
    print(*results, sep='\n')
