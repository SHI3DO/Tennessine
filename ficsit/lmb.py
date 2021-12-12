loga = []


def log(content):
    loga.append(content)


def reset():
    loga.clear()


def out():
    print(loga)


def get():
    return loga
