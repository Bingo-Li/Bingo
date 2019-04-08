from pathlib import Path
p = Path('.')
print(list(p.glob('**/*.py')))
