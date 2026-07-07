from dotenv import load_dotenv
import os

load_dotenv()
ambient_variables = ["MATRIX_MODE", "DATABASE_URL", "API_KEY", "LOG_LEVEL", 
                     "ZION_ENDPOINT"]
default_values = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "INFO",
}


def verify() -> None:
    print("Configuration loaded:\n")
    for variable in ambient_variables:
        value = os.getenv(variable)
        if value is not None:
            print(f"{variable.capitalize()} : {value}")
        else:
            if variable in default_values.keys():
                print(f"{variable.capitalize()} : {default_values[variable]}")
            else:
                print(f"{variable}: MISSING - please set this variable")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    verify()


if __name__ == "__main__":
    main()
