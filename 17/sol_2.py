import re


class Machine:
    HALT = False
    jumped = False
    registers = {}
    instruction_pointer = 0
    def solve(self, program, registers):
        self.HALT = False
        self.jumped = False
        self.instruction_pointer = 0
        self.registers = registers
        outputs = []
        while not self.HALT and self.instruction_pointer < len(program):
            code = program[self.instruction_pointer]
            value = program[self.instruction_pointer + 1]

            output = self.op(code, value)
            if output is not None:
                outputs.append(output)
            if not self.jumped:
                self.instruction_pointer += 2
            self.jumped = False

        return outputs

    def get_combo_value(self, value: int):
        if value < 4:
            return value
        if value == 4:
            return self.registers["A"]
        if value == 5:
            return self.registers["B"]
        if value == 6:
            return self.registers["C"]
        if value == 7:
            self.HALT = True


    def op(self, code: int, value: int):
        if code == 0:
            self.registers["A"] = int(self.registers["A"] / (2 ** self.get_combo_value(value)))
        if code == 1:
            self.registers["B"] = self.registers["B"] ^ value
        if code == 2:
            self.registers["B"] = self.get_combo_value(value) % 8
        if code == 3:
            if self.registers["A"] != 0:
                self.instruction_pointer = value
                self.jumped = True
        if code == 4:
            self.registers["B"] = self.registers["B"] ^ self.registers["C"]
        if code == 5:
            return self.get_combo_value(value) % 8
        if code == 6:
            self.registers["B"] = int(self.registers["A"] / (2 ** self.get_combo_value(value)))
        if code == 7:
            self.registers["C"] = int(self.registers["A"] / (2 ** self.get_combo_value(value)))


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


with open("input") as file:
    registers, program = parse_input(file.read())
    print(registers, program)
    machine = Machine()
    possible_nums = [0]
    for i in range(1, len(program)+1):
        new_candidates = []
        for number in possible_nums:
            for j in range(8):
                candidate = number * 8 + j
                registers_cp = registers.copy()
                registers_cp["A"] = candidate
                result = machine.solve(program, registers_cp)
                print(candidate, result, program[-i:])
                if result == program[-i:]:
                    print("CD",candidate)
                    new_candidates.append(candidate)
        possible_nums = new_candidates
        print(possible_nums)
