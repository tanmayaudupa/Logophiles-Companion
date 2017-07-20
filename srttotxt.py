"""
Creates readable text file from SRT file.
"""
import re, sys
import organisedsubtitles as ors
def is_time_stamp(l):
  if l[:2].isnumeric() and l[2] == ':':
    return True
  return False

def has_letters(line):
  if re.search('[a-zA-Z]', line):
    return True
  return False

def has_no_text(line):
  l = line.strip()
  if not len(l):
     return True
  if l.isnumeric():
    return True
  if is_time_stamp(l):
    return True
  if l[0] == '(' and l[-1] == ')':
    return True
  if not has_letters(line):
    return True
  return False

def is_lowercase_letter_or_comma(letter):
  if letter.isalpha() and letter.lower() == letter:
    return True
  if letter == ',':
    return True
  return False

def clean_up(lines):
  """
  Get rid of all non-text lines and
  try to combine text broken into multiple lines
  """
  new_lines = []
  for line in lines[1:]:
    if has_no_text(line):
      continue
    elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
      #combine with previous line
      new_lines[-1] = new_lines[-1].strip() + ' ' + line
    else:
      #append line
      new_lines.append(line)
  return new_lines

def importsrt(args):

  file_name = args
  try:
    with open(file_name) as f:
      lines = f.readlines()
      new_lines = clean_up(lines)
    new_file_name = file_name[:-4] + '.txt'
    with open(new_file_name, 'w') as f:
      for line in new_lines:
        f.write(line)
    ors.importtxt(new_file_name)
    
    return "organisedsubtitles.txt"
  except:
    print("ERROR in SRT encoding")
    
