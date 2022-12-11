import glob
def zadanie_2():
  kolvo_txt = len(glob.glob("*.txt"))
  new_txt = open('new.txt', 'w')
  new_txt.write('')
  name = []
  text = []
  sum1 = []
  for i in range(1,kolvo_txt) :
    name.append(f'{i}.txt')
    open1 = open(f'{i}.txt') 
    read1 = open1.read()
    text.append(read1)
  
    sp = read1.split('\n')
    sum = 0
    for spi in range(len(sp)):
      sum+= 1
    sum1.append(sum)
  
  def obmen(x):
    nol = x[k]
    x[k] = x[j]
    x[j] = nol
  for j in range(len(name)-1):
    for k in range(1,len(name)):
      if sum1[j]>sum1[k]:
        obmen(sum1)
        obmen(name)
        obmen(text)
  
  for m in range(len(sum1)):
    new_txt.write(f'{name[m]}\n{m+1}\n{text[m]}\n')
  new_txt.close()
  return new_txt
zadanie_2()
