from app_logic import set_first_value, set_second_value, get_addition
from utils import render_template


def add_numbers(environ):
    set_first_value(10)
    set_second_value(20)
    get_addition()

    return render_template("boundaries/add_numbers_data.html")