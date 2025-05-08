# Go – The Strategy Game

### Goban  
The **Goban** is a square board used to play Go, typically with dimensions 9×9, 13×13, or 19×19. It consists of **intersections** formed by rows (numbered from 1 to N) and columns (labeled from A to S), where players place their stones.  

### Intersections and Stones  
An **intersection** is defined by its column and row identifiers (e.g., 'C3'). It can be:  
- **empty**,  
- **occupied by a white stone ('O')**,  
- or **occupied by a black stone ('X')**.  

Players alternate turns placing stones on free intersections. Once placed, stones cannot be moved.

### Chains, Liberties and Territories  
- A **chain** is a group of one or more connected stones of the same color.  
- A **liberty** of a stone is any directly adjacent empty intersection. If a stone or a chain loses all its liberties, it is captured and removed from the board.  
- A **territory** is a group of connected empty intersections completely surrounded by stones of a single player.  

## Game Rules  
The game starts with an empty board. The **black player plays first**, and turns alternate. Each turn, a player may:  
- **place a stone**, or  
- **pass** (i.e., skip their turn).  

There are two important restrictions:  
1. **Suicide**: Players cannot place a stone in a way that would immediately remove all liberties of their own stone/chain (unless it results in capturing opponent stones).  
2. **Repetition (Ko rule)**: A move that would recreate a previous board state is illegal.

The game ends when both players pass consecutively.  

## 🧪 Tests

Automated tests are provided using the `pytest` framework.

1. Install the testing module:
```bash
pip install pytest
```

2. Run the available tests:
```bash
pytest test_public.py
pytest test_private.py
```
