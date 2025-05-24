import os
import time

def launch_terminal():
    os.system("osascript -e 'tell app \"Terminal\" to do script \"cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_terminal.py\"'")
    time.sleep(1)

def launch_control_center():
    os.system("osascript -e 'tell app \"Terminal\" to do script \"cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_control.py\"'")
    time.sleep(1)

def launch_autopilot():
    os.system("osascript -e 'tell app \"Terminal\" to do script \"cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_autopilot.py\"'")
    time.sleep(1)

def launch_memory():
    os.system("osascript -e 'tell app \"Terminal\" to do script \"cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_memory.py\"'")
    time.sleep(1)

def launch_scheduler():
    os.system("osascript -e 'tell app \"Terminal\" to do script \"cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_scheduler.py\"'")
    time.sleep(1)

def launch_composer():
    os.system("osascript -e 'tell app \"Terminal\" to do script \"cd ~/Zora-TwitterBot; source venv/bin/activate; python zora_composer.py\"'")
    time.sleep(1)

def launch_all():
    launch_terminal()
    launch_control_center()
    launch_autopilot()
    launch_memory()
    launch_scheduler()
    launch_composer()

def galaxy_console():
    while True:
        print("\n🌌✨  WELCOME TO ZORA GALAXY CONSOLE  ✨🌌")
        print("--------------------------------------")
        print("🌀 [1] Launch Terminal")
        print("🌟 [2] Launch Control Center")
        print("🚀 [3] Launch Autopilot")
        print("🧠 [4] Launch Memory Engine")
        print("🌌 [5] Launch Evolving Scheduler")
        print("🎼 [6] Launch Visionary Composer")
        print("🌠 [7] Launch ALL Modules")
        print("🌙 [0] Exit Console")
        print("--------------------------------------")
        choice = input("\n>>> Select an option: ").strip()

        if choice == "1":
            launch_terminal()
        elif choice == "2":
            launch_control_center()
        elif choice == "3":
            launch_autopilot()
        elif choice == "4":
            launch_memory()
        elif choice == "5":
            launch_scheduler()
        elif choice == "6":
            launch_composer()
        elif choice == "7":
            launch_all()
        elif choice == "0":
            print("\n🌙 Exiting Zora Galaxy Console...\n")
            break
        else:
            print("❌ Invalid selection. Please choose 0-7.")

if __name__ == "__main__":
    galaxy_console()