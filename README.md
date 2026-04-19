Here's a comprehensive README for your GitHub repository:

```markdown
# Supply Chain Management System

A command-line interface (CLI) application for managing supply chain operations, including raw materials, products, customers, inventory, sales, and shipments. The system features role-based access control with Admin and User privileges.

## 📋 Table of Contents
- [Overview](#overview)
- [Database Schema](#database-schema)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Role-Based Access](#role-based-access)
- [System Requirements](#system-requirements)
- [Project Structure](#project-structure)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Supply Chain Management System provides a comprehensive solution for tracking:
- **Raw Materials** - Track materials, suppliers, and costs
- **Products** - Manage product catalog, costs, and pricing
- **Customers** - Handle retail and wholesale customer information
- **Inventory** - Monitor stock levels across multiple warehouses
- **Sales Orders** - Process customer orders and track sales
- **Shipments** - Manage order fulfillment and shipping
- **Production Orders** - Track manufacturing operations

## Database Schema

The system uses Microsoft SQL Server with the following tables:

| Table | Description |
|-------|-------------|
| `RAW_MATERIALS` | Raw material inventory (steel, plastic, rubber, etc.) |
| `PRODUCTT` | Finished products catalog |
| `PRODUCTION_ORDER` | Manufacturing orders and status |
| `CUSTOMER` | Customer information (Retail/Wholesale) |
| `WAREHOUSE` | Storage facility locations |
| `INVENTORY` | Stock levels by product and warehouse |
| `SALES` | Customer sales transactions |
| `SALES_ORDER_ITEM` | Line items within sales orders |
| `SHIPMENT` | Order shipping details |
| `AUTH` | User authentication and roles |

### Sample Data Included

The database comes pre-populated with Ethiopian companies as sample data:
- **Suppliers**: Messebo Cement Factory, Ethio-Plastics PLC, Addis Rubber Factory
- **Customers**: Ethio Telecom, Dashen Bank, Ethiopian Airlines
- **Warehouses**: Locations across Addis Ababa, Adama, Bahir Dar, Hawassa

## Features

### Core Operations
- ✅ **Create** - Add new materials, products, customers
- ✅ **Read** - View all records with formatted output
- ✅ **Update** - Modify existing entries
- ✅ **Delete** - Remove records (Admin only)

### User Management
- 🔐 **Registration** - Create new user accounts
- 🔑 **Login/Logout** - Secure session management
- 👥 **Role-Based Access** - Admin vs User permissions
- 🔒 **Password Protection** - Basic authentication

### Business Functions
- 📦 Raw material tracking
- 🏭 Production order management
- 📊 Inventory control across warehouses
- 💰 Sales processing
- 🚚 Shipment tracking

## Prerequisites

Before running this application, ensure you have:

1. **Python 3.7+** installed
2. **Microsoft SQL Server** installed (Express edition works)
3. **SQL Server Management Studio (SSMS)** - Optional but recommended
4. **ODBC Driver 17 for SQL Server**

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/mike0192/supply_chain_management_sys_stm.git
cd supply_chain_management_sys_stm
```

### 2. Install Python Dependencies
```bash
pip install pyodbc
```

### 3. Install ODBC Driver
- **Windows**: Download from Microsoft website
- **Linux**: 
  ```bash
  sudo apt-get install odbcinst
  sudo apt-get install msodbcsql17
  ```
- **macOS**:
  ```bash
  brew install msodbcsql17
  ```

## Database Setup

### Step 1: Create Database
Open SSMS or SQLCMD and run:
```sql
CREATE DATABASE SUPPLY_CHAIN;
GO
USE SUPPLY_CHAIN;
GO
```

### Step 2: Run Schema and Sample Data
Execute all the CREATE TABLE and INSERT statements from the provided SQL script in order.

### Step 3: Verify Connection String
The application connects using:
```python
"DRIVER={ODBC Driver 17 for SQL Server};"
"SERVER=.\\SQLEXPRESS;"  # Change if your SQL Server instance is different
"DATABASE=SUPPLY_CHAIN;"
"Trusted_Connection=yes;"
```

