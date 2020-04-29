import sqlite3


def print_data():
    con = sqlite3.connect('proxy.db')
    cur = con.cursor()

    p = cur.execute('''select * from proxy_table''').fetchall()
    print(p)


if __name__ == '__main__':
    print_data()
