import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate 

#パラメータの定義
#エタロン1
intencity_1 = 1             #振幅
FSR_1 = 11.5                #単位はGHz
finesse_1 = 53              #フィネス
FWHM_1 = FSR_1 / finesse_1  #半値全幅

#エタロン2
intencity_2 = 1             #振幅
finesse_2 = 53              #フィネス

#A2とExの幅(GHz)
diff = 7.25

#グラフ作成範囲(GHz)
f = 400

#探索のパラメタ
N = 10000                   #分割数

#関数の定義
def lorentz_func(x, A, X0, HWHM):
    return A * HWHM**2 / ((x - X0)**2 + HWHM**2)

def f_1(x):
# =============================================================================
#     エタロン1
# =============================================================================
    y = 0
    for i in range(-250, 251, 1):
        y += lorentz_func(x, intencity_1, FSR_1 * i, FWHM_1/2)
    return y

def f_2(x, a):
# =============================================================================
#     エタロン2 
# =============================================================================
    y = 0
    for i in range(-250, 251, 1):
        y += lorentz_func(x, intencity_2, a * i, a / (finesse_2 * 2))
    return y

x = np.linspace(-f, f, 200 * f) #0.01GHzの幅で配列作成
y1 = f_1(x)
result_x = np.linspace(0.0001, 2.5 * FSR_1, N)
result_etalon = []
result_A2 = []
for j in range(0, len(result_x), 1):
    y3 = f_2(x, result_x[j])
    y = y1 * y3
    integ = 0
    for i in range(0, len(x)-1, 1):
        integ += (y[i + 1] + y[i]) * (x[i + 1] - x[i]) / 2
    result_temp = 10 * np.log10(integ / (2*f))
    result_etalon.append(result_temp)
    result_A2_temp = 10 * np.log10(y[100 * f + 725] / y[100 * f])
    result_A2.append(result_A2_temp)


fig = plt.figure(1)
plt.plot(result_x, result_etalon)
plt.xlim(10, 20)
plt.xlabel("FSR [GHz]")
plt.ylabel("power [dB]")
plt.show()

#A2とEｘの差
fig = plt.figure(2)
plt.plot(result_x, result_A2)
plt.xlabel("FSR [GHz]")
plt.ylabel("differential [dB]")
plt.show()

# =============================================================================
# FSR = 11.8089(GHz)のときを採用。(index = 4107)
# エタロン1とエタロン2の波形をそれぞれf_1(x),f_2(x)とした。
# エタロンの波形は-450~450(GHz)の範囲で作成。
# f_1(x) * f_2(x)のグラフを-200~200(GHz)の範囲で台形近似して積分。(幅0.01GHz)
# FSRは0.0001~28.75(GHz)を10000分割。(幅2.875MHz)
# 0は特異点となるため除いてある。

#計算の幅を広げてみる。
# =============================================================================




