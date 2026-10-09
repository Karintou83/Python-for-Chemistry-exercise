fcc = {"Cu", "Co", "Fe", "Mn", "Ni", "Sc"}
bcc = {"Cr", "Fe", "Mn", "Ti", "V"}
hcp = {"Co", "Ni", "Sc", "Ti", "Zn"}

## (a) 面心立方(fcc)、体心立方(bcc)、六方最密充填(hcp)のうち1つの構造のみをとる金属
print("面心立方(fcc)、体心立方(bcc)、六方最密充填(hcp)のうち1つの構造のみをとる金属:" )
print((fcc - bcc - hcp) | (bcc - fcc - hcp) | (hcp - fcc - bcc))

## (b) これら3つのうち2つの構造をとる金属
print("これら3つのうち2つの構造をとる金属:" )
print((fcc & bcc - hcp) | (fcc & hcp - bcc) | (bcc & hcp - fcc))

## (c) hcp構造をとらない金属
print("hcp構造をとらない金属:" )
print((fcc - hcp) | (bcc - hcp))

## (d) 3つの構造をとる金属
print("3つの構造をとる金属:" )
if fcc & bcc & hcp:
    print(fcc & bcc & hcp)
else:
    print("存在しません")
