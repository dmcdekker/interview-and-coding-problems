"""Functions to parse a file containing student data."""


def unique_houses(filename):
    """Return a set of student houses.

    Iterate over the cohort_data.txt file to look for all of the included house names
    and create a set called "houses" that holds those names.

    For example:

    >>> sorted(unique_houses("cohort_data.txt"))
    ["Dumbledore's Army", 'Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    """

    houses = set()

    cohort_data = open(filename)

    for line in cohort_data:
        line = line.rstrip()
        student = line.split("|")
        if len(student) >= 3:  # adding this in as a safety.
            if student[2]:
                houses.add(student[2])

    return houses


def sort_by_cohort(filename):
    """Return a list of all cohort lists, including ghosts but not instructors.

    Sort students by cohort, skipping instructors.

    Iterate over the data to create a list for each cohort. Puts ghosts into a
    separate list called "ghosts".

    For example:

    >>> sort_by_cohort("cohort_data.txt")
    [['Harry Potter', 'Mandy Brocklehurst', 'Ron Weasley', 'Oliver Wood', 'Colin Creevey', 'Cho Chang', 'Michael Corner', 'Draco Malfoy', 'Seamus Finnigan', 'Eddie Carmichael', 'Theodore Nott', 'Terence Higgs', 'Hermione Granger', 'Penelope Clearwater', 'Angelina Johnson', 'Dennis Creevey'], ['Neville Longbottom', 'Cedric Diggory', 'Pansy Parkinson', 'Anthony Goldstein', 'Padma Patil', 'Luna Lovegood', 'Eleanor Branstone', 'Lee Jordan', 'Marietta Edgecombe', 'Andrew Kirke', 'Ginny Weasley', 'Mary Macdonald', 'Blaise Zabini', 'Natalie McDonald', 'Adrian Pucey', 'Hannah Abbott', 'Graham Pritchard', 'Susan Bones', 'Roger Davies', 'Owen Cauldwell'], ['Laura Madley', 'Orla Quirke', 'Parvati Patil', 'Eloise Midgeon', 'Zacharias Smith', 'Cormac McLaggen', 'Lisa Turpin', 'Demelza Robins', 'Ernie Macmillan', 'Millicent Bullstrode', 'Percy Weasley', 'Jimmy Peakes', 'Justin Finch-Fletchley', 'Miles Bletchley', 'Malcolm Baddock'], ['Marcus Belby', 'Euan Abercrombie', 'Vincent Crabbe', 'Ritchie Coote', 'Katie Bell', 'Terry Boot', 'Lavender Brown', 'Gregory Goyle', 'Marcus Flint', 'Dean Thomas', 'Jack Sloper', 'Rose Zeller', 'Stewart Ackerley', 'Fred Weasley', 'George Weasley', 'Romilda Vane', 'Alicia Spinnet', 'Kevin Whitby'], ['Friendly Friar', 'Grey Lady', 'Nearly Headless Nick', 'Bloody Baron']]
    """

    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    cohort_data = open(filename)

    for line in cohort_data:
        line = line.rstrip()
        student = line.split("|")
        student_name = student[0] + " " + student[1]

        if student[4] == "Winter 2016":
            winter_16.append(student_name)

        elif student[4] == "Spring 2016":
            spring_16.append(student_name)

        elif student[4] == "Summer 2016":
            summer_16.append(student_name)

        elif student[4] == "Fall 2015":
            fall_15.append(student_name)

        elif student[4] == "G":
            ghosts.append(student_name)

    all_students.append(fall_15)
    all_students.append(winter_16)
    all_students.append(spring_16)
    all_students.append(summer_16)

    all_students.append(ghosts)

    return all_students


def hogwarts_by_house(filename):
    """TODO: Sort students into lists by house and return all lists in one list.

    Iterate over the data to create an alphabeticaly sorted list for each
    house, and sorts students into their appropriate houses by last name. Sorts
    ghosts into a list called "ghosts" and instructors into a list called
    "instructors". Add them, in that order, to your list of houses.

    For example:
    >>> hogwarts_by_house("cohort_data.txt")
    [['Abbott', 'Chang', 'Creevey', 'Creevey', 'Edgecombe', 'Nott', 'Spinnet'], ['Abercrombie', 'Bell', 'Brown', 'Coote', 'Finnigan', 'Granger', 'Johnson', 'Jordan', 'Kirke', 'Longbottom', 'Macdonald', 'McDonald', 'McLaggen', 'Patil', 'Peakes', 'Potter', 'Robins', 'Sloper', 'Thomas', 'Vane', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Weasley', 'Wood'], ['Bones', 'Branstone', 'Cauldwell', 'Diggory', 'Finch-Fletchley', 'Macmillan', 'Madley', 'Midgeon', 'Smith', 'Whitby', 'Zeller'], ['Ackerley', 'Belby', 'Boot', 'Brocklehurst', 'Carmichael', 'Clearwater', 'Corner', 'Davies', 'Goldstein', 'Lovegood', 'Patil', 'Quirke', 'Turpin'], ['Baddock', 'Bletchley', 'Bullstrode', 'Crabbe', 'Flint', 'Goyle', 'Higgs', 'Malfoy', 'Parkinson', 'Pritchard', 'Pucey', 'Zabini'], ['Baron', 'Friar', 'Lady', 'Nick'], ['Flitwick', 'McGonagall', 'Snape', 'Sprout']]

    """

    all_hogwarts = []
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    cohort_data = open(filename)

    for line in cohort_data:
        line = line.rstrip()
        student = line.split("|")

        first_name, last_name, house, advisor, cohort = student

        # That "list unpacking" could be written individually, too:

        # first_name = student[0]
        # last_name = student[1]
        # house = student[2]
        # advisor = student[3]
        # cohort = student[4]

        if house:

            if house == "Gryffindor":
                gryffindor.append(last_name)

            elif house == "Slytherin":
                slytherin.append(last_name)

            elif house == "Hufflepuff":
                hufflepuff.append(last_name)

            elif house == "Ravenclaw":
                ravenclaw.append(last_name)

            elif house == "Dumbledore's Army":
                dumbledores_army.append(last_name)

        elif cohort == "G":
            ghosts.append(last_name)

        else:
            instructors.append(last_name)

    all_hogwarts.append(dumbledores_army)
    all_hogwarts.append(gryffindor)
    all_hogwarts.append(hufflepuff)
    all_hogwarts.append(ravenclaw)
    all_hogwarts.append(slytherin)
    all_hogwarts.append(ghosts)
    all_hogwarts.append(instructors)

    # You could have sorted each of the lists individually before you
    # appended them: ex. gryffindor.sort() --- but a for-loop works
    # just as well!

    for house_list in all_hogwarts:
        house_list.sort()

    return all_hogwarts


