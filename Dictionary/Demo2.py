# Creating a dictionary
if __name__=='__main__':
    student = {
        "name": "Aanya",
        "age": 20,
        "courses": ["Math", "Computer Science"]
    }

    # Accessing values
    print(student["name"])         # Output: Aanya

    # Adding a new key-value pair
    student["grade"] = "A"

    # Updating an existing value
    student["age"] = 21

    # Deleting a key-value pair
    del student["courses"]

    # Iterating through the dictionary
    for key, value in student.items():
        print(f"{key}: {value}")
