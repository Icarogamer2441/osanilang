commands = {}
variables = {}
oscommands = {}
functions = {}

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
            elif pushtype.startswith("prvar"):
                varname = line.split(", >")[1].split("<")[0].strip("\"\'")
                print(variables.get(varname), end="")
            elif pushtype.startswith("newline"):
                print("")
        elif line.startswith("add"):
            addtype = line.split(" ")[1].strip("\"\'")
            if addtype.startswith("cmd"):
                cmdname = line.split(", ")[1].strip("\"\'")
                commands[cmdname] = []
            if addtype.startswith("oscmd"):
                cmdname = line.split(", ")[1].strip("\"\'")
                oscommands[cmdname] = []
            elif addtype.startswith("code"):
                cmdname = line.split(", ")[1].split(" @> ")[0].strip("\"\'")
                cmdcode = line.split(" @> ")[1].split(" @<")[0].strip("\"\'")
                for cmds in commands:
                    if cmdname == cmds:
                        commands[cmdname].append(cmdcode)
            elif addtype.startswith("funccode"):
                funcname = line.split(", ")[1].split(" @> ")[0].strip("\"\'")
                funccode = line.split(" @> ")[1].split(" @<")[0].strip("\"\'")
                for func in functions:
                    if funcname == func:
                        functions[funcname].append(funccode)
            elif addtype.startswith("oscode"):
                cmdname = line.split(", ")[1].split(" @> ")[0].strip("\"\'")
                cmdcode = line.split(" @> ")[1].split(" @<")[0].strip("\"\'")
                for cmds in oscommands:
                    if cmdname == cmds:
                        oscommands[cmdname].append(cmdcode)
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
                    for cm in oscommands:
                        print(cm)
                else:
                    exec("\n".join(commands[command]))
                    for cmd in oscommands:
                        if command == cmd:
                            interpret("\n".join(oscommands[cmd]))
        elif line.startswith("define"):
            definetype = line.split(" ")[1].strip("\"\'")
            if definetype.startswith("int"):
                varname = line.split("> ")[1].split(", ")[0].strip("\"\'")
                value = line.split(", ")[1].strip("\"\'")
                variables[varname] = int(value)
            elif definetype.startswith("string"):
                varname = line.split("> ")[1].split(", ")[0].strip("\"\'")
                value = line.split(", >")[1].split("<")[0].strip("\"\'")
                variables[varname] = value
            elif definetype.startswith("bool"):
                varname = line.split("> ")[1].split(", ")[0].strip("\"\'")
                value = line.split(", ")[1].strip("\"\'")
                if value == "true":
                    variables[varname] = True
                elif value == "false":
                    variables[varname] = False
                else:
                    print("use true or false!")
            elif definetype.startswith("float"):
                varname = line.split("> ")[1].split(", ")[0].strip("\"\'")
                value = line.split(", ")[1].strip("\"\'")
                variables[varname] = float(value)
            elif definetype.startswith("function"):
                funcname = line.split(", ")[1].strip("\"\'")
                functions[funcname] = []
        elif line.startswith("call"):
            funcname = line.split(", ")[1].strip("\"\'")
            for func in functions:
                if funcname == func:
                    interpret("\n".join(functions[funcname]))

def execute_file(filename):
    if filename.endswith(".os"):
        with open(filename, "r") as f:
            content = f.read()
        interpret(content)
    else:
        print("use an osani file extension: .os")

filename = input("what's your .os file? > ")
execute_file(filename)
