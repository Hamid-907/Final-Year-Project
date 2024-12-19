#include <windows.h>

int main() {
    // Path to the executable
    const char *path = "C:\\Users\\Wahab\\Desktop\\ttt.exe";

    // Structure to hold process information
    PROCESS_INFORMATION procInfo;
    ZeroMemory(&procInfo, sizeof(procInfo));

    // Structure to specify process attributes
    STARTUPINFO startInfo;
    ZeroMemory(&startInfo, sizeof(startInfo));
    startInfo.cb = sizeof(startInfo);

    // Create the process
    BOOL result = CreateProcess(
        NULL,              // Application name
        (LPSTR)path,       // Command line (including executable path)
        NULL,              // Process security attributes
        NULL,              // Thread security attributes
        FALSE,             // Handles are inherited
        0,                 // Creation flags
        NULL,              // Environment variables
        NULL,              // Current directory
        &startInfo,        // Startup information
        &procInfo          // Process information
    );

    if (result) {
        // Wait for the process to complete (optional)
        WaitForSingleObject(procInfo.hProcess, INFINITE);
        
        // Close process and thread handles
        CloseHandle(procInfo.hProcess);
        CloseHandle(procInfo.hThread);
    } else {
        // Handle the error
        DWORD error = GetLastError();
        // Optional: Print or log the error
    }

    return 0;
}