class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainOnlyOneAtSymbol(Exception):
    pass


class MailNameMustContainDotError(Exception):
    pass


valid_domains = ["com", "bg", "org", "net"]
email = input()

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if email.count("@") > 1:
        raise MustContainOnlyOneAtSymbol("Email should contain only one @")

    email_name, domain_name = email.split('@')

    if len(email_name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." not in domain_name:
        raise MailNameMustContainDotError("The mail should have official domain")

    mail_name, domain = domain_name.split('.')

    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

    email = input()


