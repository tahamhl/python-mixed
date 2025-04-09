import random
from collections import Counter

class MontyHallSimulator:
    def __init__(self, num_simulations=10000):
        self.num_simulations = num_simulations
        self.results_switch = []
        self.results_stay = []
    
    def play_game(self, switch_door=True):
        # Kapıları hazırla (0: keçi, 1: araba)
        doors = [0, 0, 1]
        random.shuffle(doors)
        
        # İlk seçim
        first_choice = random.randint(0, 2)
        
        # Monty'nin açabileceği kapıları belirle
        available_doors = [i for i in range(3) 
                         if i != first_choice and doors[i] == 0]
        
        # Monty bir keçi kapısını açar
        monty_opens = random.choice(available_doors)
        
        if switch_door:
            # Kalan kapıya geç
            final_choice = [i for i in range(3) 
                          if i != first_choice and i != monty_opens][0]
        else:
            # İlk seçimde kal
            final_choice = first_choice
            
        return doors[final_choice] == 1  # Araba kazandık mı?
    
    def run_simulation(self):
        for _ in range(self.num_simulations):
            self.results_switch.append(self.play_game(switch_door=True))
            self.results_stay.append(self.play_game(switch_door=False))
    
    def get_results(self):
        switch_wins = Counter(self.results_switch)[True]
        stay_wins = Counter(self.results_stay)[True]
        
        switch_win_rate = switch_wins / self.num_simulations * 100
        stay_win_rate = stay_wins / self.num_simulations * 100
        
        return {
            "switch_win_rate": switch_win_rate,
            "stay_win_rate": stay_win_rate,
            "total_games": self.num_simulations
        }

# Test çalıştırması
simulator = MontyHallSimulator(10000)
simulator.run_simulation()
results = simulator.get_results()

print("Monty Hall Problemi Simülasyon Sonuçları")
print(f"Toplam oyun sayısı: {results["total_games"]}")
print(f"Kapı değiştirince kazanma oranı: {results["switch_win_rate"]:.1f}%")
print(f"Kapıda kalınca kazanma oranı: {results["stay_win_rate"]:.1f}%")