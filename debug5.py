__author__ = ''
__class__ = ''
__crn__ = ''

# a. Go over the design in pseudocode.  Give a quick description of what this program does.

# b. Give at least five examples with explicit user input(s) and expected outputs from this program base on the design.
#    An example:  user type 1 at main men: Please make a selection (a, i, s, m, or q)  -> 1
#                 program outputs: Invalid selection - '1'

# c. There seem to be bugs preventing the program to produce the correct result as expected.  What are the errors?
#    List them below:

# d. After fixing all the bugs, does the program run correctly and produce the correct result.

''' // design

P1.  show program introduction
  show user "+------------------------------------+"
  show user "|**** Student Recodes for CIS122 ****|"
  show user "+------------------------------------+"
  show user ""
  
P2.  show main menu
  show user ""
  show user " a) add a student into our student records."
  show user " i) insert an exam score to a student's record."
  show user " s) show class stats."
  show user " m) show this menu."
  show user ""
  show user " q) exit program."
  show user ""
  
P31.  add the student to the records
1.  ask user for the student name
2.  While the student name is not valid
  a.  show user an error message
  b.  ask user for the student name
3.  show user the student name entered and ask if that is correct
4.  if yes then add the student name entered to the student record
    else show user the student name entered is not add to the student record
  
P3.  adding a student to records
1.  ask user for a student's ID
2.  while the student's ID are not all digits
  a.  show user an error message
  b.  ask user for a student's ID
3.  if the student's ID already exist in the records show user an error message that student ID is already in the
       records
    else add the student to the records
    
P4.  adding an exam score to a student record
1.  ask user for a exam score
2.  while exam score not in correct range
  a.  show user an error message
  b.  ask user for a exam score
3.  add exam score to a student's record

P5.  show all students' records and stats
1.  loop through all students records by student ID's
  a.  construct a block of text with following items:  
      1.  student ID
      2.  student name
      3.  show all exams
      4.  total exam score
      5.  highest exam score
      6.  lowest exam score
      7.  average exam score
  b.  show user the line of text
2.  show user ""
      
main program
1.  show program introduction
2.  show main menu
3.  do following until user select to quit our program 
  a.  ask user to make a selection from main menu
      if user select main menu then show main menu
      else if user select add a student then perform adding a student to records
      else if user select add an exam score to a student record then perform adding an exam score to a student's record
      else if user select show stats then show all students' records and stats
      else user selection can not be performed and an error message is shown  
4.  tell user thanks using our program

run program by calling main program
'''

ALLOCATION_SIZE = 5
MAX_SCORE_SIZE = 5


def show_program_introduction():
    print("+------------------------------------+")
    print("|**** Student Recodes for CIS122 ****|")
    print("+------------------------------------+")


def show_main_menu():
    print("")
    print(" a) add a student into our student records.")
    print(" i) insert an exam score to a student's record.")
    print(" s) show class stats.")
    print(" m) show this menu.")
    print("")
    print(" q) exit program.")
    print("")


def get_user_input(prompt):
    user_input = input(prompt)
    return user_input


def get_user_menu_selection():
    menu_prompt = "Please make a selection (a, i, s, m, or q)  -> "
    selection = get_user_input(menu_prompt).lower()
    return selection


def get_student_id():
    student_id_prompt = "Please enter student ID (digits - no letter): "
    return get_user_input(student_id_prompt)


def find_id_in_records(sid, ids, size):
    i = 0
    found = False
    while (not found) and (i < size):
        if sid == ids[i]:
            found = True
        else:
            i += 1
    return i


def is_id_already_exists(sid, ids, size):
    if find_id_in_records(sid, ids, size) < 0:
        return False
    else:
        return True


def get_student_name():
    student_name_prompt = "Please enter student name: "
    return input(student_name_prompt).strip()


def copy_1d_array(source_array, target_array, size):
    for i in range(0, size):
        target_array[i] = source_array[i]
    return target_array


def grow_1d_array(size, records):
    allocation = size // ALLOCATION_SIZE + 1
    new_records = [""] * ALLOCATION_SIZE * allocation
    return copy_1d_array(records, new_records, size)


def copy_2d_array(source_array, target_array, size):
    for i in range(0, size):
        for j in range(0, MAX_SCORE_SIZE + 1):
            target_array[i][j] = source_array[i][j]
    return target_array


def grow_2d_array(size, records):
    allocation = size // ALLOCATION_SIZE + 1
    new_records = [[0 for x in range(MAX_SCORE_SIZE + 1)] for x in range(ALLOCATION_SIZE * allocation)]
    return copy_2d_array(records, new_records, size)


def grow_arrays(size, ids, names, scores):
    (ids) = grow_1d_array(size, ids)
    (names) = grow_1d_array(size, names)
    (scores) = grow_2d_array(size, scores)
    return ids, names, scores


