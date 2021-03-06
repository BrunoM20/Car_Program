# -*- coding: utf-8 -*-
"""Car_Program.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ysFgkXXNi5t-Q_8yQO9LtpC7hLAzGvpl
"""

print("Consumo de um carro em um certo trajeto utilizando etanol ou gasolina: ")
m = str(input("\nModelo do carro: "))
Km = float(input("\nDistância percorrida (km): "))
Gas = float(input("\nPreço da gasolina (R$): ")) 
Et = float(input("\nPreço do Etanol (R$): "))
if m == 'Fox' or m == 'fox':
  consum_gas = (Km/13.5)*Gas
  consum_et = (Km/9.5)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Civic' or m == 'civic':
  consum_gas = (Km/12.9)*Gas
  consum_et = (Km/8.9)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Uno' or m == 'uno':
  consum_gas = (Km/21)*Gas
  consum_et = (Km/15)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Fusca' or m == 'fusca':
  consum_gas = (Km/14.4)*Gas
  consum_et = (Km/10.3)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")  
elif m == 'Corolla' or m == 'corolla':
  consum_gas = (Km/13.2)*Gas
  consum_et = (Km/9.2)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")    
elif m == 'HB20' or m == 'hb20':  
  consum_gas = (Km/14.6)*Gas
  consum_et = (Km/10.1)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Gol' or m == 'gol':
  consum_gas = (Km/12.9)*Gas
  consum_et = (Km/8.8)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Palio' or m == 'palio':
  consum_gas = (Km/15)*Gas
  consum_et = (Km/10.3)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Celta' or m == 'celta':
  consum_gas = (Km/16.9)*Gas
  consum_et = (Km/12.2)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
elif m == 'Onix' or m == 'onix':        
  consum_gas = (Km/12.8)*Gas
  consum_et = (Km/8.7)*Et
  print("\nO consumo do", m,f"na gasolina será de R${consum_gas:.2f} e no etanol R${consum_et:.2f}")
else:
   print("\nO modelo inserido não foi encontrado no sistema")
   print("\nModelos disponíveis: Fox, Civic, Uno, Fusca, Corolla, HB20, Gol, Palio, Celta e Onix")