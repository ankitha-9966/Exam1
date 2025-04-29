def register(name, email, password):
    if email.endswith("@gmail.com"):
        if len(password) >= 8:
            return "Registration successfull"
            
        else:
            return "Password must be 8 characters long"
    else:
        return "Invalid email"

print(register("Ankitha", "Ankitha@gmail.com", "1234asdf"))
print(register("Ankitha", "Ankitha", "1234asdf"))
print(register("Ankitha", "Ankitha@gmail.com", "1234af"))

