import os
import time

programs = {
    "Zora Terminal": "zora_terminal.py",
    "Zora Control Center": "zora_control.py",
    "Zora Autopilot": "zora_autopilot.py",
    "Zora Memory Engine": "zora_memory.py",
    "Zora Scheduler": "zora_scheduler.py",
    "Zora Visionary Composer": "zora_composer.py",
}

def check_program(file_name):
    return os.path.isfile(file_name)

def galaxy_status():
    print("\n🌌🛸  Zora Galaxy Status Console  🛸🌌\n")
    time.sleep(1)
    for name, file in programs.items():
        exists = check_program(file)
        status = "✅ Found" if exists else "❌ Missing"
        print(f"• {name:<30} ➔ {status}")
        time.sleep(0.4)
    print("\n🚀 All systems checked. Galaxy synchronized.\n")

if __name__ == "__main__":
    galaxy_status()