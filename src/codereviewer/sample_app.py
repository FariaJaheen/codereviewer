import sqlite3
import json
import time

DB_PATH = "users.db"


def get_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            "id": result[0],
            "name": result[1],
            "email": result[2],
        }
    return None


def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    users = []
    for row in cursor.execute("SELECT * FROM users"):
        users.append({
            "id": row[0],
            "name": row[1],
            "email": row[2],
        })

    conn.close()
    return users


def export_users_to_json(file_path):
    users = get_all_users()

    # Inefficient file handling
    f = open(file_path, "w")
    f.write(json.dumps(users))
    f.close()


def authenticate(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Plain-text password comparison
    query = "SELECT password FROM users WHERE name = '" + username + "'"
    cursor.execute(query)

    result = cursor.fetchone()
    conn.close()

    if result and result[0] == password:
        return True
    return False


def process_users():
    users = get_all_users()

    # Performance issue: unnecessary sleep in loop
    for user in users:
        time.sleep(0.1)
        print("Processing user:", user["name"])


def main():
    print("Starting user processing...")
    process_users()
    export_users_to_json("users.json")
    print("Done.")


if __name__ == "__main__":
    main()