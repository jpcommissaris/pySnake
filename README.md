# pySnake
- 2 player snake game written in Python
- Majority of this was written in 2019

## How to play
- P1 uses arrow keys, P2 uses AWSD
- Running into a wall or any snake causes defeat.
- Eat apples to grow
- Trap your opponent & score points!

## Installing Requirements
- Python 3.x
- Add venv (recommended): `python3 -m venv venv`
- `source venv/bin/activate`
- Required dependencies (install via `pip`):
  ```bash
  pip install -r requirements.txt
  ```
- Optional (Pylance): Select this venv as interpreter in vscode
- Optional: use "Black" as formatter

## Setup the game
- Inside your venv. Run `main.py`
- You can change the speed via the SPEED const in `main.py`
- Advanced: You can change the board size via self.length & self.width (along with other consts) in `board.py`