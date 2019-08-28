import os
import command_list as cl


def read_commands():
    input_command = ""
    while input_command != "exit":
        print(">>> " , end="")
        input_command = input()
        if input_command == "exit":
            exit(0)
        elif input_command == "help":
            print( cl.command_list )


def valid_workspace( dirpath=None  ):

    module_path = dirpath if dirpath else os.getcwd()
    if not os.path.exists( module_path ):
        return False

    list_of_important_folders = [
        "managers",
        "amd/build",
        "amd/src",
        "view",
        "templates",
        "style",
        "core",
        "classes",
        "db"
    ]

    for dir_to_check in list_of_important_folders:
        if not os.path.exists( os.path.join( dirpath , dir_to_check ) ) :
            print("No existe el directorio:'" + dir_to_check + "' en '" + os.path.join(dirpath, dir_to_check) + "'")
            return False

    return True


def main():
    if not valid_workspace( "/usr/local/www/apache24/data/moodle35/blocks/ases" ):
        print("Espacio de trabajo no válido.")
        return -1

    read_commands()


if __name__ == "__main__":
    main()