#!/usr/bin/python3
import imp


def main():
    # Load the .pyc file
    module_name = "hidden_4"
    path = "hidden_4.pyc"

    #Load the module
    module = imp.load_compiled(module_name, path)

    module_names = [name for name in dir(module) if not name.startswith("__")]
    module_names.sort()

    for name in module_names:
        print(name)


if __name__ == "__main__":
    main()
