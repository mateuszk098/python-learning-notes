"""
Example implementation of database structure.
"""


class Person:
    """Simple class representing a person."""

    def __init__(self, name, salary, next=None):
        self.name = name
        self.salary = salary
        self.next = next


class PersonList:
    """Linked List representing list of people."""

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_last(self, name, salary):
        """Add a person at the end of the list."""
        new_person = Person(name, salary)
        if self.head is None:
            self.head = new_person
            self.tail = new_person
        else:
            self.tail.next = new_person  # type: ignore
            self.tail = new_person
        self.length += 1
        return new_person  # IMPORTANT (SEE add_and_sort() in DataBase).

    def print_out(self):
        """Print out the list of people."""
        current = self.head
        while current is not None:
            print(f"NAME: {current.name}\t SALARY: {current.salary}")
            current = current.next

    def remove_person(self, name):
        """Removes a person with given name."""
        prev, current, found = self._search_ref(name)
        if not found:
            return
        self.length -= 1

        if self.length == 0:  # There was only one element.
            self.head = None
            self.tail = None
            return
        if self.head == current:  # Remove from the beginning.
            self.head = current.next
            return
        if self.tail == current:  # Remove from the end.
            self.tail = prev
            prev.next = None
            return
        prev.next = current.next  # Remove from somewhere in the middle.

    def _search_ref(self, name):
        """Return previous and current reference of the given person."""
        prev = None
        current = self.head
        while current is not None:
            if current.name == name:
                return prev, current, True  # Person was found.
            prev = current
            current = current.next
        return prev, current, False  # Person was not found.


class NameIndex:
    """Auxiliary class. Realises sorting by person name.
    Contains pointer to Person instance."""

    def __init__(self):
        self.person = None
        self.next = None  # Next element of this list.

    def print_out(self):
        element = self
        while element is not None:
            print(f"NAME: {element.person.name}\t SALARY: {element.person.salary}")  # type: ignore
            element = element.next


class SalaryIndex:
    """Auxiliary class. Realises sorting by person salary.
    Contains pointer to Person instance."""

    def __init__(self):
        self.person = None
        self.next = None  # Next element of this list.

    def print_out(self):
        element = self
        while element is not None:
            print(f"NAME: {element.person.name}\t SALARY: {element.person.salary}")  # type: ignore
            element = element.next


class DataBase:
    """Main class representing the database."""

    def __init__(self):
        self.data = PersonList()
        self.name_head = None
        self.name_tail = None
        self.salary_head = None
        self.salary_tail = None

    def add_and_sort(self, name, salary):
        person = self.data.add_last(name, salary)
        self._add_and_sort_by_name(person)
        self._add_and_sort_by_salary(person)

    def remove_person(self, name):
        """Removes person its indices from Database."""
        self.data.remove_person(name)

        # Remove from NameIndex.
        prev_id, current_id = self._search_name_ref(name)
        if self.name_head == current_id:  # Remove from the beginning.
            self.name_head = current_id.next
        elif self.name_tail == current_id:  # Remove from the end.
            self.name_tail = prev_id
            prev_id.next = None
        else:
            prev_id.next = current_id.next  # Remove from somewhere in the middle.

        # Remove from SalaryIndex.
        salary = current_id.person.salary
        prev_id, current_id = self._search_salary_ref(salary)
        if self.salary_head == current_id:  # Remove from the beginning.
            self.salary_head = current_id.next
        elif self.salary_tail == current_id:  # Remove from the end.
            self.salary_tail = prev_id
            prev_id.next = None
        else:
            prev_id.next = current_id.next  # Remove from somewhere in the middle.

    def print_out_by_name(self):
        if self.name_head is not None:
            self.name_head.print_out()
        else:
            print("Empty index.")

    def print_out_by_salary(self):
        if self.salary_head is not None:
            self.salary_head.print_out()
        else:
            print("Empty index.")

    def print_out(self):
        if self.data is not None:
            self.data.print_out()
        else:
            print("Database is empty.")

    def _search_name_ref(self, name):
        """Returns pointer to previous and current name field in NameIndex."""
        prev = None
        current = self.name_head
        while current is not None:
            if current.person.name == name:  # type: ignore
                return prev, current  # Name was found.
            prev = current
            current = current.next
        return prev, current  # Name was not found.

    def _search_salary_ref(self, salary):
        """Returns pointer to previous and current salary field in SalaryIndex."""
        prev = None
        current = self.salary_head
        while current is not None:
            if current.person.salary == salary:  # type: ignore
                return prev, current  # Salary was found.
            prev = current
            current = current.next
        return prev, current  # Salary was not found.

    def _add_and_sort_by_name(self, person):
        """Adds with sorting a new index to NameIndex."""
        name = person.name
        new_index = NameIndex()
        new_index.person = person

        if self.name_head is None:  # Emtpy index list.
            self.name_head = new_index
            self.name_tail = new_index
            return

        prev = None
        current = self.name_head
        while current is not None:  # Find appropriate place.
            if current.person.name >= name:  # type: ignore
                break
            else:
                prev = current
                current = current.next

        if prev is None:  # Add index at the beginning.
            self.name_head = new_index
            new_index.next = current  # type: ignore
        else:
            if current is None:  # Add index at the end.
                prev.next = new_index  # type: ignore
                self.name_tail = new_index
            else:  # Add index somewhere in the middle.
                prev.next = new_index  # type: ignore
                new_index.next = current  # type: ignore

    def _add_and_sort_by_salary(self, person):
        """Adds with sorting a new index to SalaryIndex."""
        salary = person.salary
        new_index = SalaryIndex()
        new_index.person = person

        if self.salary_head is None:  # Emtpy index list.
            self.salary_head = new_index
            self.salary_tail = new_index
            return

        prev = None
        current = self.salary_head
        while current is not None:  # Find appropriate place.
            if current.person.salary >= salary:  # type: ignore
                break
            else:
                prev = current
                current = current.next

        if prev is None:  # Add index at the beginning.
            self.salary_head = new_index
            new_index.next = current  # type: ignore
        else:
            if current is None:  # Add index at the end.
                prev.next = new_index  # type: ignore
                self.salary_tail = new_index
            else:  # Add index somewhere in the middle.
                prev.next = new_index  # type: ignore
                new_index.next = current  # type: ignore
