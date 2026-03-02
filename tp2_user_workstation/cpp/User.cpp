#include "User.hpp"

User::User(
    const std::string& first_name,
    const std::string& last_name,
    const std::string& department,
    const std::string& role
) : first_name_(first_name),
    last_name_(last_name),
    department_(department),
    role_(role) {}

const std::string& User::first_name() const {
    return first_name_;
}

const std::string& User::last_name() const {
    return last_name_;
}

const std::string& User::department() const {
    return department_;
}

const std::string& User::role() const {
    return role_;
}

std::string User::full_name() const {
    return first_name_ + " " + last_name_;
}

