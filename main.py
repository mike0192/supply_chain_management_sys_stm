import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=.\\SQLEXPRESS;"
    "DATABASE=SUPPLY_CHAIN;"
    "Trusted_Connection=yes;"
)

print("Connected successfully!")
cursor = conn.cursor()

# Current user variables
current_user = None
current_role = None

# Material Functions
def addmaterial():
    id=int(input("Enter the material's id: "))
    name=input("Enter the material's name: ")
    supp=input("Enter the supplier's name: ")
    cost=int(input("Enter the cost of the material: "))
    cursor.execute(
        "INSERT INTO RAW_MATERIALS (MAT_ID, M_NAME, SUPPLIER, COST) VALUES (?, ?, ?, ?)", 
        (id, name, supp, cost)
    )
    conn.commit()
    print("Material added successfully!")

def viewallrawmaterials():
    cursor.execute("SELECT * FROM RAW_MATERIALS")
    raw_m = cursor.fetchall()
    for materials in raw_m:
        print(f"ID: {materials.MAT_ID}, Name: {materials.M_NAME}, Supplier: {materials.SUPPLIER}, Cost: {materials.COST}")

def updatematerialinfo():
    id=int(input("Enter material ID to update: "))
    new_name=input("Enter new material name: ")
    new_sup=input("Enter new supplier name: ")
    new_cost=int(input("Enter new material cost: "))
    cursor.execute(
        "UPDATE RAW_MATERIALS SET M_NAME = ?, SUPPLIER = ?, COST = ? WHERE MAT_ID = ?",
        (new_name, new_sup, new_cost, id),
    )
    conn.commit()
    print("Material updated successfully!")

def deletematerial():
    id = int(input("Enter material id to delete: "))
    cursor.execute("DELETE FROM RAW_MATERIALS WHERE MAT_ID = ?", (id,))
    conn.commit()
    print("Material deleted successfully!")

# Product Functions
def addproduct():
    prod_id=int(input("Enter the product's id: "))
    name=input("Enter the product's name: ")
    cost=int(input("Enter the cost of the product: "))
    price=int(input("Enter the product's price: "))
    cursor.execute(
        "INSERT INTO PRODUCTT (PRODUCT_ID, P_NAME, COST, PRICE) VALUES (?, ?, ?, ?)", 
        (prod_id, name, cost, price)
    )
    conn.commit()
    print("Product added successfully!")

def viewallproduct():
    cursor.execute("SELECT * FROM PRODUCTT")
    prod = cursor.fetchall()
    for product in prod:
        print(f"ID: {product.PRODUCT_ID}, Name: {product.P_NAME}, Cost: {product.COST}, Price: {product.PRICE}")

def updateproductinfo():
    id=int(input("Enter Product ID to update: "))
    new_name=input("Enter new product name: ")
    new_cost=int(input("Enter the new product's cost: "))
    new_price=int(input("Enter the new product's price: "))
    cursor.execute(
        "UPDATE PRODUCTT SET P_NAME = ?, COST = ?, PRICE = ? WHERE PRODUCT_ID = ?",
        (new_name, new_cost, new_price, id),
    )
    conn.commit()
    print("Product updated successfully!")

def deleteproduct():
    id = int(input("Enter product id to delete: "))
    cursor.execute("DELETE FROM PRODUCTT WHERE PRODUCT_ID = ?", (id,))
    conn.commit()
    print("Product deleted successfully!")

# Customer Functions
def addcustomer():
    c_id=int(input("Enter the customer's id: "))
    name=input("Enter the customer's name: ")
    typee=input("Enter the customer type (Retail or Wholesale): ")
    cursor.execute(
        "INSERT INTO CUSTOMER (C_ID, C_NAME, TYPE) VALUES (?, ?, ?)", 
        (c_id, name, typee)
    )
    conn.commit()
    print("Customer added successfully!")

def viewallcustomer():
    cursor.execute("SELECT * FROM CUSTOMER")
    cust = cursor.fetchall()
    for customer in cust:
        print(f"ID: {customer.C_ID}, Name: {customer.C_NAME}, Type: {customer.TYPE}")

def updatecustomerinfo():
    id=int(input("Enter the customer id to update: "))
    new_name=input("Enter the new customer name: ")
    new_type=input("Modify the customer's type: ")
    cursor.execute(
        "UPDATE CUSTOMER SET C_NAME = ?, TYPE = ? WHERE C_ID = ?",
        (new_name, new_type, id),
    )
    conn.commit()
    print("Customer updated successfully!")

