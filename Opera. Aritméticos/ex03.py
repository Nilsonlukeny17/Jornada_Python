# Conversor de Medidas

medida = float(input('Digite o número em metros a ser convertido: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print('A medida de {}m em km é {}'. format(medida, km))
print('A medida de {}m em hm é {}'. format(medida, hm))
print('A medida de {}m em dam é {}'. format(medida, dam))
print('A medida de {}m em dm é {}'. format(medida, dm))
print('A medida de {}m em cm é {}'. format(medida, cm))
print('A medida de {}m em mm é {}'. format(medida, mm))