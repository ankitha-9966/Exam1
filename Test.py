from Library import register

def test_cases():
    assert register("Ankitha", "Ankitha@gmail.com", "1234asdf") == "Registration successfull"
    assert register("Ankitha", "Ankitha", "1234asdf") == "Password must be 8 characters long"
    assert register("Ankitha", "Ankitha@gmail.com", "1234af") == "Invalid email"