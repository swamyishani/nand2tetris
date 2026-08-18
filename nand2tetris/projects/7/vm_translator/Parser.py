class vm_Parser:
  def __init__(self, input_file):
    self.input_file = input_file
    with open(self.input_file) as f:
      self.lines = [line.strip() for line in f if line.strip() and not line.strip().startswith('//')]
    self.current_index = 0
    self.current_line = self.lines[0] if self.lines else ""

  def hasMoreLines(self, count):
    return count < len(self.lines)

  def advance(self, count):
    if self.hasMoreLines(count):
      self.current_line = self.lines[count]

  def commandType(self):
    arithmetic_logical = ['add','sub','neg','eq','gt','lt','and','or','not']
    cmd = self.current_line.split()[0] if self.current_line else ""
    if cmd in arithmetic_logical:
      return 'C_ARITHMETIC'
    elif cmd == 'push':
      return 'C_PUSH'
    elif cmd == 'pop':
      return 'C_POP'
    elif cmd == 'label':
      return 'C_LABEL'
    elif cmd == 'goto':
      return 'C_GOTO'
    elif cmd == 'if-goto':
      return 'C_IF'
    elif cmd == 'function':
      return 'C_FUNCTION'
    elif cmd == 'return':
      return 'C_RETURN'
    elif cmd == 'call':
      return 'C_CALL'
    else:
      return None

  def arg1(self):
    if self.commandType() == 'C_RETURN':
      return None
    if self.commandType() == 'C_ARITHMETIC':
      return self.current_line.split()[0]
    return self.current_line.split()[1]

  def arg2(self):
    cmd_type = self.commandType()
    if cmd_type in ['C_CALL', 'C_FUNCTION', 'C_PUSH', 'C_POP']:
      return self.current_line.split()[2]
    return None

