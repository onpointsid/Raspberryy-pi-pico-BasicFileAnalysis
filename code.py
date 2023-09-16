import os 
# Open a file for reading
file_path = "example.txt"  # Replace with the path to your file
try:
    with open(file_path, "r") as file:
        # Read the content of the file
        file_content = file.read()

        # Analyze the file content (e.g., count characters and lines)
        char_count = len(file_content)
        line_count = len(file_content.splitlines())

        # Display the analysis results
        print("File Path:", file_path)
        print("Character Count:", char_count)
        print("Line Count:", line_count)

except OSError as e:
    print("An error occurred:", str(e))

