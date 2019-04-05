from pathlib import Path

path= Path("ecommerce")
print(path.exists())
# print(path.mkdir())
# print(path.rmdir())
for files in path.glob('*'):

    print(files)