def deletecustomer():
    id = int(input("Enter customer id to delete: "))
    cursor.execute("DELETE FROM CUSTOMER WHERE C_ID = ?", (id,))
    conn.commit()
    print("Customer deleted successfully!")

# Authentication Functions
def register():
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (Admin/User): ").capitalize()
    
    if role not in ['Admin', 'User']:
        print("Error: Role must be 'Admin' or 'User'")
        return
    
    try:
        cursor.execute("""
            INSERT INTO AUTH (Username, Password, Role)
            VALUES (?, ?, ?)
        """, (username, password, role))
        conn.commit()
        print(f"User '{username}' registered successfully as {role}.")
    except pyodbc.IntegrityError:
        print("Error: Username already exists.")
    except Exception as e:
        print(f"Error: {e}")

def login():
    global current_user, current_role
    
    username = input("Username: ")
    password = input("Password: ")
    
    cursor.execute("""
        SELECT UserID, Role FROM AUTH
        WHERE Username = ? AND Password = ?
    """, (username, password))
    result = cursor.fetchone()
    
    if result:
        user_id, role = result
        current_user = username
        current_role = role
        print(f"Login successful! Welcome, {username} ({role})")
        return True
    else:
        print("Invalid credentials.")
        return False

def logout():
    global current_user, current_role
    if current_user:
        print(f"Goodbye {current_user}!")
        current_user = None
        current_role = None
    else:
        print("No user is logged in.")


def material_menu():
    while True:
        print("\n--- Material Management ---")
        print("1. View All Materials")
        if current_role == 'Admin':
            print("2. Add Material")
            print("3. Update Material")
            print("4. Delete Material")
            print("5. Back to Main Menu")
        else:
            print("2. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            viewallrawmaterials()
        elif current_role == 'Admin':
            if choice == "2":
                addmaterial()
            elif choice == "3":
                updatematerialinfo()
            elif choice == "4":
                deletematerial()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        else:
            if choice == "2":
                break
            else:
                print("Invalid choice.")

def product_menu():
    while True:
        print("\n--- Product Management ---")
        print("1. View All Products")
        if current_role == 'Admin':
            print("2. Add Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. Back to Main Menu")
        else:
            print("2. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            viewallproduct()
        elif current_role == 'Admin':
            if choice == "2":
                addproduct()
            elif choice == "3":
                updateproductinfo()
            elif choice == "4":
                deleteproduct()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        else:
            if choice == "2":
                break
            else:
                print("Invalid choice.")

def customer_menu():
    while True:
        print("\n--- Customer Management ---")
        print("1. View All Customers")
        if current_role == 'Admin':
            print("2. Add Customer")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. Back to Main Menu")
        else:
            print("2. Back to Main Menu")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            viewallcustomer()
        elif current_role == 'Admin':
            if choice == "2":
                addcustomer()
            elif choice == "3":
                updatecustomerinfo()
            elif choice == "4":
                deletecustomer()
            elif choice == "5":
                break
            else:
                print("Invalid choice.")
        else:
            if choice == "2":
                break
            else:
                print("Invalid choice.")

def main_menu():
    global current_user, current_role
    
    while True:
        print("\nSUPPLY CHAIN MANAGEMENT SYSTEM")
        
        if current_user:
            print(f"[Logged in as: {current_user} ({current_role})]")
            print("\nMAIN MENU:")
            print("1. Material Management")
            print("2. Product Management")
            print("3. Customer Management")
            print("4. Logout")
            if current_role == 'Admin':
                print("5. Register New User")
            print("0. Exit System")
            
            choice = input("\nChoose an option: ")
            
            if choice == "1":
                material_menu()
            elif choice == "2":
                product_menu()
            elif choice == "3":
                customer_menu()
            elif choice == "4":
                logout()
            elif choice == "5" and current_role == 'Admin':
                register()
            elif choice == "0":
                print("\nExiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
                
        else:
            print("\nPlease login or register:")
            print("1. Login")
            print("2. Register")
            print("0. Exit System")
            
            choice = input("\nChoose an option: ")
            
            if choice == "1":
                login()
            elif choice == "2":
                register()
            elif choice == "0":
                print("\nExiting system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
    conn.close()
