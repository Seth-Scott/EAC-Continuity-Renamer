import os
import re

# Function to get the starting number from the user
def get_starting_number():
    while True:
        try:
            starting_number = int(input("What number should we start with?: "))
            return starting_number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Custom sorting function to handle numerical ordering
def custom_sort(filename):
    return [int(x) if x.isdigit() else x for x in re.split('(\d+)', filename)]

# Main function
if __name__ == "__main__":
    input_folder = "files"
    output_folder = "renamed"
    
    # Check if the 'renamed' folder exists, and create it if it doesn't
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    starting_number = get_starting_number()
    
    # Check if the 'files' folder exists
    if not os.path.exists(input_folder):
        print(f"Folder '{input_folder}' does not exist.")
    else:
        # List the files in the 'files' folder and sort them using the custom_sort function
        files_to_rename = [filename for filename in os.listdir(input_folder) if filename.endswith(".wav")]
        files_to_rename.sort(key=custom_sort)
        
        # Open a log file for writing
        log_file_path = os.path.join(os.path.dirname(__file__), "rename_log.txt")
        with open(log_file_path, "w") as log_file:
            for filename in files_to_rename:
                old_number = filename.split(" ")[0]  # Extract the existing number
                new_filename = f"{starting_number} {filename.split(' ', 1)[1]}"  # Keep the rest of the filename the same
                new_filepath = os.path.join(output_folder, new_filename)
                
                try:
                    # Rename the file in the 'renamed' folder
                    os.rename(os.path.join(input_folder, filename), new_filepath)
                    
                    # Log the renaming information
                    log_file.write(f"{filename} > {new_filename}\n")
                    
                    starting_number += 1
                except OSError as e:
                    print(f"Error renaming '{filename}': {str(e)}")
                    
        print("Files renamed and log file generated successfully.")
