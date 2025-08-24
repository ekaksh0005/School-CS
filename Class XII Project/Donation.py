"""
==========================================================
                DIGITAL DONATION TRACKER
        CBSE Class 12 (Python + MySQL) Project
        - No classes (functions only)
        - Separate Donor / NGO / Admin menus
        - 300+ lines, heavy comments for viva
        - Uses proper SQL with mysql-connector
==========================================================
"""

# ==========================
# SECTION 0: IMPORTS
# ==========================
import mysql.connector
from mysql.connector import Error
from datetime import datetime
import getpass
import sys
import re
import time

# ==========================
# SECTION 1: CONFIG & GLOBALS
# ==========================
DB_HOST = "localhost"
DB_USER = "root"          # <-- change if needed
DB_PASS = "12345678"              # <-- put your MySQL password
DB_NAME = "donation_system"

# A simple, human-readable admin password for viva
ADMIN_PASSWORD = "admin123"   # You can change this

ITEM_TYPES = ("Food", "Clothes", "Money")
URGENCY_LEVELS = ("Low", "Medium", "High")

# ==========================
# SECTION 2: DB CONNECTION & SETUP HELPERS
# ==========================

def get_connection(db_name=None):
    """
    Returns a MySQL connection. If db_name is None, connects without selecting DB.
    """
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=db_name if db_name else None
        )
        return conn
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None


def init_database_and_tables():
    """
    Creates the database and required tables if they don't exist.
    Using the exact schema we shared in part (A).
    """
    # 1) Create DB if not exists
    conn = get_connection()
    if not conn:
        print("Cannot connect to MySQL. Check credentials/installation.")
        sys.exit(1)

    try:
        cur = conn.cursor()
        cur.execute("CREATE DATABASE IF NOT EXISTS donation_system;")
        cur.close()
        conn.close()
    except Error as e:
        print("Error creating database:", e)
        sys.exit(1)

    # 2) Create tables
    conn = get_connection(DB_NAME)
    if not conn:
        print("Cannot connect to the donation_system database.")
        sys.exit(1)

    create_sql = [
        """
        CREATE TABLE IF NOT EXISTS donors (
            donor_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(15),
            password VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ngos (
            ngo_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            phone VARCHAR(15),
            password VARCHAR(100) NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS donations (
            donation_id INT AUTO_INCREMENT PRIMARY KEY,
            donor_id INT NOT NULL,
            item_type ENUM('Food','Clothes','Money') NOT NULL,
            quantity INT NOT NULL CHECK (quantity >= 0),
            date_of_donation DATE NOT NULL,
            remarks VARCHAR(255),
            FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS requests (
            request_id INT AUTO_INCREMENT PRIMARY KEY,
            ngo_id INT NOT NULL,
            item_type ENUM('Food','Clothes','Money') NOT NULL,
            quantity INT NOT NULL CHECK (quantity >= 0),
            date_of_request DATE NOT NULL,
            urgency ENUM('Low','Medium','High') DEFAULT 'Low',
            notes VARCHAR(255),
            FOREIGN KEY (ngo_id) REFERENCES ngos(ngo_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        );
        """
    ]

    try:
        cur = conn.cursor()
        for sql in create_sql:
            cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()
    except Error as e:
        print("Error creating tables:", e)
        sys.exit(1)

# ==========================
# SECTION 3: COMMON UTILS (VALIDATION, INPUT)
# ==========================

def pause():
    input("\nPress ENTER to continue...")

def valid_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email))

