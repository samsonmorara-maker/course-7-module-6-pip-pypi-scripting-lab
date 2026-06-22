from datetime import datetime
import os

def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    with open(filename, "w", encoding="utf-8") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


if __name__ == "__main__":
    logs = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    filename = generate_log(logs)
    print(f"Log written to {filename}")