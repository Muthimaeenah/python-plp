def modify_content(content):
    """Modify file content (example: convert to uppercase)."""
    return content.upper()

# Ask the user for a filename
filename = input("Enter the filename to read: ")

try:
    # Try to open and read the file
    with open(filename, "r") as file:
        content = file.read()

    # Modify content
    modified_content = modify_content(content)

    # Write to a new file
    new_filename = "modified_output.txt"
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content written to '{new_filename}' successfully! ✅")

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again. ❌")

except IOError:
    print("Error: Unable to read the file. Please check permissions. ❌")
