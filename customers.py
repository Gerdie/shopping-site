from passlib.hash import pbkdf2_sha256

"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = pbkdf2_sha256.encrypt(password, rounds=20000, salt_size=16)

    def __repr__(self):

        return "<Customer {} {}>".format(self.last_name, self.email)


def read_customers_from_file(filename):
    customers = {}
    with open(filename) as melon_file:
        for line in melon_file:
            line = line.rstrip().split('|')
            first_name, last_name, email, password = line
            customers[email] = Customer(first_name, last_name, email, password)

    return customers


def get_by_email(email):

    # flash_login_error = flash("Sorry, couldn't find your email!")

    return customers_list.get(email)


customers_list = read_customers_from_file("customers.txt")