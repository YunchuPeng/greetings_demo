def greet(personal, family, title: str = "", polite: bool = False) -> str:
    """Generate a greeting string for a person.

    Parameters
    ----------
    personal : str
        Given name, e.g. "Terry"
    family : str
        Family name, e.g. "Gilliam"
    title : str, optional
        Optional title, e.g. "Dr", "Prof"
    polite : bool, optional
        If True, use a more formal greeting.

    Returns
    -------
    str
        A complete greeting sentence.

    Examples
    --------
    >>> from greetings.greeter import greet
    >>> greet("Terry", "Jones")
    'Hey, Terry Jones.'
    >>> greet("Graham", "Chapman", polite=True)
    'How do you do, Graham Chapman.'
    >>> greet("Michael", "Palin", title="CBE")
    'Hey, CBE Michael Palin.'
    """
    greeting = "How do you do, " if polite else "Hey, "
    if title:
        greeting += f"{title} "

    greeting += f"{personal} {family}."
    return greeting
