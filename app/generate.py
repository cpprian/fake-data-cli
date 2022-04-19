from PyInquirer import prompt
from examples import custom_style_2

from app.questions import csv, excel, sql, generate_file

def generate_txt():
    pass

def generate_csv():
    c = prompt(csv, style=custom_style_2)
    d = c.get("csv_option")

def generate_excel():
    e = prompt(excel, style=custom_style_2)
    f = e.get("excel_sheet_name")
    g = e.get("excel_column")

def generate_sql():
    s = prompt(sql, style=custom_style_2)
    t = s.get("sql_database")
    u = s.get("sql_table")
    v = s.get("sql_column")

def new_file(data) -> tuple:
    s = prompt(generate_file, style=custom_style_2)
    a = s.get("file_name")
    b = s.get("size")
    return (a, b)