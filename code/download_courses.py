from explorecourses import *
from explorecourses import filters
import json

SAVE_FILE = "../data/json/courses.json"

connect = CourseConnection()

# Print out all courses for 2024-2025.
n_truncated = 0
data = []
year = "2024-2025"
courses = connect.get_courses_by_query(query="%", year=year)
for course in courses:
    instructors = []
    terms = []
    for section in course.sections:
        for schedule in section.schedules:
            for instructor in schedule.instructors:
                instructors.append(instructor.first_name + " " + instructor.middle_name + " " + instructor.last_name)
        terms.append(section.term)

    obj = {
        "year": year,
        "subject": course.subject,
        "code": course.code,
        "title": course.title,
        "description": course.description,
        "gers": course.gers,
        "repeatable": course.repeatable,
        "grading_basis": course.grading_basis,
        "units_min": course.units_min,
        "units_max": course.units_max,
        "final_exam": course.final_exam,
        "terms": terms,
        "instructors": instructors,
        "course_id": course.course_id,
        "active": course.active,
        "offer_num": course.offer_num,
        "academic_group": course.academic_group,
        "academic_org": course.academic_org,
        "academic_career": course.academic_career,
        "max_units_repeat": course.max_units_repeat,
        "max_times_repeat": course.max_times_repeat,
        "@type": "Course", # This is required by NLWeb
        "url": f"https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear={year}&q=%22{course.subject}+{course.code}%22&collapse=" # This is required by NLWeb
    }

    # NLWeb requires each entry be less than 20k characters. If the object has too many fields, we truncate the description.
    obj_length = len(json.dumps(obj))
    surplus = obj_length - 20000
    if surplus > 0:
        obj["description"] = obj["description"][:len(obj["description"]) - surplus]
        n_truncated += 1
    data.append(obj)

print(f"Downloaded {len(data)} courses. {n_truncated} courses were truncated.")

# Deduplicate courses by id.
filtered_data = []
ids = set()
for course in data:
    if course["course_id"] not in ids:
        ids.add(course["course_id"])
        filtered_data.append(course)
print(f"Deduplicated {len(data)} courses to {len(filtered_data)} courses.")

# Save the data to a file, with each course on a new line.
with open(SAVE_FILE, "w") as f:
    for course in filtered_data:
        f.write(json.dumps(course) + "\n")
