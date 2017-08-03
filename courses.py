COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}
def covers(topics):
    courses_list = []    

    for course in COURSES:
        if COURSES[course] & topics:   # Here the & sign finds the overlaps of the two sets.
            courses_list.append(course)
    return courses_list


def covers_all(topics):
	courses_list = []

	for keys in COURSES:
		if topics <= COURSES[keys]:
			courses_list.append(keys)
	return courses_list
print(covers_all({"conditions", "input"}))