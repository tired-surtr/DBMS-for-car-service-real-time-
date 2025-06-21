import tkinter as tk
import mysql.connector


# Database connection function (replace with your actual credentials)
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MituGok@mysql20",
            database="sri_maruti_auto_service"
        )
        return mydb
    except mysql.connector.Error as err:
        print("Error connecting to database:", err)
        return None


# Function to manage customers
def manage_customers():
    customer_window = tk.Tk()
    customer_window.title("Manage Customers")

    # Function to add a new customer
    def add_new_customer():
        # Database connection and error handling
        mydb = connect_to_database()
        if not mydb:
            return

        try:
            customer_id = customer_id_entry.get()  # Get customer ID from entry field
            name = customer_name_entry.get()
            phone_number = phone_number_entry.get()
            vehicle_number = vehicle_number_entry.get()
            address = address_entry.get()
            vehicle = vehicle_entry.get()

            # Using all columns in the INSERT query
            sql = "INSERT INTO customer (CUSTOMER_ID, NAME, PHONE_NUMBER, VEHICLE_NUMBER, ADDRESS, VEHICLE) " \
                  "VALUES (%s, %s, %s, %s, %s, %s) "

            # Execute query
            cursor = mydb.cursor()
            cursor.execute(sql, (customer_id, name, phone_number, vehicle_number, address, vehicle))
            mydb.commit()

            # Display confirmation message
            confirmation_label.config(text="New customer added successfully!", fg="green")

            # Clear entry fields after successful addition
            clear_customer_entries()

        except mysql.connector.Error as err:
            print("Error adding customer:", err)
            confirmation_label.config(text="Error adding customer!", fg="red")

        finally:
            if mydb:
                mydb.close()

    # Function to clear entry fields
    def clear_customer_entries():
        customer_id_entry.delete(0, tk.END)
        customer_name_entry.delete(0, tk.END)
        phone_number_entry.delete(0, tk.END)
        vehicle_number_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        vehicle_entry.delete(0, tk.END)
        confirmation_label.config(text="", fg="black")  # Reset confirmation label

    # Labels and entry fields for customer details
    customer_id_label = tk.Label(customer_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = tk.Entry(customer_window)  # Entry field for customer ID
    customer_id_entry.pack()

    customer_name_label = tk.Label(customer_window, text="Customer Name:")
    customer_name_label.pack()
    customer_name_entry = tk.Entry(customer_window)
    customer_name_entry.pack()

    phone_number_label = tk.Label(customer_window, text="Phone Number:")
    phone_number_label.pack()
    phone_number_entry = tk.Entry(customer_window, width=10)
    phone_number_entry.pack()

    vehicle_number_label = tk.Label(customer_window, text="Vehicle Number:")
    vehicle_number_label.pack()
    vehicle_number_entry = tk.Entry(customer_window)
    vehicle_number_entry.pack()

    address_label = tk.Label(customer_window, text="Address:")
    address_label.pack()
    address_entry = tk.Entry(customer_window)
    address_entry.pack()

    vehicle_label = tk.Label(customer_window, text="Vehicle:")
    vehicle_label.pack()
    vehicle_entry = tk.Entry(customer_window)
    vehicle_entry.pack()

    # Button for adding a customer
    add_button = tk.Button(customer_window, text="Add Customer", command=add_new_customer)
    add_button.pack()

    # Label for confirmation message
    confirmation_label = tk.Label(customer_window, text="")
    confirmation_label.pack()

    customer_window.mainloop()


# Function to manage automotive parts
def manage_automotive_parts():
    # Similar structure to manage_customers function
    # Create a new window for automotive parts management
    automotive_parts_window = tk.Tk()
    automotive_parts_window.title("Manage Automotive Parts")

    # Function to add a new automotive part
    def add_new_automotive_part():
        # Database connection and error handling
        mydb = connect_to_database()
        if not mydb:
            return

        try:
            part_name = part_name_entry.get()
            qty = qty_entry.get()
            purchase_date = purchase_date_entry.get()
            parts_price = parts_price_entry.get()
            supplier_name = supplier_name_entry.get()

            # Using all columns in the INSERT query
            sql = "INSERT INTO automotive_parts (PART_NAME, QTY, PURCHASE_DATE, PARTS_PRICE, SUPPLIER_NAME) VALUES (" \
                  "%s, %s, %s, %s, %s) "

            # Execute query
            cursor = mydb.cursor()
            cursor.execute(sql, (part_name, qty, purchase_date, parts_price, supplier_name))
            mydb.commit()

            # Display confirmation message
            confirmation_label.config(text="New automotive part added successfully!", fg="green")

            # Clear entry fields after successful addition
            clear_automotive_part_entries()

        except mysql.connector.Error as err:
            print("Error adding automotive part:", err)
            confirmation_label.config(text="Error adding automotive part!", fg="red")

        finally:
            if mydb:
                mydb.close()

    # Function to clear entry fields for automotive parts
    def clear_automotive_part_entries():
        # ... (similar logic to clear_customer_entries)
        part_name_entry.delete(0, tk.END)
        qty_entry.delete(0, tk.END)
        purchase_date_entry.delete(0, tk.END)
        parts_price_entry.delete(0, tk.END)
        supplier_name_entry.delete(0, tk.END)
        confirmation_label.config(text="", fg="black")  # Reset confirmation label

    # Labels and entry fields for automotive part details
    part_name_label = tk.Label(automotive_parts_window, text="Part Name:")
    part_name_label.pack()
    part_name_entry = tk.Entry(automotive_parts_window)
    part_name_entry.pack()

    qty_label = tk.Label(automotive_parts_window, text="Quantity:")
    qty_label.pack()
    qty_entry = tk.Entry(automotive_parts_window)
    qty_entry.pack()

    purchase_date_label = tk.Label(automotive_parts_window, text="Purchase Date (YYYY-MM-DD):")
    purchase_date_label.pack()
    purchase_date_entry = tk.Entry(automotive_parts_window)
    purchase_date_entry.pack()

    parts_price_label = tk.Label(automotive_parts_window, text="Parts Price:")
    parts_price_label.pack()
    parts_price_entry = tk.Entry(automotive_parts_window)
    parts_price_entry.pack()

    supplier_name_label = tk.Label(automotive_parts_window, text="Supplier Name:")
    supplier_name_label.pack()
    supplier_name_entry = tk.Entry(automotive_parts_window)
    supplier_name_entry.pack()

    # Button for adding a new automotive part
    add_button = tk.Button(automotive_parts_window, text="Add Automotive Part", command=add_new_automotive_part)
    add_button.pack()

    # Label for confirmation message
    confirmation_label = tk.Label(automotive_parts_window, text="")
    confirmation_label.pack()

    automotive_parts_window.mainloop()


# Function to manage deliveries
# Function to manage deliveries
def manage_deliveries():
    delivery_window = tk.Tk()
    delivery_window.title("Manage Deliveries")

    # Function to add a new delivery
    def add_new_delivery():
        # Database connection and error handling
        mydb = connect_to_database()
        if not mydb:
            return

        try:
            # Retrieve delivery details from entry fields
            customer_id = customer_id_entry.get()
            delivery_date = delivery_date_entry.get()
            delivery_time = delivery_time_entry.get()
            amount = amount_entry.get()
            feedback = feedback_entry.get()
            mode_of_payment = mode_of_payment_entry.get()

            # Using all columns in the INSERT query
            sql = "INSERT INTO delivery (CUSTOMER_ID, DELIVERY_DATE, DELIVERY_TIME, AMOUNT, FEEDBACK, MODE_OF_PAYMENT) " \
                  "VALUES (%s, %s, %s, %s, %s, %s) "

            # Execute query
            cursor = mydb.cursor()
            cursor.execute(sql, (customer_id, delivery_date, delivery_time, amount, feedback, mode_of_payment))
            mydb.commit()

            # Display confirmation message
            confirmation_label.config(text="New delivery added successfully!", fg="green")

            # Clear entry fields after successful addition
            clear_delivery_entries()

        except mysql.connector.Error as err:
            print("Error adding delivery:", err)
            confirmation_label.config(text="Error adding delivery!", fg="red")

        finally:
            if mydb:
                mydb.close()

    # Function to clear entry fields
    def clear_delivery_entries():
        # Clear entry fields for delivery
        customer_id_entry.delete(0, tk.END)
        delivery_date_entry.delete(0, tk.END)
        delivery_time_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        feedback_entry.delete(0, tk.END)
        mode_of_payment_entry.delete(0, tk.END)
        confirmation_label.config(text="", fg="black")  # Reset confirmation label

    # Labels and entry fields for delivery details
    customer_id_label = tk.Label(delivery_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = tk.Entry(delivery_window)
    customer_id_entry.pack()

    delivery_date_label = tk.Label(delivery_window, text="Delivery Date (YYYY-MM-DD):")
    delivery_date_label.pack()
    delivery_date_entry = tk.Entry(delivery_window)
    delivery_date_entry.pack()

    delivery_time_label = tk.Label(delivery_window, text="Delivery Time:")
    delivery_time_label.pack()
    delivery_time_entry = tk.Entry(delivery_window)
    delivery_time_entry.pack()

    amount_label = tk.Label(delivery_window, text="Amount:")
    amount_label.pack()
    amount_entry = tk.Entry(delivery_window)
    amount_entry.pack()

    feedback_label = tk.Label(delivery_window, text="Feedback:")
    feedback_label.pack()
    feedback_entry = tk.Entry(delivery_window)
    feedback_entry.pack()

    mode_of_payment_label = tk.Label(delivery_window, text="Mode of Payment:")
    mode_of_payment_label.pack()
    mode_of_payment_entry = tk.Entry(delivery_window)
    mode_of_payment_entry.pack()

    # Button for adding a new delivery
    add_button = tk.Button(delivery_window, text="Add Delivery", command=add_new_delivery)
    add_button.pack()

    # Label for confirmation message
    confirmation_label = tk.Label(delivery_window, text="")
    confirmation_label.pack()

    delivery_window.mainloop()


def manage_employees():
    # Create a new window for employee management
    employee_window = tk.Tk()
    employee_window.title("Manage Employees")

    # Function to add a new employee
    def add_new_employee():
        # Database connection and error handling
        mydb = connect_to_database()
        if not mydb:
            return

        try:
            # Retrieve employee details from entry fields
            emp_name = emp_name_entry.get()
            age = age_entry.get()
            emp_phone_number = emp_phone_number_entry.get()
            emp_address = emp_address_entry.get()
            designation = designation_entry.get()

            # Using all columns in the INSERT query
            sql = "INSERT INTO employee (EMP_NAME, AGE, EMP_PHONE_NUMBER, EMP_ADDRESS, DESIGNATION) " \
                  "VALUES (%s, %s, %s, %s, %s) "

            # Execute query
            cursor = mydb.cursor()
            cursor.execute(sql, (emp_name, age, emp_phone_number, emp_address, designation))
            mydb.commit()

            # Display confirmation message
            confirmation_label.config(text="New employee added successfully!", fg="green")

            # Clear entry fields after successful addition
            clear_employee_entries()

        except mysql.connector.Error as err:
            print("Error adding employee:", err)
            confirmation_label.config(text="Error adding employee!", fg="red")

        finally:
            if mydb:
                mydb.close()

    # Function to clear entry fields for employees
    def clear_employee_entries():
        # Clear entry fields for employees
        emp_name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        emp_phone_number_entry.delete(0, tk.END)
        emp_address_entry.delete(0, tk.END)
        designation_entry.delete(0, tk.END)
        confirmation_label.config(text="", fg="black")  # Reset confirmation label

    # Labels and entry fields for employee details
    emp_name_label = tk.Label(employee_window, text="Employee Name:")
    emp_name_label.pack()
    emp_name_entry = tk.Entry(employee_window)
    emp_name_entry.pack()

    age_label = tk.Label(employee_window, text="Age:")
    age_label.pack()
    age_entry = tk.Entry(employee_window)
    age_entry.pack()

    emp_phone_number_label = tk.Label(employee_window, text="Phone Number:")
    emp_phone_number_label.pack()
    emp_phone_number_entry = tk.Entry(employee_window)
    emp_phone_number_entry.pack()

    emp_address_label = tk.Label(employee_window, text="Address:")
    emp_address_label.pack()
    emp_address_entry = tk.Entry(employee_window)
    emp_address_entry.pack()

    designation_label = tk.Label(employee_window, text="Designation:")
    designation_label.pack()
    designation_entry = tk.Entry(employee_window)
    designation_entry.pack()

    # Button for adding a new employee
    add_button = tk.Button(employee_window, text="Add Employee", command=add_new_employee)
    add_button.pack()

    # Label for confirmation message
    confirmation_label = tk.Label(employee_window, text="")
    confirmation_label.pack()

    employee_window.mainloop()


def manage_vehicles():
    # Create a new window for vehicle management
    vehicle_window = tk.Tk()
    vehicle_window.title("Manage Vehicles")

    # Function to add a new vehicle
    def add_new_vehicle():
        # Database connection and error handling
        mydb = connect_to_database()
        if not mydb:
            return

        try:
            # Retrieve vehicle details from entry fields
            customer_id = customer_id_entry.get()
            fuel_info = fuel_info_entry.get()
            mileage = mileage_entry.get()
            model = model_entry.get()
            odometer_reading = odometer_reading_entry.get()
            remarks = remarks_entry.get()

            # Using all columns in the INSERT query
            sql = "INSERT INTO vehicle (CUSTOMER_ID, FUEL_INFO, MILEAGE, MODEL, ODOMETER_READING, REMARKS) " \
                  "VALUES (%s, %s, %s, %s, %s, %s) "

            # Execute query
            cursor = mydb.cursor()
            cursor.execute(sql, (customer_id, fuel_info, mileage, model, odometer_reading, remarks))
            mydb.commit()

            # Display confirmation message
            confirmation_label.config(text="New vehicle added successfully!", fg="green")

            # Clear entry fields after successful addition
            clear_vehicle_entries()

        except mysql.connector.Error as err:
            print("Error adding vehicle:", err)
            confirmation_label.config(text="Error adding vehicle!", fg="red")

        finally:
            if mydb:
                mydb.close()

    # Function to clear entry fields for vehicles
    def clear_vehicle_entries():
        # Clear entry fields for vehicles
        customer_id_entry.delete(0, tk.END)
        fuel_info_entry.delete(0, tk.END)
        mileage_entry.delete(0, tk.END)
        model_entry.delete(0, tk.END)
        odometer_reading_entry.delete(0, tk.END)
        remarks_entry.delete(0, tk.END)
        confirmation_label.config(text="", fg="black")  # Reset confirmation label

    # Labels and entry fields for vehicle details
    customer_id_label = tk.Label(vehicle_window, text="Customer ID:")
    customer_id_label.pack()
    customer_id_entry = tk.Entry(vehicle_window)
    customer_id_entry.pack()

    fuel_info_label = tk.Label(vehicle_window, text="Fuel Info:")
    fuel_info_label.pack()
    fuel_info_entry = tk.Entry(vehicle_window)
    fuel_info_entry.pack()

    mileage_label = tk.Label(vehicle_window, text="Mileage:")
    mileage_label.pack()
    mileage_entry = tk.Entry(vehicle_window)
    mileage_entry.pack()

    model_label = tk.Label(vehicle_window, text="Model:")
    model_label.pack()
    model_entry = tk.Entry(vehicle_window)
    model_entry.pack()

    odometer_reading_label = tk.Label(vehicle_window, text="Odometer Reading:")
    odometer_reading_label.pack()
    odometer_reading_entry = tk.Entry(vehicle_window)
    odometer_reading_entry.pack()

    remarks_label = tk.Label(vehicle_window, text="Remarks:")
    remarks_label.pack()
    remarks_entry = tk.Entry(vehicle_window)
    remarks_entry.pack()

    # Button for adding a new vehicle
    add_button = tk.Button(vehicle_window, text="Add Vehicle", command=add_new_vehicle)
    add_button.pack()

    # Label for confirmation message
    confirmation_label = tk.Label(vehicle_window, text="")
    confirmation_label.pack()

    vehicle_window.mainloop()


# Function to create the main window
def main_window():
    try:
        window = tk.Tk()
        window.title("Sri Maruti Auto Service")
        window.geometry("200x250")  # Set initial window size

        # Create buttons for both customer and automotive parts management
        manage_customer_button = tk.Button(window, text="Manage Customers", command=manage_customers, bg="lightblue", padx=10, pady=5)
        manage_customer_button.pack(pady=5)

        manage_automotive_parts_button = tk.Button(window, text="Manage Automotive Parts",
                                                   command=manage_automotive_parts, bg="lightgreen", padx=10, pady=5)
        manage_automotive_parts_button.pack(pady=5)

        manage_deliveries_button = tk.Button(window, text="Manage Deliveries", command=manage_deliveries, bg="lightcoral", padx=10, pady=5)
        manage_deliveries_button.pack(pady=5)

        manage_employees_button = tk.Button(window, text="Manage Employees", command=manage_employees, bg="lightyellow", padx=10, pady=5)
        manage_employees_button.pack(pady=5)

        manage_vehicles_button = tk.Button(window, text="Manage Vehicles", command=manage_vehicles, bg="lightpink", padx=10, pady=5)
        manage_vehicles_button.pack(pady=5)

        # Start the main window's event loop
        window.mainloop()  # Crucial for displaying the window

    except tk.TclError as err:
        print("Error creating window:", err)


# Start the main window
main_window()
