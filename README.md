# Cross the Road Game 

Cross the Road is a simple arcade game built using Python and the Turtle graphics library. The objective of the game is to help the turtle cross the road while avoiding incoming cars. The player progresses through levels, and the game ends when the turtle is hit by a car or reaches the maximum level.
I created this project while learning Python to practice working with object-oriented programming, game loops, and event handling.

## Features 🚀 

* Player-controlled turtle that moves up and down.
* Randomly generated cars moving across the screen.
* Increasing difficulty with each level.
* Display of the current level.
* Game over and win messages with an option to restart. 

## Controls 🎮  

* Up Arrow - Move the turtle up
* Down Arrow - Move the turtle down
* y - Restart the game after losing
* n - Quit the game after losing

## Requirements 📌  

- Python 3.x  
- `turtle` module (included in Python by default)  

## How to Run

1. Clone this repository or download the source code:  
   ```
   git clone https://github.com/nbezverkhaya/cross_the_road_game.git
   cd cross-the-road-game
    ```
2. Install dependencies (if required):
   ```
   pip install -r requirements.txt
    ```
3. Run the game with:  
   ```
   python main.py
    ```
4. Enjoy playing! 🎉

## How to Play ▶️ 

* Use the arrow keys to move the turtle.
* Avoid getting hit by the cars.
* Reach the finish line at the top to advance to the next level.
* The speed of the cars increases as levels progress.
* If you reach level 4, you win the game!
* If you lose, you can restart by pressing Y or quit by pressing N.

## Project Structure

Cross-the-Road-Game/
│── main.py              # Main game logic
│── myturtle.py          # Player-controlled turtle class
│── carmanager.py        # Car movement and generation
│── levelboard.py        # Display level and game messages
│── requirements.txt     # Dependencies (if needed)
│── README.md            # Project documentation

## License

This project is open-source and available under the MIT [License](License.txt).
