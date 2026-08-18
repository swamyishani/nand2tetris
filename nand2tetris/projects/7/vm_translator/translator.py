from pathlib import Path
import Parser
from code_writer import vm_code_writer

file=Path(input("Enter the path to the .vm file: "))
output_file=file.with_suffix('.asm')

VM_Parser = Parser.vm_Parser(file)
VM_Code_Writer=vm_code_writer(output_file)
count=0
while VM_Parser.hasMoreLines(count):
  command_type = VM_Parser.commandType()
  if command_type == 'C_ARITHMETIC':
    VM_Code_Writer.writeArithmetic(VM_Parser.arg1())
  elif command_type == 'C_PUSH':
    VM_Code_Writer.writePushPop('C_PUSH', VM_Parser.arg1(), VM_Parser.arg2())
  elif command_type == 'C_POP':
    VM_Code_Writer.writePushPop('C_POP', VM_Parser.arg1(), VM_Parser.arg2())
  count+=1
  VM_Parser.advance(count)
VM_Code_Writer.close()