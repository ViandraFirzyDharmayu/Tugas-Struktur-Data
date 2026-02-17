game = GameOfLife(5, 5)

# Pola awal
game.setAlive(2, 1)
game.setAlive(2, 2)
game.setAlive(2, 3)

print("Generasi 0:")
game.display()

for i in range(4):
    game.nextGeneration()
    print(f"Generasi {i+1}:")
    game.display()
