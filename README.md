# Kombat_Game; intro to programming course's mini project, for beginners

# A general info about the project

This project is about a game which will be played by  two players in a turn-based manner. In each turn, one of the player's hero will attack the other player's hero. An attack may be successful by a certain chance rate. If an attack is successful, the attacked player's health
points will decrease by the magnitude of the attack which will be decided by the attacking
player. The first player whose health points become zero or negative will lose the game. Ini
tially, each player's hero will have 100 health points. The game will continue in a turn-based
manner until one of the players loses.

# The tested knoweledge

*Getting input from the user
*loops
*Functions(void and fruitfull)
*Random module
*If statement

# The installation and usage instruction (for users)

*For the installation

1/Clone the repository to your local machine:
git clone https://github.com/your-username/Kombat_Game.git

2/Navigate to the project directory:
cd Kombat_Game

*For the usage

1/Run the game python script:
python Kombat_Game.py

2/Follow the on-screen prompts to:

.Enter the names of the two players' heroes.
.Choose attack magnitudes when prompted.
.Play the game in a turn-based manner until one player loses.

3/After each game, you will be prompted to play again or exit.

4/Enjoy battling against your friend in this turn-based combat game!

**Make sure you have Python installed on your system.
**The game runs in the console/terminal. Ensure you have a compatible terminal emulator to play the game.

# The installation and usage instruction (for contributors)
*Cloning the Repository

1/Fork the repository to your GitHub account by clicking on the "Fork" button at the top right corner of the repository page

2/Clone your forked repository to your local machine:
git clone https://github.com/your-username/Kombat_Game.git

3/Navigate to the project directory:
cd Kombat_Game

*Setting Up the Development Environment

1/Create a virtual environment for the project (optional but recommended)
python -m venv venv

2/Activate the virtual environment:
On windows:   venv\Scripts\activate
On macOS/Linux:  source venv/bin/activate

3/Install project dependencies:
pip install -r requirements.txt

*Running the Game

1/Run the game Python script:
python Kombat_Game.py

2/Follow the on-screen prompts to play the game or make changes to the code.

*Contributing

1/Create a new branch for your feature/improvement:
git checkout -b feature/improvement

2/Make your changes to the code.

3/Commit your changes:
git commit -am 'Add new feature'  # Replace 'Add new feature' with a descriptive commit message

4/Push your changes to your forked repository:
git push origin feature/improvement

5/Create a new Pull Request on the original repository's GitHub page.

# Known issues
The main code can be simpler and distributed over other functions.