**Note**: If using SQL Server Authentication instead of Windows Authentication:
```python
"UID=your_username;"
"PWD=your_password;"
```

## Usage

### Starting the Application
```bash
python main.py
```

### First-Time Login
Since no default admin exists, you'll need to:
1. Temporarily modify the code to bypass authentication, OR
2. Manually insert an admin user directly into the database:
```sql
INSERT INTO AUTH (Username, Password, Role) 
VALUES ('admin', 'admin123', 'Admin');
```

### Main Menu Options

**When Logged Out:**
```
1. Login
2. Register
0. Exit System
```

**When Logged In (User Role):**
```
1. Material Management (View Only)
2. Product Management (View Only)
3. Customer Management (View Only)
4. Logout
0. Exit System
```

**When Logged In (Admin Role):**
```
1. Material Management (Full CRUD)
2. Product Management (Full CRUD)
3. Customer Management (Full CRUD)
4. Logout
5. Register New User
0. Exit System
```

### Example Workflow

1. **Login** with admin credentials
2. **Add a new raw material**:
   - Enter material ID, name, supplier, cost
   - System validates and inserts into database
3. **View all products** to check inventory
4. **Add a new customer** (Retail or Wholesale)
5. **Create a sales order** (requires manual SQL for now)

## Role-Based Access

| Operation | Admin | User |
|-----------|-------|------|
| View Materials | ✅ | ✅ |
| Add Material | ✅ | ❌ |
| Update Material | ✅ | ❌ |
| Delete Material | ✅ | ❌ |
| View Products | ✅ | ✅ |
| Add Product | ✅ | ❌ |
| Update Product | ✅ | ❌ |
| Delete Product | ✅ | ❌ |
| View Customers | ✅ | ✅ |
| Add Customer | ✅ | ❌ |
| Update Customer | ✅ | ❌ |
| Delete Customer | ✅ | ❌ |
| Register Users | ✅ | ❌ |

## System Requirements

- **OS**: Windows/Linux/macOS
- **RAM**: Minimum 2GB (4GB recommended)
- **Disk Space**: 1GB for SQL Server Express + application
- **Python**: 3.7 or higher
- **SQL Server**: 2016 or higher

## Project Structure

```
supply_chain_management_sys_stm/
│
├── main.py                    # Main application file
├── README.md                  # This file
├── database_schema.sql        # SQL schema and sample data
│
└── docs/
    ├── ER_diagram.png        # Database entity relationship diagram
    └── user_guide.pdf        # Detailed user manual
```

## Future Improvements

### Planned Features
- [ ] Password hashing (bcrypt/argon2)
- [ ] Graphical user interface (GUI)
- [ ] Report generation (PDF/Excel)
- [ ] Email notifications for low stock
- [ ] Real-time inventory tracking
- [ ] Barcode scanning integration
- [ ] Dashboard with analytics
- [ ] Export/Import functionality
- [ ] Audit logging for all operations
- [ ] API endpoints for integration

### Known Issues
- Passwords stored in plain text
- No input validation for special characters
- No relationship between materials and products
- Manual SQL required for sales order creation

## Troubleshooting

### Common Errors

**Error: `pyodbc.Error: Data source name not found`**
- Solution: Install ODBC Driver 17 for SQL Server

**Error: `Login failed for user`**
- Solution: Check connection string and authentication method

**Error: `Cannot open database "SUPPLY_CHAIN"`**
- Solution: Create the database first using the SQL script

**Error: `Duplicate key` on INSERT**
- Solution: Check if ID already exists, use different ID

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

**Repository Owner**: Mike0192  
**Project Link**: [https://github.com/mike0192/supply_chain_management_sys_stm](https://github.com/mike0192/supply_chain_management_sys_stm)

## Acknowledgments

- Ethiopian companies for realistic sample data
- Microsoft for SQL Server and ODBC Driver
- Python pyodbc community

---

**⚠️ Security Note**: This is a learning project. For production use, implement proper password hashing, SQL injection prevention, and input validation.

**Version**: 1.0.0  
**Last Updated**: 2025
```

This README provides comprehensive documentation including installation, database setup, usage instructions, and troubleshooting. Save it as `README.md` in your repository root.
