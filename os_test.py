import os

print(os.path.abspath('.'))
print(os.path.abspath('..'))
print(os.path.exists('/Users/'))
print(os.path.isfile('/Users/'))
print(os.path.isdir('/Users/'))
print(os.path.join('/tmp/a','b/c'))

from pathlib import Path
p = Path('.')
print(p.resolve())

# p.is_dir()




# pathlib 和 os 相似