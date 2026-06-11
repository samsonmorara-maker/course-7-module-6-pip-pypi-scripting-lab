from datetime import datetime
import os

def generate_log(data):
    # Validate input
    if not isinstance(data, list):
        raise ValueError("data must be a list")
    
    # Generate filename with today's date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    
    # Write log entries to file
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")
    
    # Print confirmation
    print(f"Log written to {filename}")
    
    return filename  # ← CRITICAL


if __name__ == "__main__":
    log_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]
    generate_log(log_data)