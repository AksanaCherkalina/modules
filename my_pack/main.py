import application.salary
import application.db.people

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()

if __name__ == '__main__':
    get_employees()


import datetime

dt_now = datetime.datetime.now()
print(dt_now)
