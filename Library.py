def register(name, email, password):
    if email.endswith("@gmail.com"):
        if len(password) >= 8:
            if password.isalnum():
                return "Registration successfull"
            else:
                return "Password must be alphanumeric"
        else:
            return "Password must be 8 characters long"
    else:
        print("Invalid email")

register("Ankitha", "Ankitha@gmail.com", "1234asdf")
register("Ankitha", "Ankitha", "1234asdf")
register("Ankitha", "Ankitha@gmail.com", "12343456")
register("Ankitha", "Ankitha@gmail.com", "1234af")

