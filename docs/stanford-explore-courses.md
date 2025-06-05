# NLWeb Stanford Course Explorer

Start by following steps 1-6 in the [NLWeb Hello World](nlweb-hello-world.md) guide.


## Data 

We download data using the [Stanford Explore Courses API](https://github.com/jeremyephron/explore-courses-api).

Install the API:

```bash
pip install explorecourses
```

Run the download script:

```bash
cd code
python download_courses.py
```

This script will download the courses and save them to the `data/json/courses.json` file. It's about 20MB, so we can just keep it in the repo. Each line is a JSON object representing a course. An example is shown below:

```json
{
  "year": "2024-2025",
  "subject": "AA",
  "code": "100",
  "title": "Introduction to Aeronautics and Astronautics",
  "description": "This class introduces the basics of aeronautics and astronautics through applied physics, hands-on activities, and real world examples. The principles of fluid flow, flight, and propulsion for aircraft will be illustrated, including the creation of lift and drag, aerodynamic performance including takeoff, climb, range, and landing. The principles of orbits, maneuvers, space environment, and propulsion for spacecraft will be illustrated. Students will be exposed to the history and challenges of aeronautics and astronautics.",
  "gers": [
    "GER:DB-EngrAppSci",
    "WAY-AQR",
    "WAY-SMA"
  ],
  "repeatable": false,
  "grading_basis": "Letter or Credit/No Credit",
  "units_min": 3,
  "units_max": 3,
  "final_exam": true,
  "terms": [
    "2024-2025 Autumn"
  ],
  "instructors": [
    "Hannah  Nabavi",
    "Kendall  Seefried",
    "Funmilayo Comfort Adeeye",
    "Manan  Arya"
  ],
  "course_id": 103093,
  "active": true,
  "offer_num": "1",
  "academic_group": "ENGR",
  "academic_org": "AEROASTRO",
  "academic_career": "UG",
  "max_units_repeat": 3,
  "max_times_repeat": 1,
  "@type": "Course",
  "url": "https://explorecourses.stanford.edu/search?view=catalog&filter-coursestatus-Active=on&page=0&catalog=&academicYear=2024-2025&q=%22AA+100%22&collapse="
}
```

Because some of these objects are too large to fit in the database, we truncate the description field. See `download_courses.py` for more details.

## Load the data into the database

```bash
python -m tools.db_load ../data/json/courses.json "Stanford-Explore-Courses"
```

## Run the chatbot

```bash
python app-file.py
```