def choose_item_type():
    print("\nSelect item type:")
    for i, t in enumerate(ITEM_TYPES, 1):
        print(f"{i}. {t}")
    while True:
        try:
            ch = int(input("Enter choice (1-3): ").strip())
            if ch in (1, 2, 3):
                return ITEM_TYPES[ch-1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number 1-3.")

def choose_urgency():
    print("\nSelect urgency:")
    for i, u in enumerate(URGENCY_LEVELS, 1):
        print(f"{i}. {u}")
    while True:
        try:
            ch = int(input("Enter choice (1-3): ").strip())
            if ch in (1, 2, 3):
                return URGENCY_LEVELS[ch-1]
            else:
                print("Invalid choice.")
        except ValueError:
            print("Enter a number 1-3.")

def input_quantity():
    while True:
        try:
            q = int(input("Enter quantity/amount (integer): ").strip())
            if q >= 0:
                return q
            print("Quantity cannot be negative.")
        except ValueError:
            print("Please enter a valid integer.")

def today_date_str():
    return datetime.now().strftime("%Y-%m-%d")

# ==========================
# SECTION 4: DONOR FUNCTIONS
# ==========================

def donor_register():
    """
    Registers a new donor.
    """
    print("\n--- Donor Registration ---")
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    if not valid_email(email):
        print("Invalid email format.")
        return
    phone = input("Phone: ").strip()
    password = getpass.getpass("Create password: ")

    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO donors(name, email, phone, password) VALUES (%s,%s,%s,%s)",
            (name, email, phone, password)
        )
        conn.commit()
        print("Donor registered successfully.")
    except Error as e:
        if "Duplicate entry" in str(e):
            print("Email already registered. Try another email.")
        else:
            print("Error:", e)
    finally:
        cur.close()
        conn.close()


def donor_login():
    """
    Logs in a donor by email + password.
    Returns donor_id if success else None.
    """
    print("\n--- Donor Login ---")
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")

    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT donor_id, name FROM donors WHERE email=%s AND password=%s",
            (email, password)
        )
        row = cur.fetchone()
        if row:
            donor_id, name = row
            print(f"Welcome, {name} (Donor ID: {donor_id})")
            return donor_id
        else:
            print("Invalid credentials.")
            return None
    except Error as e:
        print("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()


def donor_add_donation(donor_id):
    """
    Donor adds a donation with item_type, quantity, date (today), remarks.
    """
    print("\n--- Add Donation ---")
    item_type = choose_item_type()
    quantity = input_quantity()
    remarks = input("Remarks (optional): ").strip()
    date_str = today_date_str()

    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO donations(donor_id, item_type, quantity, date_of_donation, remarks)
               VALUES (%s,%s,%s,%s,%s)""",
            (donor_id, item_type, quantity, date_str, remarks)
        )
        conn.commit()
        print("Donation recorded successfully.")
    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def donor_view_history(donor_id):
    """
    Shows all donations by this donor (latest first).
    """
    print("\n--- My Donation History ---")
    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT donation_id, item_type, quantity, date_of_donation, IFNULL(remarks,'')
               FROM donations
               WHERE donor_id=%s
               ORDER BY date_of_donation DESC, donation_id DESC""",
            (donor_id,)
        )
        rows = cur.fetchall()
        if not rows:
            print("No donations yet.")
        else:
            print(f"{'ID':<6}{'Type':<10}{'Qty':<8}{'Date':<12}Remarks")
            print("-"*60)
            for r in rows:
                print(f"{r[0]:<6}{r[1]:<10}{r[2]:<8}{str(r[3]):<12}{r[4]}")
    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# ==========================
# SECTION 5: NGO FUNCTIONS
# ==========================

def ngo_register():
    print("\n--- NGO Registration ---")
    name = input("NGO Name: ").strip()
    email = input("Email: ").strip()
    if not valid_email(email):
        print("Invalid email format.")
        return
    phone = input("Phone: ").strip()
    password = getpass.getpass("Create password: ")

    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO ngos(name, email, phone, password) VALUES (%s,%s,%s,%s)",
            (name, email, phone, password)
        )
        conn.commit()
        print("NGO registered successfully.")
    except Error as e:
        if "Duplicate entry" in str(e):
            print("Email already registered for an NGO.")
        else:
            print("Error:", e)
    finally:
        cur.close()
        conn.close()


def ngo_login():
    print("\n--- NGO Login ---")
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")

    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT ngo_id, name FROM ngos WHERE email=%s AND password=%s",
            (email, password)
        )
        row = cur.fetchone()
        if row:
            ngo_id, name = row
            print(f"Welcome, {name} (NGO ID: {ngo_id})")
            return ngo_id
        else:
            print("Invalid credentials.")
            return None
    except Error as e:
        print("Error:", e)
        return None
    finally:
        cur.close()
        conn.close()


