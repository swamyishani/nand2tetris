class Tokenizer:

  def __init__(self, input_file):
    self.keywords = ['class','constructor','function','method','field','static','var','int','char','boolean','void','true','false','null','this','let','do','if','else','while','return']
    self.symbols = ['{','}','(',')','[',']','.',',',';','+','-','*','/','&','|','<','>','=','~']
    self.input_file=input_file
    self.token_count=0
    for i in self.input_file.read():
      self.token_count+=1
    self.current_token=self.input_file.read()[0]
    return

  def hasMoreTokens(self, count):
    return count < self.token_count

  def advance(self, count):
    if self.hasMoreTokens(count):
      self.current_token=self.input_file.read()[count]
    return

  def tokenType(self):
    if self.current_token in self.keywords:
      return 'KEYWORD'
    elif self.current_token in self.symbols:
      return 'SYMBOL'
    elif self.current_token.isdigit():
      return 'INT_CONST'
    elif (self.current_token.startswith('\"') and self.current_token.endswith('\"')) or (self.current_token.startswith('\'') and self.current_token.endswith('\'')):
      return 'STRING_CONST'
    identifier=1
    for i in self.current_token:
      if i.isdigit():
        continue
      elif i.isalpha():
        continue
      elif i == '_':
        continue
      else:
        identifier=0
        break
    if identifier == 1:
      return 'IDENTIFIER'

  def keyWord(self):
    if self.tokenType() == 'KEYWORD':
      keyword=self.current_token
      return keyword.upper()

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

    
