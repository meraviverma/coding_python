# coding_python
# 🧩 What is `TypedDict` in Python?

## 🔹 Definition
`TypedDict` is a feature from Python’s **typing module** (introduced in Python 3.8) that allows you to define the **expected structure of a dictionary** — including the keys and the types of their values.  

It’s essentially a way to give dictionaries **type hints**, making your code more readable, maintainable, and safer.

---

## 🔹 Why Use `TypedDict`?
Normally, Python dictionaries are flexible but unstructured:

```python
user = {"name": "Ravi", "age": 30, "is_admin": True}
```

There’s no guarantee that:
- The keys will always exist (`name`, `age`, `is_admin`).  
- The values will be of the correct type (`str`, `int`, `bool`).  

`TypedDict` solves this by enforcing a **schema** for your dictionary.

---

## 🔹 Example Usage

```python
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int
    is_admin: bool

# Example dictionary that follows the schema
user: UserDict = {
    "name": "Ravi",
    "age": 30,
    "is_admin": True
}
```

- ✅ Keys must match exactly (`name`, `age`, `is_admin`).  
- ✅ Values must be of the correct type (`str`, `int`, `bool`).  
- If you try to assign a wrong type, type checkers (like `mypy`) will raise an error.

---

## 🔹 Variants of `TypedDict`

1. **Required vs Optional Keys**
```python
class UserDict(TypedDict, total=False):
    name: str
    age: int
    is_admin: bool
```
- `total=False` → All keys are optional.  
- Without `total=False`, all keys are required.

2. **Mixing Required and Optional**
```python
class UserDict(TypedDict):
    name: str
    age: int

class PartialUserDict(UserDict, total=False):
    is_admin: bool
```

---

## 🔹 Benefits
- **Type Safety** → Prevents accidental misuse of dictionary keys/values.  
- **Documentation** → Acts as a schema, making code self-explanatory.  
- **Tooling Support** → Works with static type checkers (`mypy`, `pyright`).  
- **Maintainability** → Easier to manage complex dictionaries in large projects.

---

## 🔹 Key Takeaway
`TypedDict` is like a **lightweight data class for dictionaries**:
- Use it when you want the flexibility of dictionaries but with the **safety of type hints**.  
- It’s especially useful in **data pipelines, APIs, and configurations** where dictionary structures must remain consistent.

