import re

HALT = False
jumped = False
registers = {}
instruction_pointer = 0


def get_combo_value(value: int):
    global HALT
    if value < 4:
        return value
    if value == 4:
        return registers["A"]
    if value == 5:
        return registers["B"]
    if value == 6:
        return registers["C"]
    if value == 7:
        HALT = True


def op(code: int, value: int):
    global instruction_pointer
    global jumped
    if code == 0:
        registers["A"] = int(registers["A"] / (2 ** get_combo_value(value)))
    if code == 1:
        registers["B"] = registers["B"] ^ value
    if code == 2:
        registers["B"] = get_combo_value(value) % 8
    if code == 3:
        if registers["A"] != 0:
            instruction_pointer = value
            jumped = True
    if code == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    if code == 5:
        return get_combo_value(value) % 8
    if code == 6:
        registers["B"] = int(registers["A"] / (2 ** get_combo_value(value)))
    if code == 7:
        registers["C"] = int(registers["A"] / (2 ** get_combo_value(value)))


def parse_input(text):
    # Pattern for registers
    register_pattern = r"Register ([A-C]): (\d+)"
    # Pattern for program
    program_pattern = r"Program: ([\d,]+)"

    # Find all register matches
    registers = {
        match.group(1): int(match.group(2))
        for match in re.finditer(register_pattern, text)
    }

    # Find program numbers
    program_match = re.search(program_pattern, text)
    program = [int(x) for x in program_match.group(1).split(",")]

    return registers, program


with open("debug") as file:
    registers, program = parse_input(file.read())
    print(registers, program)
    outputs = []
    while not HALT and instruction_pointer < len(program):
        code = program[instruction_pointer]
        value = program[instruction_pointer + 1]
        print(code, value, registers)

        output = op(code, value)
        if output is not None:
            print(output)
            outputs.append(output)
        if not jumped:
            instruction_pointer += 2
        jumped = False

    print(",".join([str(output) for output in outputs]))
