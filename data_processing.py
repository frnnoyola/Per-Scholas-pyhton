def get_average_grade(grades_tuple):
    """Calculates the average of a tuple of numeric grades."""
    try:
        average = sum(grades_tuple) / len(grades_tuple)
        return average
    except ZeroDivisionError:
        print("Warning: Cannot calculate average for an empty grade list.")
        return None

# Dictionary containing course names and tuples of grades
# Includes an edge case ("Art") with an empty tuple
course_grades = {
    "Math": (90, 85, 92, 78),
    "Science": (88, 94, 91),
    "History": (75, 82, 80),
    "Art": ()  # Edge case: Empty tuple to trigger exception handling
}

# Loop to iterate over the dictionary and print averages
for course, grades in course_grades.items():
    avg = get_average_grade(grades)
    
    if avg is not None:
        print(f"The average grade for {course} is {avg:.1f}")
    else:
        print(f"Could not compute the average for {course}.\n")
