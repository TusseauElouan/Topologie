#ifndef USER_HPP
#define USER_HPP

#include <string>

class User {
private:
    std::string first_name_;
    std::string last_name_;
    std::string department_;
    std::string role_;

public:
    User(
        const std::string& first_name,
        const std::string& last_name,
        const std::string& department,
        const std::string& role
    );

    const std::string& first_name() const;
    const std::string& last_name() const;
    const std::string& department() const;
    const std::string& role() const;
    std::string full_name() const;
};

#endif

