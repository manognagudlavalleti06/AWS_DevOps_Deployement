import sys
from datetime import datetime


def main():
    print("===================================")
    print("AWS Glue Python Shell Job Started")
    print("===================================")

    print(f"Job execution time: {datetime.now()}")

    # Sample data
    data = [
        {"id": 1, "name": "Manu", "department": "IT"},
        {"id": 2, "name": "Rahul", "department": "CSE"},
        {"id": 3, "name": "Priya", "department": "ECE"}
    ]

    print("\nInput Data:")
    for record in data:
        print(record)

    # Simple transformation
    transformed_data = []

    for record in data:
        transformed_record = {
            "id": record["id"],
            "name": record["name"].upper(),
            "department": record["department"]
        }

        transformed_data.append(transformed_record)

    print("\nTransformed Data:")
    for record in transformed_data:
        print(record)

    print("\n===================================")
    print("AWS Glue Python Shell Job Completed")
    print("===================================")


if __name__ == "__main__":
    main()