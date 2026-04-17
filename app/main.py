import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Default App")
ENV = os.getenv("ENVIRONMENT", "development")


def add_numbers(a: int, b: int) -> int:
    return a + b


def get_app_info() -> str:
    return f"{APP_NAME} running in {ENV}"


if __name__ == "__main__":
    print(get_app_info())
    print("2 + 3 =", add_numbers(2, 3))