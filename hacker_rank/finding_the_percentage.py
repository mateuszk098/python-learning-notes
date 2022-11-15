"""
See description at https://www.hackerrank.com/challenges/finding-the-percentage

The provided code stub will read in a dictionary containing key/value pairs 
of name:[marks] for a list of students. Print the average of the marks array 
for the student name provided, showing 2 places after the decimal.
"""

if __name__ == "__main__":

    n: int = int(input())
    student_marks: dict = {}

    for _ in range(n):
        name, *line = input().split()
        scores: list = list(map(float, line))
        student_marks[name] = scores

    query_name: str = input()
    my_list: list = student_marks.get(query_name, None)

    if my_list is not None:
        print(f"{sum(my_list)/len(my_list):.2f}")
    else:
        print(f"There is no student {query_name}.")
