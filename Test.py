from Library import register

def test_cases():
    assert register("Ankitha", "Ankitha@gmail.com", "1234asdf") == "Registration successfull"
    assert register("Ankitha", "Ankitha", "1234asdf") == "Invalid email"
    assert register("Ankitha", "Ankitha@gmail.com", "1234af") == "Password must be 8 characters long"