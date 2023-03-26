""" Crie uma aplicação que calcule o valor total que o Sr. João possui em moedas de real (R$) no caixa. 
A aplicação deve imprimir o valor total em reais (R$) e pode-se utilizar ponto flutuante para representar
 o valor com duas casas decimais no momento que for imprimir o valor na tela.

Dica bônus: você deve realizar este cálculo fazendo a multiplicação da quantidade de moedas pelo seu valor
correspondente. Por exemplo, para 5 centavos temos 35 moedas, então podemos fazer 35 * 0.05. Depois de realizar
a multiplicação entre todas as moedas, você deve somá-las e apresentar o resultado com o print.

"""
# 0.5 = 35
# 0.10 = 50
# 0.50 = 30
# 1.0 = 19

total_5_centavos = 35 * 0.05
total_10_centavos = 50 * 0.10
total_50_centavos = 30 * 0.50
total_1_real = 1.0 * 19


total_caixa = (total_5_centavos + total_10_centavos + total_50_centavos + total_1_real)

print(total_caixa)