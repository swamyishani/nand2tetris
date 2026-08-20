from pathlib import Path

class vm_code_writer:
  def __init__(self,output_file):
    self.output_file = Path(output_file)
    self.file = open(self.output_file, 'w')
    self.label_counter = 0
    return

  def writePushPop(self, command, segment, index):
    assembly_code = ''
    if command == 'C_PUSH':
      self.file.write(f'// push {segment} {index}\n')
      if segment == 'constant':
        assembly_code=f'@{index}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'local':
        assembly_code=f'@LCL\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'argument':
        assembly_code=f'@ARG\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'this':
        assembly_code=f'@THIS\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'that':
        assembly_code=f'@THAT\nD=M\n@{index}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'temp':
        assembly_code=f'@{5+int(index)}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'static':
        assembly_code=f'@{self.output_file.stem}.{index}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
      elif segment == 'pointer':
        if index == '0':
          assembly_code=f'@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
        elif index == '1':
          assembly_code=f'@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1'
    elif command == 'C_POP':
      self.file.write(f'// pop {segment} {index}\n')
      if segment == 'local':
        assembly_code=f'@LCL\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D'
      elif segment == 'argument':
        assembly_code=f'@ARG\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D'
      elif segment == 'this':
        assembly_code=f'@THIS\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D'
      elif segment == 'that':
        assembly_code=f'@THAT\nD=M\n@{index}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D'
      elif segment == 'temp':
        assembly_code=f'@{5+int(index)}\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D'
      elif segment == 'static':
        assembly_code=f'@{self.output_file.stem}.{index}\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D'
      elif segment == 'pointer':
        if index == '0':
          assembly_code=f'@SP\nAM=M-1\nD=M\n@THIS\nM=D'
        elif index == '1':
          assembly_code=f'@SP\nAM=M-1\nD=M\n@THAT\nM=D'
    self.file.write(assembly_code + '\n')

  def writeArithmetic(self, command):
    if command=='add':
      self.file.write(f'// add\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M+D\n')
    elif command=='sub':
      self.file.write(f'// sub\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M-D\n')
    elif command=='neg':
      self.file.write(f'// neg\n@SP\nA=M-1\nM=-M\n')
    elif command=='eq':
      self.file.write(f'// eq\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@EQ_TRUE{self.label_counter}\nD;JEQ\n@SP\nA=M-1\nM=0\n@EQ_END{self.label_counter}\n0;JMP\n(EQ_TRUE{self.label_counter})\n@SP\nA=M-1\nM=-1\n(EQ_END{self.label_counter})\n')
      self.label_counter += 1  
    elif command=='gt':
      self.file.write(f'// gt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@GT_TRUE{self.label_counter}\nD;JGT\n@SP\nA=M-1\nM=0\n@GT_END{self.label_counter}\n0;JMP\n(GT_TRUE{self.label_counter})\n@SP\nA=M-1\nM=-1\n(GT_END{self.label_counter})\n')
      self.label_counter += 1
    elif command=='lt':
      self.file.write(f'// lt\n@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@LT_TRUE{self.label_counter}\nD;JLT\n@SP\nA=M-1\nM=0\n@LT_END{self.label_counter}\n0;JMP\n(LT_TRUE{self.label_counter})\n@SP\nA=M-1\nM=-1\n(LT_END{self.label_counter})\n')
      self.label_counter += 1
    elif command=='and':
      self.file.write(f'// and\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M&D\n')
    elif command=='or':
      self.file.write(f'// or\n@SP\nAM=M-1\nD=M\nA=A-1\nM=M|D\n')
    elif command=='not':
      self.file.write(f'// not\n@SP\nA=M-1\nM=!M\n')
    return

  def writeLabel(self, label):
    label_name=label.split()[0]
    self.file.write(f'({label_name})')
    return

  def writeGoto(self, label):
    label_name=label.split()[0]
    self.file.write(f'@{label_name}\n0;JMP\n')
    return

  def writeIf(self, label):
    label_name=label.split()[0]
    self.file.write(f'@SP\nAM=M-1\nD=M\n@{label_name}\nD;JNE\n')
    return

  def writeFunction(self, function_name, n_vals):
    self.file.write(f'({function_name})\n')
    i=0
    while i < int(n_vals):
      self.file.write('@SP\nAM=M+1\nA=A-1\nM=0\n')
    return

  def writeCall(self, function_name, n_args):
    self.file.write('@return_address\n')
    self.file.write('@LCL\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n')
    self.file.write('@ARG\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n')
    self.file.write('@THIS\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n')
    self.file.write('@THAT\nD=M\n@SP\nAM=M+1\nA=A-1\nM=D\n')
    self.file.write(f'@SP\nD=M\n@5\nD=D-A\n@{n_args}\nD=D-A\n@ARG\nM=D\n')
    self.file.write('@SP\nD=M\n@LCL\nM=D\n')
    self.writeGoto(function_name)
    self.writeLabel('return_address')
    return

  def writeReturn(self):
    self.file.write('@LCL\nD=M\n@SP\nM=D\n')
    self.file.write('@R13\nD=M\n@5\nA=D-A\nD=M\n')
    self.file.write('@R14\nM=D\n@SP\nAM=M-1\nD=M\n@ARG\nA=M\nM=D\n')
    self.file.write('@ARG\nD=M+1\n@SP\nM=D\n')
    self.file.write('@R13\nD=M\n@1\nA=D-A\nD=M\n@THAT\nM=D\n')
    self.file.write('@R13\nD=M\n@2\nA=D-A\nD=M\n@THIS\nM=D\n')
    self.file.write('@R13\nD=M\n@3\nA=D-A\nD=M\n@ARG\nM=D\n')
    self.file.write('@R13\nD=M\n@4\nA=D-A\nD=M\n@LCL\nM=D\n')
    self.file.write('@R14\nA=M\n0;JMP\n')
    return

  def close(self):
    self.file.close()
    return

    