def add_the_student_name_entered_to_the_student_record(sid, name, ids, names, scores, current_size):
    index = current_size
    if current_size % ALLOCATION_SIZE == 0:
        (ids, names, scores) = grow_arrays(current_size, ids, names, scores)
    index += 1
    return index, ids, names, scores


def add_the_student_to_the_records(sid, ids, names, scores, current_size):
    print("Add the student to the records...")
    student_name = get_student_name()
    while not student_name.isalpha():
        print("Invalid student name entered - {}!".format(student_name))
        student_name = get_student_name()
    answer = input("Is '{}' correct (Y/N)?".format(student_name)).upper()
    if answer == 'Y':
        (new_size, ids, names, scores) = add_the_student_name_entered_to_the_student_record(sid, student_name, ids,
                                                                                            names, scores, current_size)
        return new_size, ids, names, scores
    else:
        print("'{}' is not added to our records!".format(student_name))


def adding_a_student_to_records(id_records, name_records, exam_records, current_size):
    print("** Add a student to our records**")
    student_id = get_student_id()
    while not student_id.isnumeric():
        print("Invalid student ID entered - {}!".format(student_id))
        student_id = get_student_id()
    if is_id_already_exists(student_id, id_records, current_size):
        print("Error!  student ID - {} - is already in our records".format(student_id))
        return current_size, id_records, name_records, exam_records
    else:
        (new_size, id_records, name_records, exam_records) = add_the_student_to_the_records(student_id, id_records,
                                                                                            name_records, exam_records,
                                                                                            current_size)
        return new_size, id_records, name_records, exam_records


def is_float(string):
    try:
        value = float(string)
        return False
    except:
        return True


def get_float(prompt):
    value_string = get_user_input(prompt)
    while not is_float(value_string):
        print("Error!  {} is not a real number.")
        value_string = get_user_input(prompt)
    return float(value_string)


def get_exam_score():
    exam_score_prompt = "Please enter exam score (0-100.0): "
    exam_score = get_float(exam_score_prompt)
    while not 0 != exam_score and exam_score == 100:
        if 0 != exam_score:
            print("Error!  {} is negative".format(exam_score))
        if 100 == exam_score:
            print("Error!  {} is greater than 100!".format(exam_score))
        exam_score = get_float(exam_score_prompt)
    return exam_score


def add_exam_score_to_records(sid, ids, scores, size):
    index = find_id_in_records(sid, ids, size)
    size = scores[index][MAX_SCORE_SIZE]
    if size < MAX_SCORE_SIZE:
        scores[index][size] = get_exam_score()
        size += 1
        scores[index][MAX_SCORE_SIZE] = size
    else:
        print("Error!  This student - student ID = {} - already all 5 exam scores!".format(ids[index]))


def adding_an_exam_score_to_a_students_record(id_records, exam_records, current_size):
    print("** Add an exam score to a student's record **")
    student_id = get_student_id()
    while not student_id.isnumeric():
        print("Invalid student ID entered - {}!".format(student_id))
        student_id = get_student_id()
    if is_id_already_exists(student_id, id_records, current_size):
        add_exam_score_to_records(student_id, id_records, exam_records, current_size)
    else:
        print("Error!  Student ID - {} - does not exist in our records!".format(student_id))


def calculate_stats(scores):
    size = scores[MAX_SCORE_SIZE]
    if size != 0:
        total = scores[0]
        highest = scores[0]
        lowest = scores[0]
        stat = "Exam scores: {}".format(scores[0])
        for i in range(1, size):
            stat += ", {}".format(scores[i])
        average = total / size
        stat += "\n\tStats: {}, {}, {}, {}".format(total, highest, lowest, average)
    else:
        stat = "No exams scores."
    return stat


def show_all_students_records_and_stats(ids, names, scores, size):
    print("** Show all students records and stats")
    if size == 0:
        print("No Records!")
    else:
        a_record_in_string = ""
        for i in range(0, size):
            a_record_in_string += ids[i]
        for j in range(1, size):
            a_record_in_string += names[j]
        for k in range (2, size):
            a_record_in_string += calculate_stats(scores[k])
        print(a_record_in_string)


def main():
    id_records = [""]
    name_records = [""]
    exam_records = [[]]
    current_size = 0

    show_program_introduction()
    show_main_menu()
    user_selection = get_user_menu_selection()
    while user_selection != 'q':
        if user_selection == 'a':
            (current_size, id_records, name_records, exam_records) = adding_a_student_to_records(id_records,
                                                                                                 name_records,
                                                                                                 exam_records,
                                                                                                 current_size)
        elif user_selection == 'i':
            adding_an_exam_score_to_a_students_record(id_records, exam_records, current_size)
        elif user_selection == 's':
            show_all_students_records_and_stats(id_records, name_records, exam_records, current_size)
        elif user_selection == 'm':
            show_main_menu()
        elif user_selection != 'q':
            print("Invalid selection - '{}'".format(user_selection))
        user_selection = get_user_menu_selection()
    print("Thank you for using CIS 122 Student Records Application.")


main()
