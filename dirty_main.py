from datetime import datetime

from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now().strftime("%T %d-%B-%Y"))