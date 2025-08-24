# -------------------------------------------------------------------------
# Cyberbullying Complaint System
# CBSE Class 12 Computer Science Project (Python + MySQL)
# -------------------------------------------------------------------------
# Database: ekaksh
# User: root
# Password: 12345678
# Table: complaints
#
# Project Features:
# 1. Students can anonymously report cases of online bullying.
# 2. Admin can login with a password and access a dashboard.
# 3. Admin can view all complaints, update their status, or delete them.
# 4. Complaint data is stored in MySQL.
# -------------------------------------------------------------------------
import mysql.connector       # To connect Python with MySQL
import datetime              # To get the current date for complaints

# -------------------------------------------------------------------------
# FUNCTION: connect_db
# Purpose : Establishes connection with MySQL database "ekaksh"
# -------------------------------------------------------------------------
def connect_db():
    """Connect to the MySQL database and return connection object"""
    return mysql.connector.connect(
        host="localhost",        # MySQL server is running locally
        user="root",             # Username
        password="12345678",     # Password
        database="ekaksh"        # Database name
    )

# -------------------------------------------------------------------------
# FUNCTION: report_complaint
# Purpose : Allows students to anonymously report a complaint
# -------------------------------------------------------------------------
def report_complaint():
    """Function for students to file cyberbullying complaints anonymously"""

    # Establish database connection
    conn = connect_db()
    cur = conn.cursor()

    print("\n=====================================================")
    print("                 REPORT CYBERBULLYING                ")
    print("=====================================================")

    # Take inputs from student (anonymously)
    platform = input("Enter Platform (Instagram / WhatsApp / Facebook / Other): ")
    bullying_type = input("Enter Type of Bullying (Harassment / Threat / Fake News / Other): ")
    details = input("Enter Complaint Details (describe incident briefly): ")

    # Auto-generate today's date
    date_today = datetime.date.today()

    # SQL Query to insert complaint
    query = """
        INSERT INTO complaints(date, platform, bullying_type, details, status)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (date_today, platform, bullying_type, details, "Pending")

    # Execute and commit changes
    cur.execute(query, values)
    conn.commit()

    print("\n✅ Complaint Submitted Successfully!")
    print("   Your identity remains anonymous.")
    print("   The admin team will review and take action.\n")

    # Close connection
    cur.close()
    conn.close()

# -------------------------------------------------------------------------
# FUNCTION: admin_login
# Purpose : Authenticate admin using a hardcoded password
# -------------------------------------------------------------------------
def admin_login():
    """Function to authenticate the admin"""
    print("\n=====================================================")
    print("                   ADMIN LOGIN                       ")
    print("=====================================================")
    password = input("Enter Admin Password: ")

    # Hardcoded password for simplicity
    if password == "admin123":
        print("✅ Login Successful! Welcome Admin.")
        admin_menu()   # Show admin dashboard
    else:
        print("❌ Incorrect Password. Access Denied.")

# -------------------------------------------------------------------------
# FUNCTION: admin_menu
# Purpose : Displays admin dashboard menu with options
# -------------------------------------------------------------------------
def admin_menu():
    """Menu for admin after successful login"""
    while True:
        print("\n=====================================================")
        print("                 ADMIN DASHBOARD                     ")
        print("=====================================================")
        print("1. View All Complaints")
        print("2. Update Complaint Status")
        print("3. Delete a Complaint")
        print("4. Logout")
        print("=====================================================")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            view_complaints()
        elif choice == "2":
            update_status()
        elif choice == "3":
            delete_complaint()
        elif choice == "4":
            print("Logging out... Returning to Main Menu.")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# -------------------------------------------------------------------------
# FUNCTION: view_complaints
# Purpose : Display all complaints stored in database
# -------------------------------------------------------------------------
def view_complaints():
    """Function to display all complaints for the admin"""

    conn = connect_db()
    cur = conn.cursor()

    # SQL query to fetch all complaints
    query = "SELECT * FROM complaints"
    cur.execute(query)
    records = cur.fetchall()

    print("\n=====================================================")
    print("                  ALL COMPLAINTS                     ")
    print("=====================================================")

    if len(records) == 0:
        print("No complaints found.")
    else:
        for row in records:
            print("\n-----------------------------------")
            print(f"Complaint ID : {row[0]}")
            print(f"Date         : {row[1]}")
            print(f"Platform     : {row[2]}")
            print(f"Type         : {row[3]}")
            print(f"Details      : {row[4]}")
            print(f"Status       : {row[5]}")
            print("-----------------------------------")

    cur.close()
    conn.close()

# -------------------------------------------------------------------------
# FUNCTION: update_status
# Purpose : Admin can update the status of a complaint
# -------------------------------------------------------------------------
def update_status():
    """Function to update complaint status"""

    conn = connect_db()
    cur = conn.cursor()

    # Show all complaints before updating
    view_complaints()
    cid = input("\nEnter Complaint ID to update status: ")

    print("\nSelect New Status:")
    print("1. Pending")
    print("2. In Progress")
    print("3. Resolved")

    choice = input("Enter choice (1-3): ")

    # Map choices to statuses
    status_map = {"1": "Pending", "2": "In Progress", "3": "Resolved"}

    if choice not in status_map:
        print("❌ Invalid choice. Status not updated.")
    else:
        new_status = status_map[choice]
        query = "UPDATE complaints SET status=%s WHERE id=%s"
        cur.execute(query, (new_status, cid))
        conn.commit()
        print(f"✅ Complaint ID {cid} status updated to {new_status}")

    cur.close()
    conn.close()

# -------------------------------------------------------------------------
# FUNCTION: delete_complaint
# Purpose : Admin can delete a complaint (if invalid)
# -------------------------------------------------------------------------
def delete_complaint():
    """Function to delete a complaint"""

    conn = connect_db()
    cur = conn.cursor()

    # Show all complaints before deletion
    view_complaints()
    cid = input("\nEnter Complaint ID to delete: ")

    query = "DELETE FROM complaints WHERE id=%s"
    cur.execute(query, (cid,))
    conn.commit()

    if cur.rowcount > 0:
        print(f"✅ Complaint ID {cid} deleted successfully.")
    else:
        print("❌ Complaint ID not found.")

    cur.close()
    conn.close()

# -------------------------------------------------------------------------
# FUNCTION: main_menu
# Purpose : Entry point of the program (Student/Admin selection)
# -------------------------------------------------------------------------
def main_menu():
    """Main menu shown to every user at start"""

    while True:
        print("\n=====================================================")
        print("        WELCOME TO CYBERBULLYING COMPLAINT SYSTEM    ")
        print("=====================================================")
        print("1. Report Cyberbullying (Student)")
        print("2. Admin Login")
        print("3. Exit")
        print("=====================================================")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            report_complaint()
        elif choice == "2":
            admin_login()
        elif choice == "3":
            print("\nExiting program... Goodbye!")
            print("=====================================================")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# -------------------------------------------------------------------------
# PROGRAM EXECUTION STARTS HERE
# -------------------------------------------------------------------------
main_menu()
