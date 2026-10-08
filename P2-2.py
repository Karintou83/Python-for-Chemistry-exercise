mC,mH,mO = 12, 1, 16
mtri = mC * 55 + mH * 104 + mO * 6
mH2O, mCO2 = mH * 2 + mO, mC + mO * 2

ntri = 1000 / mtri
MH2O, MCO2 = ntri * mH2O * 52, ntri * mCO2 * 55
print("H2O:", MH2O, "g, CO2:", MCO2, "g")
print("二酸化炭素としての排出割合", MCO2*100/1000, "％")