# Python 3: Deep Dive – Part 2  
## Sequences, Iterables, Generators, and More

Welcome to **Part 2** of the *Python 3: Deep Dive* series. This section focuses on foundational concepts that power Python’s data handling and flow control. If you want to level up your understanding of how Python works under the hood, you're in the right place.

---

## 🧭 Topics Covered

### 📌 Sequences
- Sequence types: `list`, `tuple`, `str`, `range`
- Immutability vs Mutability
- Indexing, slicing, and sequence operations
- Sequence protocol (`__getitem__`, `__len__`)

### 📌 Iterables
- What it means to be iterable
- The iterable protocol: `__iter__`
- Iterating with `for` loops and manual iteration

### 📌 Iterators
- The iterator protocol: `__next__`, `__iter__`
- Stateless vs Stateful iteration
- Creating custom iterators
- Handling `StopIteration`

### 📌 Generators
- Generator functions using `yield`
- Generator expressions
- Lazy evaluation and performance benefits
- Use cases for pipelines and streams

### 📌 Comprehensions
- List, set, and dictionary comprehensions
- Nested comprehensions
- Conditional expressions inside comprehensions
- Performance vs readability

### 📌 Context Managers
- The `with` statement
- Context management protocol: `__enter__`, `__exit__`
- Creating custom context managers
- Simplifying with `contextlib`

---

## 🚀 Getting Started

### Requirements
- Python 3.8 or higher
- Familiarity with basic Python syntax

### Running Examples
Clone the repository and navigate through topic directories:

```bash
git clone https://github.com/yourusername/python-deep-dive-part-2.git
cd python-deep-dive-part-2
python3 examples/sequences/example.py
