"""
clean_inventory_system.py

A cleaned and safer version of the provided inventory_system example.
Improvements:
 - Avoid mutable default args
 - Use explicit exception handling
 - Validate argument types and values
 - Use context managers for file I/O
 - Configure logging instead of print for program actions
 - Remove dangerous eval usage
 - Provide a safe CLI-friendly main guard
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Optional

# Configure module logger
logger = logging.getLogger("inventory")
if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Global stock data (kept as a module-level dict)
stock_data: Dict[str, int] = {}


def add_item(item: str, qty: int, logs: Optional[List[str]] = None) -> None:
    """
    Add qty of item into stock_data.
    Validates inputs and records a log entry if logs list provided.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not item:
        logger.error("add_item: 'item' must be a non-empty string")
        raise TypeError("'item' must be a non-empty string")
    if not isinstance(qty, int):
        logger.error("add_item: 'qty' must be an integer")
        raise TypeError("'qty' must be an integer")
    if qty < 0:
        logger.error("add_item: 'qty' must be non-negative")
        raise ValueError("'qty' must be non-negative")

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now().isoformat()}: Added {qty} of {item}")
    logger.info("Added %d x %s", qty, item)


def remove_item(item: str, qty: int) -> None:
    """
    Remove qty of item from stock_data. Raises KeyError if item doesn't exist,
    ValueError for invalid quantities.
    """
    if not isinstance(item, str) or not item:
        logger.error("remove_item: 'item' must be a non-empty string")
        raise TypeError("'item' must be a non-empty string")
    if not isinstance(qty, int):
        logger.error("remove_item: 'qty' must be an integer")
        raise TypeError("'qty' must be an integer")
    if qty <= 0:
        logger.error("remove_item: 'qty' must be positive")
        raise ValueError("'qty' must be positive")

    if item not in stock_data:
        logger.error("remove_item: item '%s' not in stock_data", item)
        raise KeyError(item)

    current = stock_data[item]
    if qty >= current:
        # remove the item entirely
        del stock_data[item]
        logger.info("Removed all of item %s", item)
    else:
        stock_data[item] = current - qty
        logger.info("Removed %d of %s (remaining %d)", qty, item, stock_data[item])


def get_qty(item: str) -> int:
    """
    Return quantity of item. Raises KeyError if item not present.
    """
    if item not in stock_data:
        logger.error("get_qty: item '%s' not found", item)
        raise KeyError(item)
    return stock_data[item]


def load_data(file: str = "inventory.json") -> None:
    """
    Load stock_data from a JSON file. If the file does not exist, initialize
    stock_data to an empty dict.
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, dict):
                raise ValueError("inventory file must contain a JSON object")
            # convert values to ints when possible
            stock_data = {str(k): int(v) for k, v in data.items()}
            logger.info("Loaded %d items from %s", len(stock_data), file)
    except FileNotFoundError:
        logger.warning("%s not found. Starting with empty inventory.", file)
        stock_data = {}
    except (json.JSONDecodeError, ValueError) as exc:
        logger.exception("Failed to parse %s: %s", file, exc)
        raise


def save_data(file: str = "inventory.json") -> None:
    """
    Save stock_data to a JSON file safely using a context manager.
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
            logger.info("Saved %d items to %s", len(stock_data), file)
    except OSError:
        logger.exception("Failed to save data to %s", file)
        raise


def print_data() -> None:
    """Print a human-readable items report."""
    logger.info("Items Report:")
    for key, qty in stock_data.items():
        logger.info("  %s -> %d", key, qty)


def check_low_items(threshold: int = 5) -> List[str]:
    """Return list of item names whose quantity is below threshold."""
    if not isinstance(threshold, int) or threshold < 0:
        raise ValueError("threshold must be a non-negative integer")
    return [name for name, qty in stock_data.items() if qty < threshold]


def _demo_operations() -> None:
    """Small sequence used only for demonstration when run as script."""
    try:
        add_item("apple", 10)
        add_item("banana", 2)
        remove_item("apple", 3)
        logger.info("Apple stock: %d", get_qty("apple"))
        logger.info("Low items: %s", check_low_items())
    except Exception:
        logger.exception("Demo operations failed")


def main() -> None:
    """Load existing data, run demo operations, and persist data."""
    load_data()
    _demo_operations()
    save_data()


if __name__ == "__main__":
    main()
