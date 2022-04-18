from PyInquirer import prompt
from examples import custom_style_2

from app.questions import start, csv, excel, sql, generate_file

def run():
    answers = prompt(start, style=custom_style_2)
    if answers.get("user_option") == "text file":
        s = prompt(generate_file, style=custom_style_2)
        a = s.get("file_name")
        b = s.get("size")
    elif answers.get("user_option") == "csv file":
        c = prompt(csv, style=custom_style_2)
        d = c.get("csv_option")
        s = prompt(generate_file, style=custom_style_2)
        a = s.get("file_name")
        b = s.get("size")
        print('Generating csv file...')
    elif answers.get("user_option") == "excel sheet":
        e = prompt(excel, style=custom_style_2)
        f = e.get("excel_sheet_name")
        g = e.get("excel_column")
        s = prompt(generate_file, style=custom_style_2)
        a = s.get("file_name")
        b = s.get("size")
        print('Generating excel sheet...')
    elif answers.get("user_option") == "sql query":
        s = prompt(sql, style=custom_style_2)
        t = s.get("sql_database")
        u = s.get("sql_table")
        v = s.get("sql_column")
        s = prompt(generate_file, style=custom_style_2)
        a = s.get("file_name")
        b = s.get("size")
        print('Generating sql query...')

if __name__ == "__main__":
    run()