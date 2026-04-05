import os
import platform

def shutdown():
    system = platform.system()
    
    if system == "Windows":
        os.system("shutdown /s /t 1")
    elif system == "Linux" or system == "Darwin":  # Darwin = macOS
        os.system("shutdown -h now")
    else:
        print("Unsupported operating system")

# Call the function
shutdown()