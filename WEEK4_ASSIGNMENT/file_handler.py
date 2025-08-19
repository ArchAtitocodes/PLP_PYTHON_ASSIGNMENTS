import os
import shutil

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

def write_file(filename, lines):
    try:
        with open(filename, 'w') as file:
            file.writelines(lines)
        print(f"Modified content written to '{filename}'.")
    except PermissionError:
        print(f"Error: Permission denied when trying to write to '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while writing: {e}")

def backup_file(original_filename):
    backup_filename = original_filename + ".backup"
    try:
        shutil.copy(original_filename, backup_filename)
        print(f"Backup created: '{backup_filename}'")
    except Exception as e:
        print(f"Backup failed: {e}")

def modify_uppercase(lines):
    return [line.upper() for line in lines]

def modify_line_numbers(lines):
    return [f"{i}: {line}" for i, line in enumerate(lines, 1)]

def modify_replace_word(lines):
    old_word = input("Enter the word to replace: ")
    new_word = input("Enter the replacement word: ")
    return [line.replace(old_word, new_word) for line in lines]

def display_menu():
    print("\nChoose a modification option:")
    print("1. Convert text to UPPERCASE")
    print("2. Add line numbers")
    print("3. Replace a word")
    print("4. Backup original file before writing new content")
    print("5. Done selecting options")

def main():
    input_filename = input("Enter the filename to read: ").strip()
    lines = read_file(input_filename)
    if lines is None:
        return

    modified_lines = lines[:]
    selected_options = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            modified_lines = modify_uppercase(modified_lines)
            selected_options.append("UPPERCASE")
        elif choice == '2':
            modified_lines = modify_line_numbers(modified_lines)
            selected_options.append("Line Numbers")
        elif choice == '3':
            modified_lines = modify_replace_word(modified_lines)
            selected_options.append("Replace Word")
        elif choice == '4':
            backup_file(input_filename)
            selected_options.append("Backup")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

    output_filename = input("Enter output filename (e.g., output.txt): ").strip()
    write_file(output_filename, modified_lines)

    print("\nModifications applied:", ', '.join(selected_options) if selected_options else "None")
    print("Program finished successfully.")

if __name__ == "__main__":
    main()
