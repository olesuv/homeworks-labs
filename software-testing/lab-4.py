import math


def func(a, y):
    try:
        res = math.sqrt(y**2 - 2*a)
    except ValueError:
        return "Under sqrt should be bigger than 0"

    return a * res    


if __name__ == "__main__":
    while True:
        parameters = {
            "a": None,
            "y": None
        }

        print("For exit enter `exit`")

        for option_name, value in parameters.items():
            u_input = input(f"Enter {option_name}: ")
            if u_input == "exit":
                exit()

            parameters[option_name] = int(u_input)

        res = func(parameters["a"], parameters["y"])
        print(f"Result: {res}\n")

