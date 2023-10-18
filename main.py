import math

# Funções para cálculos de valores
def format_scientific(number):
    return "{:.2e}".format(number)

def calculate_Bm_I(Em):
    Bm = Em / 377  # Impedância do vácuo
    I = 0.5 * Em * Bm
    return Bm, I

def calculate_Em_Bm(I):
    Em = math.sqrt(2 * I / 377)
    Bm = Em / 377
    return Em, Bm

def calculate_Em_I(Bm):
    Em = Bm * 377
    I = 0.5 * Em * Bm
    return Em, I

def calculate_lambda_k_omega(f):
    c = 3 * 10**8  # Velocidade da luz no vácuo (m/s)
    wavelength = c / f
    k = 2 * math.pi / wavelength
    omega = 2 * math.pi * f
    return wavelength, k, omega

def calculate_f_k_omega(wavelength):
    c = 3 * 10**8  # Velocidade da luz no vácuo (m/s)
    f = c / wavelength
    k = 2 * math.pi / wavelength
    omega = 2 * math.pi * f
    return f, k, omega

def calculate_f_lambda_omega(k):
    c = 3 * 10**8  # Velocidade da luz no vácuo (m/s)
    wavelength = 2 * math.pi / k
    f = c / wavelength
    omega = 2 * math.pi * f
    return f, wavelength, omega

def calculate_f_lambda_k(omega):
    c = 3 * 10**8  # Velocidade da luz no vácuo (m/s)
    f = omega / (2 * math.pi)
    wavelength = c / f
    k = 2 * math.pi / wavelength
    return f, wavelength, k

# Função principal
def main():
    print("Escolha uma opção:")
    print("1. Calcular Bm e I a partir de Em")
    print("2. Calcular Em e Bm a partir de I")
    print("3. Calcular Em e I a partir de Bm")
    print("4. Calcular λ, k e ω a partir de f")
    print("5. Calcular f, k e ω a partir de λ")
    print("6. Calcular f, λ e k a partir de ω")
    print("7. Calcular f, λ e ω a partir de k")

    choice = int(input())

    if choice == 1:
        Em = float(input("Digite a amplitude do campo elétrico (Em): "))
        Bm, I = calculate_Bm_I(Em)
        print(f"Bm: {format_scientific(Bm)}")
        print(f"I: {format_scientific(I)}")
    elif choice == 2:
        I = float(input("Digite a intensidade (I): "))
        Em, Bm = calculate_Em_Bm(I)
        print(f"Em: {format_scientific(Em)}")
        print(f"Bm: {format_scientific(Bm)}")
    elif choice == 3:
        Bm = float(input("Digite a amplitude do campo magnético (Bm): "))
        Em, I = calculate_Em_I(Bm)
        print(f"Em: {format_scientific(Em)}")
        print(f"I: {format_scientific(I)}")
    elif choice == 4:
        f = float(input("Digite a frequência (f): "))
        wavelength, k, omega = calculate_lambda_k_omega(f)
        print(f"λ: {format_scientific(wavelength)}")
        print(f"k: {format_scientific(k)}")
        print(f"ω: {format_scientific(omega)}")
    elif choice == 5:
        wavelength = float(input("Digite o comprimento de onda (λ): "))
        f, k, omega = calculate_f_k_omega(wavelength)
        print(f"f: {format_scientific(f)}")
        print(f"k: {format_scientific(k)}")
        print(f"ω: {format_scientific(omega)}")
    elif choice == 6:
        k = float(input("Digite o número de onda (k): "))
        f, wavelength, omega = calculate_f_lambda_omega(k)
        print(f"f: {format_scientific(f)}")
        print(f"λ: {format_scientific(wavelength)}")
        print(f"ω: {format_scientific(omega)}")
    elif choice == 7:
        omega = float(input("Digite a frequência angular (ω): "))
        f, wavelength, k = calculate_f_lambda_k(omega)
        print(f"f: {format_scientific(f)}")
        print(f"λ: {format_scientific(wavelength)}")
        print(f"k: {format_scientific(k)}")
    else:
        print("Escolha inválida.")

if __name__ == "__main__":
    main()

