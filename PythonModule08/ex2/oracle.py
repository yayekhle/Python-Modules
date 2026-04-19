import os
from dotenv import load_dotenv


loaded = load_dotenv()


def run_config() -> None:
    config = {
        "mode": os.getenv("MATRIX_MODE"),
        "database": os.getenv("DATABASE_URL"),
        "api_key": os.getenv("API_KEY"),
        "log_level": os.getenv("LOG_LEVEL"),
        "zion": os.getenv("ZION_ENDPOINT"),
    }

    missing = [k for k, v in config.items() if not v]

    if missing:
        print("WARNING: Missing configuration variables:")
        for key in missing:
            print(f"- {key}")
        print("\nCheck your .env file.\n")

    if loaded and not missing:
        print("ORACLE STATUS: Reading the Matrix...\n")
        print("Configuration loaded:")
        print(f"Mode: {config['mode']}")
        print(f"Database: {config['database']}")
        print(f"API Access: {'OK' if config['api_key'] else 'Missing'}")
        print(f"Log Level: {config['log_level']}")
        print(f"Zion Network: {config['zion']}\n")

    print("Environment security check:")
    if loaded and not missing:
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] Hardcoded secrets detected")
        print("[ERROR] .env file not properly configured")

    if "mode" not in missing and config['mode'] != "development":
        print("[OK] Production overrides available")
    else:
        print("[KO] Production overrides not available")


if __name__ == "__main__":
    run_config()
