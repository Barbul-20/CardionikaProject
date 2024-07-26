import psycopg2


def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="cardionika",
            user="postgres",
            password="1337",
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None


def insert_data(query, data):
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query, data)
            connection.commit()
        except Exception as error:
            print(f"Error inserting data: {error}")
        finally:
            cursor.close()
            connection.close()


def fetch_data(query):
    connection = connect_to_db()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Exception as error:
            print(f"Error fetching data: {error}")
            return None
        finally:
            cursor.close()
            connection.close()


# Medical Institutions
def insert_medical_institution(name, address, phone, email, med_type, website, worktime, head):
    query = """
    INSERT INTO medical_institutions (
        medical_name, medical_address, medical_phone, medical_email, medical_type, medical_website, medical_worktime, medical_head
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (name, address, phone, email, med_type, website, worktime, head)
    insert_data(query, data)


def get_medical_institutions():
    query = "SELECT * FROM medical_institutions"
    return fetch_data(query)


# Equipment
def insert_equipment(name, equip_type, manufacturer, model, serial_number, buy_date, state):
    query = """
    INSERT INTO equipment (
        equipment_name, equipment_type, equipment_manufacturer, equipment_model, equipment_serial_number, equipment_buy_date, equipment_state
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data = (name, equip_type, manufacturer, model, serial_number, buy_date, state)
    insert_data(query, data)


def get_equipment():
    query = "SELECT * FROM equipment"
    return fetch_data(query)


# Employees
def insert_employee(surname, name, patronymic, title, speciality, phone, email, birthday, employment_date, med_institution):
    query = """
    INSERT INTO employees (
        employees_surname, employees_name, employees_patronymic, employees_title, employees_speciality, employees_phone, employees_email, employees_birthday, employees_employment_date, employees_medical_institutions
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (surname, name, patronymic, title, speciality, phone, email, birthday, employment_date, med_institution)
    insert_data(query, data)


def get_employees():
    query = "SELECT * FROM employees"
    return fetch_data(query)


# Patients
def insert_patient(surname, name, patronymic, birthday, gender, address, phone, email, policy, medical_history, med_institution):
    query = """
    INSERT INTO patients (
        patient_surname, patient_name, patient_patronymic, patient_birthday, patient_gender, patient_address, patient_phone, patient_email, patient_policy, patient_medical_history, patient_medical_institutions
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (surname, name, patronymic, birthday, gender, address, phone, email, policy, medical_history, med_institution)
    insert_data(query, data)


def get_patients():
    query = "SELECT * FROM patients"
    return fetch_data(query)