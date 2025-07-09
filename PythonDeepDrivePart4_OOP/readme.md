# 🐍 Python Object-Oriented Concepts

This document provides a concise overview of key object-oriented programming (OOP) concepts in Python.

---

## 📦 Classes
- Blueprint for creating objects.
- Encapsulates data and behavior.

## 🔗 Methods and Binding
- Functions defined inside classes.
- Bound to instances or classes depending on type.

## 👥 Instance, Class, and Static Methods
- **Instance Methods**: Operate on object instances (`self`).
- **Class Methods**: Operate on the class itself (`@classmethod`, `cls`).
- **Static Methods**: Independent of class or instance (`@staticmethod`).

## 🏠 Properties
- Manage access to instance attributes.
- Enable controlled read/write behavior.

## 🎨 Property Decorators
- Use `@property`, `@<property>.setter`, and `@<property>.deleter`.
- Provide cleaner syntax for getters and setters.

## 🧬 Single Inheritance
- A class inherits from one parent class.
- Promotes code reuse and hierarchy.

## 🚪 Slots
- Use `__slots__` to restrict dynamic attribute creation.
- Saves memory by avoiding `__dict__`.

## 🧙 Descriptors
- Objects that define `__get__`, `__set__`, and `__delete__`.
- Used to customize attribute access.

## 🎭 Enumerations
- Use `enum.Enum` to define symbolic names for constant values.
- Improves code readability and safety.

## 🚨 Exceptions
- Handle runtime errors gracefully using `try`, `except`, `finally`.
- Custom exceptions can be defined via subclassing `Exception`.

## 🧠 Metaprogramming
- Writing code that manipulates code.
- Includes decorators, metaclasses, and dynamic attribute creation.

---

Feel free to expand each section with examples or explanations tailored to your project or learning goals!