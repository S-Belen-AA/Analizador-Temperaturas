from typing import List

class AnalizadorTemperaturas:
    def __init__(self, dias: int = 7):
        self.dias = dias
        self.temperaturas: List[float] = []

    def obtener_temperaturas(self):
        print("Ingreso de temperaturas diarias:\n")
        for dia in range(1, self.dias + 1):
            while True:
                try:
                    entrada = input(f"Ingrese la temperatura del día {dia} (°C): ")
                    temperatura = float(entrada)
                    self.temperaturas.append(temperatura)
                    break
                except ValueError:
                    print("Entrada no válida. Por favor, ingrese un número.")

    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def encontrar_max_min(self):
        max_temp = max(self.temperaturas)
        min_temp = min(self.temperaturas)
        dia_max = self.temperaturas.index(max_temp) + 1
        dia_min = self.temperaturas.index(min_temp) + 1
        return max_temp, dia_max, min_temp, dia_min

    def mostrar_dias_sobre_promedio(self, promedio):
        print("\nDías con temperatura por encima del promedio:")
        for i, temp in enumerate(self.temperaturas):
            if temp > promedio:
                print(f" - Día {i+1}: {temp}°C")

    def mostrar_alertas(self):
        for i, temp in enumerate(self.temperaturas):
            if temp > 40 or temp < 0:
                print(f"¡Cuidado! Temperatura extrema día {i+1}: {temp}°C")

def main():
    analizador = AnalizadorTemperaturas()
    analizador.obtener_temperaturas()

    promedio = analizador.calcular_promedio()
    print(f"\nPromedio semanal: {promedio:.2f}°C")

    max_temp, dia_max, min_temp, dia_min = analizador.encontrar_max_min()
    print(f"Temperatura máxima: {max_temp}°C (Día {dia_max})")
    print(f"Temperatura mínima: {min_temp}°C (Día {dia_min})")

    analizador.mostrar_dias_sobre_promedio(promedio)
    analizador.mostrar_alertas()

if __name__ == "__main__":
    main()
