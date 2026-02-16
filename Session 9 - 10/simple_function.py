from os import name


def greeting():
    """
    Print greeting in multiple languages
    :return: None
    """
    print("Hello")
    print("Hola")
    print("Bonjour")
    print("Salam")
    print("Bom dia")
    print("Ciao")

    for _ in range(3):
        greeting()

def enchanced_greeting(name):
    """
    Print greeting in multiple languages towards another person
    :param name: the name of the person to greet
    :return: None
    """

    print("Hello", name)
    print("Hola", name)
    print("Bonjour", name)
    print("Salam", name)
    print("Bom dia", name)
    print("Ciao", name)

enchanced_greeting("Valeria")
enchanced_greeting("Maria")

def enchanced_greeting2(name):
    """
    Returns greeting in multiple languages towards another person
    :param name: the name of the person to greet
    :return: string
    """

    message = ""
    message += f"Hello {name}\n"
    message += f"Hola {name}\n"
    message += f"Bonjour {name}\n"
    message += f"Salem {name}\n"
    return message

result = enchanced_greeting2("Valeria")
print(f"The greetings are: {result}")