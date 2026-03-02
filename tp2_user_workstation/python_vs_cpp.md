# Python vs C++ for `User` class

## 1. Syntax and typing

- Python:
  - Very compact syntax (`dataclass`).
  - Dynamic runtime, optional type hints.
  - No header/source split.
- C++:
  - Explicit types and compilation.
  - Header (`User.hpp`) + implementation (`User.cpp`).
  - Public/private sections are mandatory design choices.

## 2. Encapsulation

- Python:
  - Convention-based encapsulation.
  - Attributes can be accessed directly unless constrained manually.
- C++:
  - Strong compile-time encapsulation via `private`.
  - Access only through public methods.

## 3. Performance and deployment

- Python:
  - Faster to write and iterate.
  - Interpreted; runtime dependency on Python environment.
- C++:
  - Compiled binary, generally faster execution.
  - Longer compile/setup cycle but better low-level control.

## 4. Memory model

- Python:
  - Automatic memory management (garbage collector).
- C++:
  - Deterministic object lifetime (RAII), explicit control when needed.

## 5. Practical conclusion for this TP

- Python is ideal for fast modeling and test-first iteration.
- C++ is better when strict encapsulation and performance constraints matter.

