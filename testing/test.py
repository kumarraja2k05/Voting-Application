import validations.validation as validate
def test1():
    dob="2000-06-18"
    age=int(validate.Validate.get_age(dob))
    assert age == 22


def test2():
    dob="2000-10-05"
    age=int(validate.Validate.get_age(dob))
    assert age == 20

def test3():
    dob="2001-08-27"
    age=int(validate.Validate.get_age(dob))
    assert age == 21
