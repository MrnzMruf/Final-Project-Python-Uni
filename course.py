import pandas as pd

"""
List of Course, Add Course attributes, add unit for each course and finally save in file
"""

class Course:
    course_db = pd.read_csv('course1.csv')
    @staticmethod
    def display_courses(major):
        return Course.course_db[Course.course_db['major'] == major]['title'].tolist()
    
    @staticmethod
    def any_capacity(course_title):
        return Course.course_db[Course.course_db['title'] == 'Data Mining']['capacity'].tolist()[0] > 1

    @staticmethod
    def choose_course(course_title):
        i = Course.course_db[Course.course_db['title'] == course_title]['capacity'].index.tolist()[0]
        Course.course_db.loc[i, 'capacity'] -= 1
        return True, Course.course_db.loc[i, 'unit']

    @staticmethod
    def add_course(title, professor, unit, capacity, major):
        d = [{"title": title,
            'professor': professor,
            'unit': unit,
            'capacity': capacity,
            'major': major}]

        Course.course_db = Course.course_db.append(pd.DataFrame(d, index=[Course.course_db.index[-1] + 1]))
        
    @staticmethod
    def save_db(fname='course1.csv'):
        with open(fname, 'w+') as fp:
            fp.write(Course.course_db.to_csv())
        Course.course_db.to_csv()