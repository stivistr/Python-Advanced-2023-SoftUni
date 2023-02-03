def age_assignment(*args, **kwargs):
    person_info = []

    for letter, age in kwargs.items():
        person = ""

        for name in args:
            if name.startswith(letter):
                person = f"{name} is {age} years old."

        person_info.append(person)

    return '\n'.join(sorted(person_info))


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
