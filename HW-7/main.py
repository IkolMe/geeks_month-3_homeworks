from parser import *
from db.queries import create_table, insert_data


MAIN_URL = 'https://www.house.kg/snyat'


def main():
    html = get_html(MAIN_URL)
    selector = Selector(text=html)
    create_table()
    insert_data(selector)


if __name__ == '__main__':
    main()
