class ArticlesReader(object):
  """ Iterates through parsed Wikipedia's text, provided by original Polyglot project.
  """
  def __init__(self, file_path):
    self._input_iter = open(file_path, 'r').__iter__()
        
  def __iter__(self):
    return self
    
  def _next_article(self):
    tokens = []
        
    # skip first line: first line is [[Article ID]]
    next_sentence = self._input_iter.next()
            
    while True:
        next_sentence = self._input_iter.next()
        next_sentence = next_sentence.decode('utf-8').rstrip()
                
        if next_sentence:
            # beginning of the next article found
            if next_sentence.startswith('[[') and next_sentence.endswith(']]'):
                break
            else:
                tokens.extend(next_sentence.split())
        
    return tokens
    
  def next(self):
    """
    Returns next article tokens.
    :return: list of tokens
    """
    return self._next_article()