def ngo_add_request(ngo_id):
    print("\n--- Add Request ---")
    item_type = choose_item_type()
    quantity = input_quantity()
    urgency = choose_urgency()
    notes = input("Notes (optional): ").strip()
    date_str = today_date_str()

    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO requests(ngo_id, item_type, quantity, date_of_request, urgency, notes)
               VALUES (%s,%s,%s,%s,%s,%s)""",
            (ngo_id, item_type, quantity, date_str, urgency, notes)
        )
        conn.commit()
        print("Request added successfully.")
    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def ngo_view_my_requests(ngo_id):
    print("\n--- My NGO Requests ---")
    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        cur.execute(
            """SELECT request_id, item_type, quantity, date_of_request, urgency, IFNULL(notes,'')
               FROM requests
               WHERE ngo_id=%s
               ORDER BY date_of_request DESC, request_id DESC""",
            (ngo_id,)
        )
        rows = cur.fetchall()
        if not rows:
            print("No requests yet.")
        else:
            print(f"{'ID':<6}{'Type':<10}{'Qty':<8}{'Date':<12}{'Urgency':<8}Notes")
            print("-"*70)
            for r in rows:
                print(f"{r[0]:<6}{r[1]:<10}{r[2]:<8}{str(r[3]):<12}{r[4]:<8}{r[5]}")
    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# ==========================
# SECTION 6: ADMIN / REPORTS
# ==========================

def admin_login():
    print("\n--- Admin Login ---")
    # For viva simplicity, using a fixed password variable
    pwd = getpass.getpass("Enter admin password: ")
    if pwd == ADMIN_PASSWORD:
        print("Admin login successful.")
        return True
    print("Incorrect admin password.")
    return False


def admin_view_all(table_name):
    """
    Generic viewer for donors/ngos/donations/requests
    to keep code compact but still readable for viva.
    """
    print(f"\n--- Admin: View All {table_name.capitalize()} ---")
    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()
        if table_name == "donors":
            cur.execute("SELECT donor_id, name, email, phone FROM donors ORDER BY donor_id;")
            rows = cur.fetchall()
            print(f"{'ID':<6}{'Name':<20}{'Email':<28}{'Phone'}")
            print("-"*70)
            for r in rows:
                print(f"{r[0]:<6}{r[1]:<20}{r[2]:<28}{r[3]}")
        elif table_name == "ngos":
            cur.execute("SELECT ngo_id, name, email, phone FROM ngos ORDER BY ngo_id;")
            rows = cur.fetchall()
            print(f"{'ID':<6}{'Name':<20}{'Email':<28}{'Phone'}")
            print("-"*70)
            for r in rows:
                print(f"{r[0]:<6}{r[1]:<20}{r[2]:<28}{r[3]}")
        elif table_name == "donations":
            cur.execute("""SELECT d.donation_id, dn.name, d.item_type, d.quantity, d.date_of_donation, IFNULL(d.remarks,'')
                           FROM donations d JOIN donors dn ON d.donor_id = dn.donor_id
                           ORDER BY d.date_of_donation DESC, d.donation_id DESC;""")
            rows = cur.fetchall()
            print(f"{'ID':<6}{'Donor':<20}{'Type':<10}{'Qty':<8}{'Date':<12}Remarks")
            print("-"*80)
            for r in rows:
                print(f"{r[0]:<6}{r[1]:<20}{r[2]:<10}{r[3]:<8}{str(r[4]):<12}{r[5]}")
        elif table_name == "requests":
            cur.execute("""SELECT r.request_id, ng.name, r.item_type, r.quantity, r.date_of_request, r.urgency, IFNULL(r.notes,'')
                           FROM requests r JOIN ngos ng ON r.ngo_id = ng.ngo_id
                           ORDER BY r.date_of_request DESC, r.request_id DESC;""")
            rows = cur.fetchall()
            print(f"{'ID':<6}{'NGO':<20}{'Type':<10}{'Qty':<8}{'Date':<12}{'Urg':<6}Notes")
            print("-"*90)
            for r in rows:
                print(f"{r[0]:<6}{r[1]:<20}{r[2]:<10}{r[3]:<8}{str(r[4]):<12}{r[5]:<6}{r[6]}")
        else:
            print("Unknown table.")
    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def admin_match_donations_requests():
    """
    Simple matching: For each request, show available donations of same type
    and quantities that can cover fully/partially.
    (We are not auto-allocating; just presenting matches for viva clarity.)
    """
    print("\n--- Admin: Match Donations ↔ Requests ---")
    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor(dictionary=True)

        # 1) Fetch open requests (all requests)
        cur.execute("""SELECT r.request_id, ng.name AS ngo_name, r.item_type, r.quantity, 
                              r.date_of_request, r.urgency
                       FROM requests r
                       JOIN ngos ng ON r.ngo_id = ng.ngo_id
                       ORDER BY r.urgency DESC, r.date_of_request ASC;""")
        requests = cur.fetchall()

        # 2) Fetch donations grouped by item_type (available = all donations)
        cur.execute("""SELECT d.donation_id, dn.name AS donor_name, d.item_type, 
                              d.quantity, d.date_of_donation
                       FROM donations d 
                       JOIN donors dn ON d.donor_id = dn.donor_id
                       ORDER BY d.date_of_donation ASC;""")
        donations = cur.fetchall()

        if not requests:
            print("No requests found.")
            return
        if not donations:
            print("No donations found.")
            return

        # Convert donations by type for quick lookup
        dons_by_type = {"Food": [], "Clothes": [], "Money": []}
        for d in donations:
            dons_by_type[d["item_type"]].append(d)

        # For each request, find donation candidates
        for req in requests:
            print("\n---------------------------------------------------------------")
            print(f"Request #{req['request_id']} | NGO: {req['ngo_name']} | "
                  f"Type: {req['item_type']} | Qty: {req['quantity']} | "
                  f"Urgency: {req['urgency']} | Date: {req['date_of_request']}")
            print("Potential donation matches:")

            candidates = [d for d in dons_by_type.get(req["item_type"], []) if d["quantity"] > 0]
            if not candidates:
                print("  - No donations of this type yet.")
                continue

            # Show top candidates that can cover fully or partially
            displayed = 0
            for d in candidates:
                status = "FULL COVER" if d["quantity"] >= req["quantity"] else "PARTIAL"
                print(f"  - Donation #{d['donation_id']} | Donor: {d['donor_name']} | "
                      f"Qty: {d['quantity']} | Date: {d['date_of_donation']} | {status}")
                displayed += 1
                if displayed >= 10:
                    print("  ...showing first 10 matches only.")
                    break

        print("\nNOTE: This is a viewing tool. Allocation/updation can be added if needed.")
    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


def admin_reports():
    """
    Generates simple numeric reports:
    - Total donors, NGOs
    - Donations count and sum by type
    - Requests count by type and urgency
    - Top 5 donors by total donated quantity
    """
    print("\n--- Admin: Reports Dashboard ---")
    conn = get_connection(DB_NAME)
    try:
        cur = conn.cursor()

        # Total donors, NGOs
        cur.execute("SELECT COUNT(*) FROM donors;")
        total_donors = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM ngos;")
        total_ngos = cur.fetchone()[0]

        print(f"Total Donors: {total_donors} | Total NGOs: {total_ngos}")

        # Donations by type
        print("\nDonations by Type (count, total quantity):")
        cur.execute("""SELECT item_type, COUNT(*), COALESCE(SUM(quantity),0)
                       FROM donations GROUP BY item_type;""")
        rows = cur.fetchall()
        if rows:
            for r in rows:
                print(f"  - {r[0]} -> Count: {r[1]}, Total Qty/Amount: {r[2]}")
        else:
            print("  No donations recorded yet.")

        # Requests by type
        print("\nRequests by Type (count, total quantity):")
        cur.execute("""SELECT item_type, COUNT(*), COALESCE(SUM(quantity),0)
                       FROM requests GROUP BY item_type;""")
        rows = cur.fetchall()
        if rows:
            for r in rows:
                print(f"  - {r[0]} -> Count: {r[1]}, Total Qty/Amount: {r[2]}")
        else:
            print("  No requests recorded yet.")

        # Requests by urgency
        print("\nRequests by Urgency (count):")
        cur.execute("""SELECT urgency, COUNT(*) FROM requests GROUP BY urgency
                       ORDER BY FIELD(urgency,'High','Medium','Low');""")
        rows = cur.fetchall()
        if rows:
            for r in rows:
                print(f"  - {r[0]}: {r[1]}")
        else:
            print("  No requests recorded yet.")

        # Top 5 donors by total quantity
        print("\nTop 5 Donors by Total Quantity/Amount Donated:")
        cur.execute("""SELECT dn.name, COALESCE(SUM(d.quantity),0) AS total_q
                       FROM donors dn LEFT JOIN donations d ON dn.donor_id = d.donor_id
                       GROUP BY dn.donor_id, dn.name
                       ORDER BY total_q DESC
                       LIMIT 5;""")
        rows = cur.fetchall()
        if rows:
            rank = 1
            for r in rows:
                print(f"  {rank}. {r[0]} -> {r[1]}")
                rank += 1
        else:
            print("  No donors found.")

    except Error as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()

# ==========================
# SECTION 7: MENUS
# ==========================

def donor_menu():
    while True:
        print("\n========== DONOR MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. Back to Main Menu")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            donor_register()
            pause()
        elif ch == "2":
            donor_id = donor_login()
            if donor_id:
                donor_logged_in_menu(donor_id)
            pause()
        elif ch == "3":
            return
        else:
            print("Invalid choice. Try again.")


def donor_logged_in_menu(donor_id):
    while True:
        print("\n------ Donor Actions ------")
        print("1. Add Donation")
        print("2. View My Donation History")
        print("3. Logout")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            donor_add_donation(donor_id)
            pause()
        elif ch == "2":
            donor_view_history(donor_id)
            pause()
        elif ch == "3":
            print("Logging out...")
            time.sleep(0.6)
            return
        else:
            print("Invalid choice.")


def ngo_menu():
    while True:
        print("\n========== NGO MENU ==========")
        print("1. Register")
        print("2. Login")
        print("3. Back to Main Menu")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            ngo_register()
            pause()
        elif ch == "2":
            ngo_id = ngo_login()
            if ngo_id:
                ngo_logged_in_menu(ngo_id)
            pause()
        elif ch == "3":
            return
        else:
            print("Invalid choice. Try again.")


def ngo_logged_in_menu(ngo_id):
    while True:
        print("\n------ NGO Actions ------")
        print("1. Add Request")
        print("2. View My Requests")
        print("3. Logout")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            ngo_add_request(ngo_id)
            pause()
        elif ch == "2":
            ngo_view_my_requests(ngo_id)
            pause()
        elif ch == "3":
            print("Logging out...")
            time.sleep(0.6)
            return
        else:
            print("Invalid choice.")


def admin_menu():
    if not admin_login():
        pause()
        return
    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. View All Donors")
        print("2. View All NGOs")
        print("3. View All Donations")
        print("4. View All Requests")
        print("5. Match Donations ↔ Requests")
        print("6. Reports Dashboard")
        print("7. Back to Main Menu")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            admin_view_all("donors")
            pause()
        elif ch == "2":
            admin_view_all("ngos")
            pause()
        elif ch == "3":
            admin_view_all("donations")
            pause()
        elif ch == "4":
            admin_view_all("requests")
            pause()
        elif ch == "5":
            admin_match_donations_requests()
            pause()
        elif ch == "6":
            admin_reports()
            pause()
        elif ch == "7":
            return
        else:
            print("Invalid choice. Try again.")

# ==========================
# SECTION 8: MAIN LOOP
# ==========================

def main():
    print("Initializing database & tables (if needed)...")
    init_database_and_tables()

    while True:
        print("\n================= DIGITAL DONATION TRACKER =================")
        print("1. Donor")
        print("2. NGO")
        print("3. Admin")
        print("4. Exit")
        ch = input("Enter choice: ").strip()
        if ch == "1":
            donor_menu()
        elif ch == "2":
            ngo_menu()
        elif ch == "3":
            admin_menu()
        elif ch == "4":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

# Entry Point
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
