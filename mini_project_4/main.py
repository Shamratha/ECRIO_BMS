"""
main.py — ECRIO_BMS Mini Project 4
────────────────────────────────────
Advanced Data Processing demo:
  • Line-by-line file reading
  • List, Tuple, Set, Dictionary operations
  • Stack (LIFO) and Queue (FIFO) demos
  • Custom exceptions
  • Assertions
  • Python logging

Run:
    python main.py
"""

import os
from logger_config import get_logger
from custom_exceptions import (
    FileProcessingError, EmptyFileError,
    StackUnderflowError, QueueUnderflowError,
)
from utils import (
    read_file_line_by_line,
    demonstrate_list_ops,
    demonstrate_tuple_ops,
    demonstrate_set_ops,
    demonstrate_dict_ops,
    Stack,
    Queue,
)

logger = get_logger("main")
BASE_DIR   = os.path.dirname(__file__)
SAMPLE_FILE = os.path.join(BASE_DIR, "data", "sample_data.txt")
DIV = "  " + "─" * 55


def section(title: str) -> None:
    print(f"\n{DIV}\n  📌  {title}\n{DIV}")


# ──────────────────────────────────────────────────────────────────────────────
# Ensure sample data file exists
# ──────────────────────────────────────────────────────────────────────────────

def ensure_sample_file() -> None:
    """Create a sample text file if it doesn't already exist."""
    os.makedirs(os.path.dirname(SAMPLE_FILE), exist_ok=True)
    if not os.path.exists(SAMPLE_FILE):
        words = [
            "apple banana cherry apple date elderberry",
            "fig grape honeydew fig apple banana",
            "kiwi lemon mango kiwi fig",
            "nectarine orange papaya quince",
            "raspberry strawberry tangerine raspberry",
        ]
        with open(SAMPLE_FILE, "w") as f:
            f.write("\n".join(words))
        print(f"  📝  Created sample file: {SAMPLE_FILE}")


# ──────────────────────────────────────────────────────────────────────────────
# Demo sections
# ──────────────────────────────────────────────────────────────────────────────

def demo_file_reading() -> list[str]:
    section("File Reading — Line by Line")
    try:
        lines = read_file_line_by_line(SAMPLE_FILE)
        print(f"  Lines read: {len(lines)}")
        for i, line in enumerate(lines, 1):
            print(f"  [{i}] {line}")
        return lines
    except (FileProcessingError, EmptyFileError) as exc:
        logger.error("File reading failed: %s", exc)
        print(f"  ❌  {exc}")
        return []


def demo_list_ops(lines: list[str]) -> None:
    section("List Operations")
    numbers = list(range(1, 21))          # [1 .. 20]
    result = demonstrate_list_ops(numbers)
    for key, val in result.items():
        print(f"  {key:<20} : {val}")


def demo_tuple_ops() -> None:
    section("Tuple Operations")
    nums = [10, 20, 10, 30, 40, 10, 50]
    result = demonstrate_tuple_ops(nums)
    for key, val in result.items():
        print(f"  {key:<15} : {val}")


def demo_set_ops() -> None:
    section("Set Operations")
    a = [1, 2, 3, 4, 5, 2, 3]
    b = [3, 4, 5, 6, 7, 5, 6]
    result = demonstrate_set_ops(a, b)
    for key, val in result.items():
        print(f"  {key:<28} : {val}")


def demo_dict_ops(lines: list[str]) -> None:
    section("Dictionary Operations — Word Frequency")
    words = " ".join(lines).split()
    result = demonstrate_dict_ops(words)
    print(f"  Unique words  : {result['unique_words']}")
    print(f"  Most common   : '{result['most_common']}'")
    print(f"  Duplicates    : {result['duplicates']}")


def demo_stack() -> None:
    section("Stack (LIFO) Demo")
    stack = Stack()
    for item in ["Task-A", "Task-B", "Task-C"]:
        stack.push(item)
        print(f"  Pushed → {item}  |  Stack: {stack}")

    print()
    while not stack.is_empty():
        item = stack.pop()
        print(f"  Popped ← {item}  |  Stack: {stack}")

    # Demonstrate custom exception
    print("\n  Attempting pop on empty stack...")
    try:
        stack.pop()
    except StackUnderflowError as exc:
        print(f"  ✅  Caught StackUnderflowError: {exc}")


def demo_queue() -> None:
    section("Queue (FIFO) Demo")
    queue = Queue()
    for item in ["Job-1", "Job-2", "Job-3"]:
        queue.enqueue(item)
        print(f"  Enqueued → {item}  |  Queue: {queue}")

    print()
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"  Dequeued ← {item}  |  Queue: {queue}")

    print("\n  Attempting dequeue on empty queue...")
    try:
        queue.dequeue()
    except QueueUnderflowError as exc:
        print(f"  ✅  Caught QueueUnderflowError: {exc}")


def demo_assertions() -> None:
    section("Assertions Demo")
    x = 42
    assert isinstance(x, int), "x must be an int"
    assert x > 0,              "x must be positive"
    print(f"  All assertions passed for x = {x}")

    # Assertion in a function context
    data = [1, 2, 3]
    assert len(data) > 0, "data list must not be empty"
    print(f"  Assertion passed: data list has {len(data)} items")


# ──────────────────────────────────────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────────────────────────────────────

def main() -> None:
    print("\n" + "=" * 60)
    print("  ⚙️   ECRIO_BMS — Advanced Data Processing")
    print("=" * 60)

    logger.info("Mini Project 4 started")
    ensure_sample_file()

    lines = demo_file_reading()
    demo_list_ops(lines)
    demo_tuple_ops()
    demo_set_ops()
    demo_dict_ops(lines)
    demo_stack()
    demo_queue()
    demo_assertions()

    print(f"\n{'=' * 60}")
    print("  ✅  All demos complete! Check logs/data_processing.log")
    print(f"{'=' * 60}\n")
    logger.info("Mini Project 4 finished")


if __name__ == "__main__":
    main()
