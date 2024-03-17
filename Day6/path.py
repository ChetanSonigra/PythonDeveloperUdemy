from pathlib import Path

base = Path.home()           # gives home directory.
guide = Path(base, 'Europe', 'France',Path('Paris', 'Effil.txt'))
guide2 = guide.with_name('Efill2.txt')
print(base, guide, guide2,sep='\n')
print(guide.parent)

guide = Path(Path.home(),'PycharmProjects/python1')
for txt in Path(guide).glob('**/*.txt'):
    print(txt)
    
guide = Path('Europe', 'France',Path('Paris', 'Effil.txt'))
print(guide.relative_to('Europe'),guide.relative_to(Path('Europe','France')))