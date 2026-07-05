class School:
    def __init__(self):
        self._grades = {}
        self._added = []

    def add_student(self, name, grade):
        # Student already exists
        for students in self._grades.values():
            if name in students:
                self._added.append(False)
                return

        self._grades.setdefault(grade, []).append(name)
        self._grades[grade].sort()
        self._added.append(True)

    def roster(self):
        result = []
        for grade in sorted(self._grades):
            result.extend(self._grades[grade])
        return result

    def grade(self, grade_number):
        return list(self._grades.get(grade_number, []))

    def added(self):
        return self._added