from tokenizer import Tokenizer
jacktokenizer=Tokenizer()

class CompilationEngine:

  def __init__(self, input_file, output_file):
    self.input_file=input_file
    self.output_file=output_file
    self.token=jacktokenizer.current_token
    return

  def compileTerm(self):
    term_type=jacktokenizer.tokenType()
    if term_type == 'SYMBOL':
      self.output_file.write(f'<symbol>{jacktokenizer.symbol()}</symbol>')
    if term_type == 'INT_CONST':
      self.output_file.write(f'<symbol>{jacktokenizer.intVal()}</symbol>')
    if term_type == 'STRING_CONST':
      self.output_file.write(f'<symbol>{jacktokenizer.stringVal()}</symbol>')
    if term_type == 'IDENTIFIER':
      self.output_file.write(f'<symbol>{jacktokenizer.identifier()}</symbol>')
    return

  def compileClass(self):
    self.output_file.write('<keyword>class</keyword>\n')
    jacktokenizer.advance()
    symbol=jacktokenizer.symbol()
    self.output_file.write(f'<symbol>{symbol}</symbol>')
    self.compileClass()
    jacktokenizer.advance()
    symbol=jacktokenizer.symbol()
    self.output_file.write(f'<symbol>{symbol}</symbol>')
    return

  def compileClassVarDec(self):
    self.output_file.write('<><>')
