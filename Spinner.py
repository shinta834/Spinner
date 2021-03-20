def counterClockwise (x):
  # transpose matrix dari kolom menjadi baris
  for i in range (len(x)):
    for j in range (i,len(x)):
      x[i][j],x[j][i]=x[j][i],x[i][j]

  # reverse angka dari baris terakhir ke baris pertama
  n = len(x)
  for i in range (n):
    for j in range (n//2):
      x[j][i],x[n-1-j][i]=x[n-1-j][i],x[j][i]
  return x
# input
listAwal = [[1,2,3],[4,5,6],[7,8,9]]
print('List Awal:')
print(listAwal)
print('')
# output
print('Ouput:')
print(counterClockwise(listAwal))