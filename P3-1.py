# Triple point of CO2 (K, Pa).
T3_CO2, p3_CO2 = 216.58, 5.185e5
# Enthalpy of fusion of CO2 (kJ.mol -1).
DfusH_CO2 = 9.019
# Entropy of fusion of CO2 (J.K-1.mol -1).
DfusS_CO2 = 40
# Enthalpy of vaporization of CO2 (kJ.mol-1).
DvapH_CO2 = 15.326
# Entropy of vaporization of CO2 (J.K-1.mol-1).
DvapS_CO2 = 70.8
# Triple point of H2O (K, Pa).
T3_H2O, p3_H2O = 273.16, 611.73
# Enthalpy of fusion of H2O (kJ.mol -1).
DfusH_H2O = 6.01
# Entropy of fusion of H2O (J.K-1.mol -1).
DfusS_H2O = 22.0
# Enthalpy of vaporization of H2O (kJ.mol-1).
DvapH_H2O = 40.68
# Entropy of vaporization of H2O (J.K-1.mol-1).
DvapS_H2O = 118.89

print(f'{"":24s}{"CO2":10s}{"H2O":10s}')
print('-' * 40)
print(f'{"p3":10s}{"/Pa":12s}{p3_CO2:10.6g}{p3_H2O:10.5g}')
print(f'{"T3":10s}{"/K":12s}{T3_CO2:10.2f}{T3_H2O:10.2f}')
print(f'{"DfusH":10s}{"/kJ.mol-1":12s}{DfusH_CO2:10.3f}{DfusH_H2O:10.3f}')
print(f'{"DfusS":10s}{"/J.K-1.mol-1":12s}{DfusS_CO2:10.1f}{DfusS_H2O:10.1f}')
print(f'{"DvapH":10s}{"/kJ.mol-1":12s}{DvapH_CO2:10.3f}{DvapH_H2O:10.3f}')
print(f'{"DvapS":10s}{"/J.K-1.mol-1":12s}{DvapS_CO2:10.1f}{DvapS_H2O:10.1f}')
