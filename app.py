from flask import Flask, render_template, request, redirect, url_for, flash
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "kuunal-secret-key")


# Azure SQL Database connection
def get_db_connection():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_USERNAME")
    password = os.getenv("DB_PASSWORD")

    connection_string = (
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )

    return pyodbc.connect(connection_string)


# READ - Display all employees
@app.route("/")
def index():
    search = request.args.get("search", "").strip()

    connection = get_db_connection()
    cursor = connection.cursor()

    if search:
        query = """
            SELECT EmployeeID, EmployeeName, Email,
                   Department, Designation, Salary
            FROM Employee
            WHERE EmployeeName LIKE ?
               OR Department LIKE ?
               OR Designation LIKE ?
               OR Email LIKE ?
            ORDER BY EmployeeID
        """

        search_value = f"%{search}%"

        cursor.execute(
            query,
            search_value,
            search_value,
            search_value,
            search_value
        )
    else:
        cursor.execute("""
            SELECT EmployeeID, EmployeeName, Email,
                   Department, Designation, Salary
            FROM Employee
            ORDER BY EmployeeID
        """)

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return render_template(
        "index.html",
        employees=employees,
        search=search
    )


# CREATE - Add employee
@app.route("/add", methods=["GET", "POST"])
def add_employee():

    if request.method == "POST":
        employee_id = request.form["employee_id"]
        employee_name = request.form["employee_name"].strip()
        email = request.form["email"].strip()
        department = request.form["department"].strip()
        designation = request.form["designation"].strip()
        salary = request.form["salary"]

        if not all([
            employee_id,
            employee_name,
            email,
            department,
            designation,
            salary
        ]):
            flash("All fields are required.", "danger")
            return redirect(url_for("add_employee"))

        try:
            connection = get_db_connection()
            cursor = connection.cursor()

            cursor.execute("""
                INSERT INTO Employee
                (EmployeeID, EmployeeName, Email,
                 Department, Designation, Salary)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
            employee_id,
            employee_name,
            email,
            department,
            designation,
            salary)

            connection.commit()

            cursor.close()
            connection.close()

            flash("Employee added successfully!", "success")
            return redirect(url_for("index"))

        except Exception as e:
            flash(f"Error adding employee: {str(e)}", "danger")
            return redirect(url_for("add_employee"))

    return render_template("add_employee.html")


# UPDATE - Edit employee
@app.route("/edit/<int:employee_id>", methods=["GET", "POST"])
def edit_employee(employee_id):

    connection = get_db_connection()
    cursor = connection.cursor()

    if request.method == "POST":
        employee_name = request.form["employee_name"].strip()
        email = request.form["email"].strip()
        department = request.form["department"].strip()
        designation = request.form["designation"].strip()
        salary = request.form["salary"]

        if not all([
            employee_name,
            email,
            department,
            designation,
            salary
        ]):
            flash("All fields are required.", "danger")
            return redirect(
                url_for("edit_employee", employee_id=employee_id)
            )

        try:
            cursor.execute("""
                UPDATE Employee
                SET EmployeeName = ?,
                    Email = ?,
                    Department = ?,
                    Designation = ?,
                    Salary = ?
                WHERE EmployeeID = ?
            """,
            employee_name,
            email,
            department,
            designation,
            salary,
            employee_id)

            connection.commit()

            flash("Employee updated successfully!", "success")

        except Exception as e:
            connection.rollback()
            flash(f"Error updating employee: {str(e)}", "danger")

        finally:
            cursor.close()
            connection.close()

        return redirect(url_for("index"))

    cursor.execute("""
        SELECT EmployeeID, EmployeeName, Email,
               Department, Designation, Salary
        FROM Employee
        WHERE EmployeeID = ?
    """, employee_id)

    employee = cursor.fetchone()

    cursor.close()
    connection.close()

    if employee is None:
        flash("Employee not found.", "danger")
        return redirect(url_for("index"))

    return render_template(
        "edit_employee.html",
        employee=employee
    )


# DELETE - Remove employee
@app.route("/delete/<int:employee_id>", methods=["POST"])
def delete_employee(employee_id):

    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM Employee WHERE EmployeeID = ?",
            employee_id
        )

        connection.commit()

        cursor.close()
        connection.close()

        flash("Employee deleted successfully!", "success")

    except Exception as e:
        flash(f"Error deleting employee: {str(e)}", "danger")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)