"""
utils.py — ECRIO_BMS Mini Project 4
─────────────────────────────────────
Helper module demonstrating:
  • File reading (line-by-line)
  • List, tuple, set, dictionary operations
  • Stack and Queue implementations
  • Assertions for internal contracts
"""

import os
from collections import deque
from typing import Any

from custom_exceptions import (
    FileProcessingError,
    EmptyFileError,
    DataValidationError,
    StackUnderflowError,
    QueueUnderflowError,
)
from logger_config import get_logger

logger = get_logger(__name__)


# ──────────────────────────────────────────────────────────────────────────────
# File Utilities
# ──────────────────────────────────────────────────────────────────────────────

def read_file_line_by_line(filepath: str) -> list[str]:
    """
    Read a text file line by line without loading it entirely into memory.
    Strips blank lines and leading/trailing whitespace.

    Args:
        filepath: Absolute or relative path to the text file.

    Returns:
        List of non-empty stripped lines.

    Raises:
        FileProcessingError: If the file cannot be opened.
        EmptyFileError     : If no usable lines are found.
    """
    if not os.path.exists(filepath):
        logger.error("File not found: %s", filepath)
        raise FileProcessingError(f"File not found: {filepath}")

    lines: list[str] = []
    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            for line in fh:          # ← reads one line at a time (memory-efficient)
                stripped = line.strip()
                if stripped:
                    lines.append(stripped)
    except OSError as exc:
        logger.error("Cannot read file %s: %s", filepath, exc)
        raise FileProcessingError(f"Cannot read file: {filepath}") from exc

    if not lines:
        logger.warning("File is empty: %s", filepath)
        raise EmptyFileError(f"File has no usable content: {filepath}")

    logger.debug("Read %d lines from %s", len(lines), filepath)
    return lines


# ──────────────────────────────────────────────────────────────────────────────
# List Operations
# ──────────────────────────────────────────────────────────────────────────────

def demonstrate_list_ops(data: list[int]) -> dict:
    """
    Perform common list operations and return a result dict.

    Operations: append, remove, sort, reverse, slice, count, index.
    """
    assert isinstance(data, list), "data must be a list"

    work = data.copy()
    work.append(99)                        # add element
    work.sort()                            # sort ascending
    sliced = work[:5]                      # first 5 items
    work.reverse()                         # reverse in-place
    total = sum(work)                      # sum

    logger.debug("List ops complete — %d items, sum=%d", len(work), total)
    return {
        "original_len"  : len(data),
        "after_append"  : len(work),
        "sorted_first_5": sliced,
        "total_sum"     : total,
        "max"           : max(work),
        "min"           : min(work),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Tuple Operations
# ──────────────────────────────────────────────────────────────────────────────

def demonstrate_tuple_ops(data: list[int]) -> dict:
    """
    Convert list to tuple and perform read-only operations.
    Tuples are immutable — ideal for fixed data records.
    """
    t = tuple(data)
    return {
        "length"   : len(t),
        "first"    : t[0] if t else None,
        "last"     : t[-1] if t else None,
        "count_10" : t.count(10),           # how many times 10 appears
        "sliced"   : t[:3],
        "is_tuple" : isinstance(t, tuple),
    }


# ──────────────────────────────────────────────────────────────────────────────
# Set Operations
# ──────────────────────────────────────────────────────────────────────────────

def demonstrate_set_ops(list_a: list, list_b: list) -> dict:
    """
    Demonstrate union, intersection, difference, and symmetric difference.
    Sets automatically remove duplicate values.
    """
    set_a = set(list_a)
    set_b = set(list_b)
    return {
        "set_a"               : set_a,
        "set_b"               : set_b,
        "union"               : set_a | set_b,
        "intersection"        : set_a & set_b,
        "difference_a_minus_b": set_a - set_b,
        "symmetric_difference": set_a ^ set_b,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Dictionary Operations
# ──────────────────────────────────────────────────────────────────────────────

def demonstrate_dict_ops(words: list[str]) -> dict:
    """
    Build a frequency dictionary from a list of words.
    Demonstrates: get(), update(), items(), keys(), values(), comprehension.
    """
    freq: dict[str, int] = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1    # count occurrences

    # Dictionary comprehension — keep only words appearing > 1 time
    duplicates = {k: v for k, v in freq.items() if v > 1}

    return {
        "frequency"  : freq,
        "unique_words": len(freq),
        "duplicates" : duplicates,
        "most_common": max(freq, key=freq.get) if freq else None,
    }


# ──────────────────────────────────────────────────────────────────────────────
# Stack (LIFO) — built on a Python list
# ──────────────────────────────────────────────────────────────────────────────

class Stack:
    """
    Last-In, First-Out data structure.
    Uses a plain list internally; push = O(1), pop = O(1).
    """

    def __init__(self) -> None:
        self._data: list[Any] = []

    def push(self, item: Any) -> None:
        """Push an item onto the top of the stack."""
        self._data.append(item)
        logger.debug("Stack push: %s (size=%d)", item, len(self._data))

    def pop(self) -> Any:
        """
        Remove and return the top item.

        Raises:
            StackUnderflowError: If the stack is empty.
        """
        if self.is_empty():
            logger.error("Stack underflow — pop() called on empty stack")
            raise StackUnderflowError("Cannot pop from an empty stack.")
        item = self._data.pop()
        logger.debug("Stack pop: %s (size=%d)", item, len(self._data))
        return item

    def peek(self) -> Any:
        """Return the top item without removing it."""
        if self.is_empty():
            raise StackUnderflowError("Cannot peek into an empty stack.")
        return self._data[-1]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Stack({self._data})"


# ──────────────────────────────────────────────────────────────────────────────
# Queue (FIFO) — built on collections.deque for O(1) dequeue
# ──────────────────────────────────────────────────────────────────────────────

class Queue:
    """
    First-In, First-Out data structure.
    Uses collections.deque for O(1) enqueue and dequeue.
    """

    def __init__(self) -> None:
        self._data: deque[Any] = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the back of the queue."""
        self._data.append(item)
        logger.debug("Queue enqueue: %s (size=%d)", item, len(self._data))

    def dequeue(self) -> Any:
        """
        Remove and return the front item.

        Raises:
            QueueUnderflowError: If the queue is empty.
        """
        if self.is_empty():
            logger.error("Queue underflow — dequeue() called on empty queue")
            raise QueueUnderflowError("Cannot dequeue from an empty queue.")
        item = self._data.popleft()
        logger.debug("Queue dequeue: %s (size=%d)", item, len(self._data))
        return item

    def front(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise QueueUnderflowError("Queue is empty.")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def size(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"
