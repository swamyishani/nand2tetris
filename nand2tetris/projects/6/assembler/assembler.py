from pathlib import Path

# PRE-PASS

symbol_table = {
    'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3, 'THAT': 4,
    'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5,
    'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
    'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15,
    'SCREEN': 16384, 'KBD': 24576
}

file = Path(input("Enter file address: "))
hack_file = file.with_suffix('.hack')

row_count = 0
ram_count = 16
lines_to_be_kept = []

with open(file, 'r') as asm_file:
    for line in asm_file:
        line = line.strip()

        if not line or line.startswith('//'):
            continue

        lines_to_be_kept.append(line)
        row_count += 1

with open(hack_file, 'w') as asm_file:
    for line in lines_to_be_kept:
        asm_file.write(line + '\n')

# FIRST-PASS

counter = 0
lines_to_be_kept = []

with open(hack_file, 'r') as asm_file:
    for line in asm_file:
        line = line.strip()

        if not line:
            continue
        if line.startswith('(') and line.endswith(')'):
            symbol_table[line[1:-1]] = counter
            continue

        lines_to_be_kept.append(line)
        counter += 1

with open(hack_file, 'w') as asm_file:
    for line in lines_to_be_kept:
        asm_file.write(line + '\n')


# SECOND-PASS

dest_lookup_table = {'M': '001', 'D': '010', 'DM': '011', 'A': '100', 'AM': '101', 'AD': '110', 'ADM': '111'}
jump_lookup_table = {'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100', 'JNE': '101', 'JLE': '110', 'JMP': '111'}
comp_a_lookup_table = {
    '0': '101010', '1': '111111', '-1': '111010', 'D': '001100', 'A': '110000', '!D': '001101', '!A': '110001',
    '-D': '001111', '-A': '110011', 'D+1': '011111', 'A+1': '110111', 'D-1': '001110', 'A-1': '110010',
    'D+A': '000010', 'D-A': '010011', 'A-D': '000111', 'D&A': '000000', 'D|A': '010101'
}
comp_b_lookup_table = {
    'M': '110000', '!M': '110001', '-M': '110011', 'M+1': '110111', 'M-1': '110010', 'D+M': '000010',
    'D-M': '010011', 'M-D': '000111', 'D&M': '000000', 'D|M': '010101'
}

lines_to_be_kept = []

with open(hack_file, 'r') as asm_file:
    for line in asm_file:
        line = line.strip()

        if not line:
            continue

        if line.startswith('@'):
            symbol = line[1:]
            if symbol.isdigit():
                value = int(symbol)
            elif symbol in symbol_table:
                value = symbol_table[symbol]
            else:
                symbol_table[symbol] = ram_count
                value = ram_count
                ram_count += 1

            a_instruct = format(value, '016b')
            lines_to_be_kept.append(a_instruct)
            continue

        dest = ''
        jump = ''
        comp = line

        if '=' in line:
            dest, comp = line.split('=', 1)

        if ';' in comp:
            comp, jump = comp.split(';', 1)

        if dest == '':
            dest_bits = '000'
        else:
            dest_bits = dest_lookup_table.get(dest, '000')

        if jump == '':
            jump_bits = '000'
        else:
            jump_bits = jump_lookup_table.get(jump, '000')

        if comp in comp_a_lookup_table:
            a_bit = '0'
            comp_bits = comp_a_lookup_table[comp]
        elif comp in comp_b_lookup_table:
            a_bit = '1'
            comp_bits = comp_b_lookup_table[comp]
        else:
            raise ValueError(f'Unknown comp mnemonic: {comp}')

        c_instruct = '111' + a_bit + dest_bits + comp_bits + jump_bits
        lines_to_be_kept.append(c_instruct)

with open(hack_file, 'w') as asm_file:
    for line in lines_to_be_kept:
        asm_file.write(line + '\n')



    