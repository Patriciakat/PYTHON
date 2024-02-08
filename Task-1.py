import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
print("1. UZDUOTIS")

interval = np.linspace(-1.3, 2.5, 64)
print(interval)
print()

# 2. Sukonstruokite pasikartojantį masyvą pagal duotą N. Duotas masyvas [1, 2, 3, 4] ir N = 3
# Rezultatas [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# Masyvas gali būti bet kokio dydžio ir atsitiktinai sugeneruojamas.
print("2. UZDUOTIS")

arr = np.array([1, 2, 3, 4])
n = 3
print(np.tile(arr, n))
print()

# 3. Sukurkite masyvą iš pasikartojančių elementų. Duotas skaičius 3 ir pasikartojimų skaičius 4.
# Rezultatas [3, 3, 3, 3]
print("3. UZDUOTIS")

element = 3
repeats = 4
array_repeat = np.array(np.repeat(element, repeats))
print(array_repeat)
print()

# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių "įrėmintų" vienetais. Užuomina - pad.
print("4. UZDUOTIS")

zero_matrix = np.zeros((10, 10), dtype=int)
matrix_with_zero = np.pad(zero_matrix, pad_width=1, mode='constant', constant_values=1)
print(matrix_with_zero)
print()

# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka.
print("5. UZDUOTIS")

checkerboard = np.zeros((8, 8), dtype=int)
checkerboard[1::2, ::2] = 1
checkerboard[::2, 1::2] = 1
print(checkerboard)
print()

# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j.
print("6. UZDUOTIS")

n = 8
n_arr = np.fromfunction(lambda i, j: i+j, (n, n), dtype=int)
print(n_arr)
print()

# 7. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Užuominos - slicing, argsort, indexing.
print("7. UZDUOTIS")

random_arr = np.random.rand(5, 5)
sorted_array = random_arr[np.argsort(random_arr[:, 1])]
print(sorted_array)
print()

# 8. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių.
print("8. UZDUOTIS")

matrix = np.array([[4, -2, 1],
                   [-2, 4, -2],
                   [1, -2, 3]])
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(eigenvalues)
print(eigenvectors)
print()

# 9. Apskaičiuokite funkcijos 0.5*x**2 + 5 * x + 4 išvestines su numpy ir sympy paketais. Užuominos - poly1d, deriv, diff
print("9. UZDUOTIS")

x = sp.symbols('x')
f = 0.5*x**2 + 5*x + 4
f_derivative = sp.diff(f, x)
print(f_derivative)
print()

# 10. Apskaičiuokite funkcijos e-x apibrėžtinį, intervale [0,1], ir neapibrėžtinį integralus.
print("10. UZDUOTIS")

x = sp.symbols('x')
f = sp.exp(-x)

print("Apibrėžtinis integralas intervale [0, 1]:", sp.integrate(f, (x, 0, 1)))
print("Neapibrėžtinis integralas:", sp.integrate(f, x))

# 11. Pasinaudodami polinėmis koordinatėmis nupieškite kardioidę.
theta = np.linspace(0, 2*np.pi, 100)
r = 1 - np.sin(theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='pink')
plt.title('Kardioidė')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')
plt.show()

# 12. Sugeneruokite masyvą iš 1000 atsitiktinių skaičių, pasiskirsčiusių pagal normalųjį dėsnį su duotais vidurkiu V ir dispersija D. Nupieškite jų histogramą.
V = 10
D = 3
random_no_arr = np.random.normal(V, np.sqrt(D), 1000)

#Histograma
plt.hist(random_no_arr, bins=30, color='pink', alpha=0.7)
plt.title('Histograma')
plt.xlabel('Skaičius')
plt.ylabel('Dažnis')
plt.grid(True)
plt.show()