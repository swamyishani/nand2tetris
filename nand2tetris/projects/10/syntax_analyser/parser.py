from tokenizer import Tokenizer

class Compilation_Engine:

  def __init__(self):
    output_file='C:\\Users\\swamy\\Downloads\\nand2tetris\\nand2tetris\\projects\\10\\ArrayTest\\Main.jack'
    self.output_file=open(output_file, 'r')
    self.jacktokenizer=Tokenizer()
    self.token_list=self.jacktokenizer.tokens
    return

  def compileTerm(self):
    if self.jacktokenizer.tokenType() == 'KEYWORD':
      self.output_file.write(f'<keyword>{self.jacktokenizer.current_token}</keyword>\n')
    elif self.jacktokenizer.tokenType() == 'SYMBOL':
      self.output_file.write(f'<symbol>{self.jacktokenizer.current_token}</symbol>\n')
    elif self.jacktokenizer.tokenType() == 'IDENTIFIER':
      self.output_file.write(f'<identifier>{self.jacktokenizer.current_token}</identifier>\n')
    elif self.jacktokenizer.tokenType() == 'INT_CONST':
      self.output_file.write(f'<intConstant>{self.jacktokenizer.current_token}</intConstant>\n')
    elif self.jacktokenizer.tokenType() == 'STRING_CONST':
      self.output_file.write(f'<stringConstant>{self.jacktokenizer.current_token}</stringConstant>\n')
    self.jacktokenizer.advance()
    return

  def compileExpressionList(self):
    return

  def compileVarDec(self):
    self.output_file.write('<varDec>\n')
    self.compileTerm()
    return