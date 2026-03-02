#include <iostream>

#include "User.hpp"

int main() {
    User user("Rachel", "Assistant", "Direction", "Executive Assistant");
    std::cout << "User: " << user.full_name() << "\n";
    std::cout << "Department: " << user.department() << "\n";
    std::cout << "Role: " << user.role() << "\n";
    return 0;
}

