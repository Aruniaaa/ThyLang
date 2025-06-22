import run

while True:
    command = input(f"ThyLang >>> ").lower()
    if command == "cease":
        break
    else:
        result, error = run.run("<stdin>", command)

        if error:
            print(error.as_string())
        elif result:
            print(repr(result))
