from pathlib import Path
path = Path('texts/potatoes.txt')

try:
    contents = path.read_text(encoding='UTF-8')
except FileNotFoundError:
    print("File not found!")
else:
    words = contents.split()
    newWords = len(words)
    print(f'The file {path} has {newWords}')
    
    