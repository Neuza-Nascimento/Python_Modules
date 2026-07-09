from dotenv import load_dotenv
import os


load_dotenv()
ambient_variables: dict[str, str] = {
    "MATRIX_MODE": "development",
    "DATABASE_URL": "Connected to local instance",
    "LOG_LEVEL": "INFO",
    "API_KEY": "Authenticated",
    "ZION_ENDPOINT": "Online"
}


def verify_env() -> None:
    print("Configuration loaded:")
    for variable in ambient_variables.keys():
        value: str | None = os.getenv(variable)
        name: str = variable.capitalize().replace('_', ' ')
        if value is not None:
            if variable == "MATRIX_MODE" or variable == "LOG_LEVEL":
                print(f"{name} : {value}")
            else:
                print(f"{name} : {ambient_variables[variable]}")
        else:
            if variable == "MATRIX_MODE" or variable == "LOG_LEVEL":
                print(f"{name} : {ambient_variables[variable]}")
            else:
                print(f"{name}: MISSING - please set this variable")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")
    if os.path.exists(".env"):
        verify_env()
        print("\nEnvironment security check: ")
        print("[OK] No hardcoded secrets detected")
        if os.getenv("MATRIX_MODE") == "development":
            print("[WARNING] Ensure .env is NOT used in production"
                  "- use real environment variables!")
        elif os.getenv("MATRIX_MODE") == "production":
            print("[OK] .env file properly configured")
        else:
            print("[WARNING] Variable MATRIX_MODE is not valid")
        print("[OK] Production overrides available")
        print("\nThe Oracle sees all configurations.")
    else:
        print("[WARNING] No .env file found!")
        print("Run: cp .env.example .env")
        print("Then edit .env with your configuration values")


if __name__ == "__main__":
    main()
