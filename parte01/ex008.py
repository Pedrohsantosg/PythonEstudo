n = float(input('Digite um valor, no conversor de metros --> '))
km = n*(10**-3)
hm = n*(10**-2)
dam = n*(10**-1)
dm = n*(10**1)
cm = n*(10**2)
mm = n*(10**3)
print('A medida de {}m corresponde a {:.3f}km, {:.2f}hm, {:.1f}dam, {:.0f}dm, {:.0f}cm, {:.0f}mm'.format(n,km, hm, dam, dm, cm, mm))
