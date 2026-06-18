import os
import time
import datetime

def get_config():
    return {
        "app_name": os.environ.get("APP_NAME","my_app"),
        "environment": os.environ.get("APP_ENV","development"),
        "db_host": os.environ.get("DB_HOST","localhost"),
        "db_port": os.environ.get("DB_PORT","localhost"),
        "db_name": os.environ.get("DN_NAME","mydb")
    }

def main():
    config = get_config()

    print("="*50)
    print(f"{config['app_name']}")
    print(f"  Environment: {config['environment']}")
    print("=" * 50)
    
    print(f"\nDatabase config:")
    print(f"  Host: {config['db_host']}")
    print(f"  Port: {config['db_port']}")
    print(f"  Name: {config['db_name']}")
    
    print("\nSimulating work...")
    for i in range(1, 6):
        print(f"  [{datetime.datetime.now().strftime('%H:%M:%S')}] Processing batch {i}/5")
        time.sleep(2)
    
    print("\nDone!")

if __name__ == "__main__":
    main()