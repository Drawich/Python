from datetime import datetime
import logging
import os
import sys
from typing import Tuple, Callable

# Config a robust prod log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.FileHandler("app_system.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)


class BillValidator:
    """Handles strict data validation and cleaning for financial inputs."""

    @staticmethod
    def clean_and_validate_float(user_input: str) -> float:
        """Cleans string inputs and validates them as positive floats."""
        cleaned = user_input.strip().replace(',', '.')
        cleaned = "".join(c for c in cleaned if c.isdigit() or c == '.')

        try:
            value = float(cleaned)
            if value <= 0:
                raise ValueError("Value must be greater than zero.")
            return value
        except ValueError as e:
            logging.error(f"Validation failed for float input '{user_input}': {str(e)}")
            raise

    @staticmethod
    def validate_people(user_input: str) -> int:
        """Ensures the crowd count is a strict, positive integer with no decimals."""
        cleaned = user_input.strip()
        if ',' in cleaned or '.' in cleaned:
            logging.warning(f"Invalid entry using float: {user_input}")
            raise ValueError("The amount of people needs to be in whole numbers (e.g., 5).")

        try:
            value = int(cleaned)
            if value <= 0:
                raise ValueError("Count must be greater than zero.")
            return value
        except ValueError as e:
            logging.error(f"Validation failed for integer input '{user_input}': {str(e)}")
            raise


class BillSplitterService:
    """Core domain service for financial calculations and historical logging."""

    def __init__(self, filename: str = "receipt_history.txt"):
        self.filename = filename

    @staticmethod
    def calculate(meal_cost: float, tip_per: float, people: int) -> Tuple[float, float]:
        """Executes deterministic financial calculations for the split."""
        if people <= 0:
            logging.critical("ZeroDivisionError vector in calculate execution.")
            raise ZeroDivisionError("Cannot divide a bill by zero people.")

        total_cost = meal_cost * (tip_per / 100) + meal_cost
        per_person = total_cost / people
        return total_cost, per_person

    def log_receipt(self, cost: float, people: int, per_person: float) -> None:
        """Appends the immutable transaction receipt to the local storage layer."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        receipt_text = (
            f"\n[{timestamp}]\n"
            f"-- Receipt Summary --\n"
            f"Total cost: ${cost:.2f}\n"
            f"Total amount of people: {people}\n"
            f"Cost per person: ${per_person:.2f}\n"
            f"------------------------------\n"
        )

        try:
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(receipt_text)
            logging.info(f"Transaction successfully logged: {self.filename}")
        except IOError as e:
            logging.error(f"Storage write failure on {self.filename}: {str(e)}")
            raise


def get_validated_inputs(prompt: str, validate_func: Callable[[str], any]) -> any:
    """Prompts user for input and checks for 'exit'."""
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'exit':
            print("\nExiting program.")
            logging.info("Pipeline execution terminated gracefully via 'exit' command.")
            sys.exit()
        try:
            return validate_func(user_input)
        except ValueError as e:
            print(f"Input Error: {str(e)} Please try again.")


def run_pipeline():
    """Orchestrates the data ingestion and processing pipeline in continuous loop."""
    logging.info("Initiating Bill Splitter pipeline execution.")
    service = BillSplitterService()

    while True:
        try:
            print("\n-- NEW BILL CALCULATION --")
            print("Type 'exit' to leave at any time.")

            meal_cost = get_validated_inputs(
                "What is the total cost of the meal? \n",
                BillValidator.clean_and_validate_float
            )

            tip_per = get_validated_inputs(
                "What is the tip percentage you'd like to apply? \n",
                BillValidator.clean_and_validate_float
            )

            people = get_validated_inputs(
                "How many people do you want to divide the amount with? \n",
                BillValidator.validate_people
            )

            try:
                total, per_person = service.calculate(meal_cost, tip_per, people)
                print(f"\nCalculated Successfully:\nTotal: ${total:.2f} | Per Person: ${per_person:.2f}")
                service.log_receipt(total, people, per_person)
            except Exception as e:
                logging.critical(f"Unhandled processing error: {str(e)}")
                print("An unexpected mathematical or system error occurred. Restarting pipeline...")
        except ValueError as e:
            print(f"\nEncountered validation constraints: {str(e)}")
            print("Restarting pipeline for a new entry...")
        except Exception as e:
            logging.critical(f"Unhandled pipeline collapse: {str(e)}")
            break

        user_choice = input("\nWould you like to split another bill? (yes, no): ").strip().lower()
        if user_choice not in ['yes', 'y']:
            print("\nExiting program. Good bye!")
            break
