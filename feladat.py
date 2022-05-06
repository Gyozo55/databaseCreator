import os
import random
import psycopg2
import datetime

# Data

datas = {
    'firstName': ['Gizi', 'Bela', 'Sandor', 'Istvan', 'Julia', 'Margo', 'Kata', 'Ildiko', 'Tamas', 'Ferenc', 'Hunor',
                  'Attila', 'Dome', 'Vazul', 'Jozsef', 'Eva', 'Kinga', 'Vivien', 'Vera', 'Veronika', 'Jake', 'Pablo'],
    'lastName': ['Kovacs', 'Olah', 'Kocsis', 'Erdei', 'Pek', 'Sirato', 'Harangozo', 'Poos', 'Kasai', 'Jambor', 'Takacs',
                 'Kallai', 'Bocskor', 'Meszaros', 'Bethlen', 'Gellerfi', 'Szaniszlo', 'Toros', 'Farago', 'Mehes'],
    'jobs': ['Developer', 'CEO', 'Fundraiser', 'InfantryOfficer', 'Infantry', 'DatabaseArchitect', 'WebDeveloper',
             'Orthoptist', 'CommercialDiver', 'Cooks'],

    'booleans': [True, False]
}


def get_db_connection():
    return psycopg2.connect(
        database=os.getenv('POSTGRES_DB', 'multiDb'),
        user=os.getenv('POSTGRES_USER', 'admin'),
        password=os.getenv('POSTGRES_PASSWORD', 'admin1234'),
        host=os.getenv('POSTGRES_SERVER', '0.0.0.0')
    )


def name_getter_from_dict(type):
    return datas.get(type)[random.randint(0, len(datas.get(type)) - 1)]


def name_creator(full_names):
    first_name = name_getter_from_dict('firstName')
    last_name = name_getter_from_dict('lastName')
    full_name = first_name + '_' + last_name

    if full_name in full_names:
        name_creator(full_names)

    full_names.append(full_name)
    return full_name


# Query the database
def create_table(date_time, cur):
    cur.execute(f"CREATE TABLE creationTime{date_time} ("
                f"firstname text,"
                f"lastname text,"
                f"fullname text,"
                f"age int,"
                f"job text,"
                f"salaryinUSD int,"
                f"active boolean)")
    return date_time


def generate_data(table_name, full_names, cur):
    for i in range(100):
        full_name = name_creator(full_names)
        first_name = full_name.split('_')[0]
        last_name = full_name.split('_')[1]
        cur.execute(
            f"INSERT INTO creationTime{table_name} "
            f" VALUES ('{first_name}', '{last_name}', '{full_name}', {random.randint(20, 60)},"
            f" '{datas.get('jobs')[random.randint(0, len(datas.get('jobs')) - 1)]}', {random.randint(10, 1000)},"
            f" {datas.get('booleans')[random.randint(0, len(datas.get('booleans')) - 1)]})")


def update_salary(table_name, cur):
    cur.execute(f"CREATE TABLE creationTime{table_name}raised AS TABLE creationTime{table_name}")

    cur.execute(f"UPDATE creationTime{table_name}raised "
                f"SET salaryinUSD = salaryinUSD + (salaryinUSD*0.05)"
                f"WHERE job = 'WebDeveloper'")

    cur.execute(f"UPDATE creationTime{table_name}raised "
                f"SET salaryinUSD = salaryinUSD + (salaryinUSD*0.1)"
                f"WHERE job = 'CEO'")


def close_db_connection(conn, cur):
    cur.close()
    conn.commit()
    conn.close()


def main():
    # Connect to existing database
    conn = get_db_connection()
    # Open cursor to perform database operation
    cur = conn.cursor()
    # Get valid epoch time
    date_time = datetime.datetime.now().strftime("%f")
    full_names = []

    # Business Logic
    table_name = create_table(date_time, cur)
    generate_data(table_name, full_names, cur)
    update_salary(table_name, cur)

    # Close communications with database
    close_db_connection(conn, cur)


if __name__ == "__main__":
    main()