def all_students_tuple_list(filename):
    """Return a list of tuples of student data.

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:

    >>> all_students_data = all_students_tuple_list("cohort_data.txt")
    >>> print(all_students_data) # doctest: +ELLIPSIS
    [('Harry Potter'...'Sprout', 'Winter 2016')]
    """

    student_list = []

    cohort_data = open(filename)

    for line in cohort_data:
        line = line.rstrip()
        student = line.split("|")
        first_name, last_name, house, advisor, cohort = student
        if house:
            student_list.append(
                (first_name + " " + last_name, house, advisor, cohort))

    return student_list


def find_cohort_by_student_name(student_list):
    """Given full name, return student's cohort.

    Use list of tuples generated by all_students_tuple_list() to make a small
    function that, given a first and last name from the command line, return
    that student's cohort, or returns "Student not found." when appropriate.

    NOTE: This function isn't included in doctests. Test it by uncommenting the
    function call at the bottom of the file.

    For example:

    Who are you looking for? Harry Potter
    'Harry Potter was in the Fall 2015 cohort.'

    Who are you looking for? Tom Riddle
    'Student not found.'

    """

    input_name = input("Who are you looking for? ")

    for student_tuple in student_list:
        student_name, house, advisor, cohort = student_tuple

        if input_name == student_name:
            print(f"{student_name} was in the {cohort} cohort.")
            return

    return "Student not found."


###############################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """Return a set of student last names that have duplicates.

    Iterate over the data to find any last names that exist across all cohorts.
    Use set operations (set math) to create and return a set of these names.

    For example:
    >>> find_name_duplicates("cohort_data.txt")
    {'Weasley'}

    """

    fall_15 = set()
    winter_16 = set()
    spring_16 = set()
    summer_16 = set()

    cohort_data = open(filename)

    for line in cohort_data:
        line = line.rstrip()
        student = line.split("|")

        first_name, last_name, house, advisor, cohort = student

        if cohort == "Fall 2015":
            fall_15.add(last_name)
        elif cohort == "Winter 2016":
            winter_16.add(last_name)
        elif cohort == "Spring 2016":
            spring_16.add(last_name)
        elif cohort == "Summer 2016":
            summer_16.add(last_name)

    duplicate_names = fall_15 & winter_16 & spring_16 & summer_16

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """Prompt user for a student. Display everyone in their house and cohort.

    Prompt the user for the name via the command line and when given a name,
    print a statement of everyone in their house in their cohort.

    Use the list of tuples generated by all_students_tuple_list() to make a
    small function that, when given a student's first and last name, prints
    students that are in both that student's cohort and that student's house.

    NOTE: This function isn't included in doctests. Test it by uncommenting the
    function call at the bottom of the file.

    For example:

    Choose a student: Hermione Granger
    Hermione Granger was in house Gryffindor in the Fall 2015 cohort.
    The following students are also in their house:
    Seamus Finnigan
    Angelina Johnson
    Harry Potter
    Ron Weasley
    Oliver Wood

    """

    input_name = input("Choose a student: ")

    for student_tuple in student_list:
        student_name, house, advisor, cohort = student_tuple

        if input_name == student_name:

            print(f"{student_name} was in house {house} in the {cohort} cohort.")
            print("The following students are also in their house:")

            for other_tuple in student_list:
                if (other_tuple[3] == cohort
                    and other_tuple[1] == house
                    and other_tuple[0] != input_name):
                    print(other_tuple[0])

            return

    print("Student not found.")


#############################################################################
# Here is some useful code to run these functions without doctests!

# find_cohort_by_student_name(all_students_data)
# find_house_members_by_student_name(all_students_data)



##############################################################################
# END OF MAIN EXERCISE.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print("ALL TESTS PASSED")
