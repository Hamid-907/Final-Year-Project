import re

# Function to modify the $i variable in the input string
def modify_script(input_string):
    # Extract the value of $i from the input string
    i_value = re.search(r"\$i='(.*?)';", input_string).group(1)

    # Remove the $i variable declaration
    modified_string = re.sub(r"\$i='.*?';", "", input_string)
    
    # Replace all occurrences of $i with its actual value
    modified_string = re.sub(r"\$i", f"'{i_value}'", modified_string)

    # Replace double quotes with single quotes
    modified_string = modified_string.replace('"', "'")

    return modified_string

# Main function
def main():
    # Prompt the user for the input string
    input_string = input("Please enter the script input: ")

    # Modify the script
    output_string = modify_script(input_string)

    # Print the modified script
    print("\nModified Script:")
    print(output_string)

# Run the main function
if __name__ == "__main__":
    main()
