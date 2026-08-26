class Tokenizer:

  def __init__(self):
    self.keywords=['class','constructor','function','method','field','static','var','int','char','boolean','void','true','false','null','this','let','do','if','else','while','return']
    self.symbols=['{','}','[',']','(',')','+','-','*','/','.',';',',','&','|','<','>','=','~']
    input_file='C:\\Users\\swamy\\Downloads\\nand2tetris\\nand2tetris\\projects\\10\\ArrayTest\\Main.jack'
    self.input_file=open(input_file, 'r')
    self.tokens=[]
    for line in self.input_file:
      if not line or line.startswith('//') or line.startswith('/*'):
        pass
      else:
        token=''
        for i in line:
          if i not in self.symbols:
            token+=i
          else:
            token=token.strip()
            if token != '':
              self.tokens.append(token)
            self.tokens.append(i)
            token=''
    print(self.tokens)
    self.current_token=self.tokens[0]
    self.current_index=0
    return

  def hasMoreTokens(self):
    return self.current_index+1 < len(self.tokens)

  def advance(self):
    if self.hasMoreTokens(self):
      self.current_token=self.tokens[self.current_index+1]
      self.current_index+=1
    return

  def tokenType(self):
    if self.current_token in self.keywords:
      return 'KEYWORD'
    if self.current_token in self.symbols:
      return 'SYMBOL'
    if self.current_token.startswith('\'') or self.current_token.startswith('\"'):
      return 'STRING_CONST'
    if self.current_token.isdigit():
      return 'INT_CONST'
    else:
      return 'IDENTIFIER'

  def keyWord(self):
    if self.tokenType() == 'KEYWORD':
      return self.current_token

  def symbol(self):
    if self.tokenType() == 'SYMBOL':
      return self.current_token

  def identifier(self):
    if self.tokenType() == 'IDENTIFIER':
      return self.current_token

  def intVal(self):
    if self.tokenType() == 'INT_CONST':
      return int(self.current_token)

  def stringVal(self):
    if self.tokenType() == 'STRING_CONST':
      return self.current_token  

