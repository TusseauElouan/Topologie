# TP2 - User and Workstation

## Expected deliverables

- PlantUML class diagram for `User` and `Workstation`.
- Python implementation for `User`.
- C++ implementation for `User`.
- A focused comparison between Python and C++ for this class implementation.

## Files

- `concept/user_workstation.puml`: class diagram.
- `python/user_workstation.py`: Python classes.
- `cpp/User.hpp` and `cpp/User.cpp`: C++ class `User`.
- `cpp/main.cpp`: small usage example.
- `python_vs_cpp.md`: language comparison.
- `tests/test_user_workstation.py`: Python tests.

## Run Python tests

```powershell
.\implement\.venv\Scripts\python.exe -m pytest tp2_user_workstation\tests
```

## Build C++ sample (g++)

```bash
g++ -std=c++17 cpp/User.cpp cpp/main.cpp -o tp2_user_demo
```

