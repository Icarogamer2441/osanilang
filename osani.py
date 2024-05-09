commands = {}
variables = {}

def interpret(code):
    lines = code.split("\n")

    for line in lines:
        if line.startswith("push"):
            pushtype = line.split(" ")[1].strip("\"\'")
            if pushtype.startswith("prchar"):
                charmsg = line.split(", ")[1].strip("\"\'")
                if len(charmsg) < 2 and len(charmsg) > 0:
                    print(charmsg, end="")
                else:
                    print("Error in print char: you can only print a char if you have one letter")
            elif pushtype.startswith("prtext"):
                msg = line.split(", >")[1].split("<")[0].strip("\"\'")
                print(msg, end="")
            elif pushtype.startswith("newline"):
                print("\n")
        elif line.startswith("add"):
            addtype = line.split(" ")[1].strip("\"\'")
            if addtype.startswith("cmd"):
                cmdname = line.split(", ")[1].strip("\"\'")
                commands[cmdname] = []
            elif addtype.startswith("code"):
                cmdname = line.split(", ")[1].split(" @>")[0].strip("\"\'")
                cmdcode = line.split("@> ")[1].split(" @<")[0].strip("\"\'")
                for cmds in commands:
                    if cmdname == cmds:
                        commands[cmdname].append(cmdcode)
                    else:
                        print("command not found")
        elif line.startswith("start"):
            osname = line.split(" ")[1].strip("\"\'")
            while True:
                command = input(f"{osname} > ")
                if command == "exit":
                    break
                elif command == "help":
                    print("commands:")
                    for cmd in commands:
                        print(cmd)
                else:
                    for cmd in commands:
                        if command == cmd:
                            exec("\n".join(commands[cmd]))
                        else:
                            print(f"Unknown command: {command}")
                            break

def execute_file(filename):
    if filename.endswith(".os"):
        with open(filename, "r") as f:
            content = f.read()
        interpret(content)

filename = input("what's your .os file? > ")
execute_file(filename)
