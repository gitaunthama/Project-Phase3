from datetime import datetime

def exit_program():
    print("Goodbye!")
    exit()


# helpers.py or appropriate file

def print_table(headers, rows):
    # Print headers
    header_row = " | ".join(headers)
    print(header_row)
    print("-" * len(header_row))

    # Print rows
    for row in rows:
        row_str = " | ".join(map(str, row))
        print(row_str)




def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False
