import datetime
import platform
import os

def get_system_info():
    return {
        "timestamp": datetime.datetime.now().isoformat(),
        "hostname": platform.node(),
        "os": platform.system(),
        "python_version": platform.python_version(),
        "environment": os.environ.get("APP_ENV","development"),
        "message": os.environ.get("APP_MESSAGE","Hello from Docker!")
    }


def main():
    print("=" * 50)
    print(" System app Info")
    print("=" * 50)
    info = get_system_info()
    for key, value in info.items():
        print(f"{key:20} : {value}") 
    print("="*50)

if __name__ == "__main__":
    main()
