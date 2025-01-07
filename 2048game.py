import random

# Function to initialize the game board
def create():
    """
    Initializes the game board (4x4 matrix) and adds two tiles to start the game.
    
    Returns:
        list: The initial game board with two tiles (either 2 or 4) placed at random positions.
    """
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

# Function to display the current state of the board
def display(board):
    """
    Displays the current state of the game board.
    
    Args:
        board (list): The current game board.
    """
    for row in board:
        print("\t".join(map(str, row)))
    print("\n")

# Function to add a new tile (2 or 4) at a random empty spot on the board
def add_new_tile(board):
    """
    Adds a new tile (2 or 4) to a random empty position on the board.
    
    Args:
        board (list): The current game board.
    """
    empty_positions = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if not empty_positions:
        return
    i, j = random.choice(empty_positions)
    board[i][j] = 2 if random.random() < 0.9 else 4

# Function to merge a single line of the board
def merge(line):
    """
    Merges a single row or column in the game, following 2048 game rules.
    
    Args:
        line (list): A row or column from the board.
    
    Returns:
        list: The merged row or column.
    """
    non_zero = [x for x in line if x != 0]
    for i in range(len(non_zero) - 1):
        if non_zero[i] == non_zero[i + 1]:
            non_zero[i] *= 2
            non_zero[i + 1] = 0
    non_zero = [x for x in non_zero if x != 0]
    return non_zero + [0] * (len(line) - len(non_zero))

# Function to move the tiles to the left (merge them accordingly)
def move_left(board):
    """
    Moves the tiles to the left on the board and merges them accordingly.
    
    Args:
        board (list): The current game board.
    """
    for r in range(4):
        board[r] = merge(board[r])
    add_new_tile(board)

# Function to move the tiles to the right (merge them accordingly)
def move_right(board):
    """
    Moves the tiles to the right on the board and merges them accordingly.
    
    Args:
        board (list): The current game board.
    """
    for r in range(4):
        board[r] = merge(board[r][::-1])[::-1]
    add_new_tile(board)

# Function to move the tiles up (merge them accordingly)
def move_up(board):
    """
    Moves the tiles up on the board and merges them accordingly.
    
    Args:
        board (list): The current game board.
    """
    for c in range(4):
        column = [board[r][c] for r in range(4)]
        column = merge(column)
        for r in range(4):
            board[r][c] = column[r]
    add_new_tile(board)

# Function to move the tiles down (merge them accordingly)
def move_down(board):
    """
    Moves the tiles down on the board and merges them accordingly.
    
    Args:
        board (list): The current game board.
    """
    for c in range(4):
        column = [board[r][c] for r in range(4)]
        column = merge(column[::-1])[::-1]
        for r in range(4):
            board[r][c] = column[r]
    add_new_tile(board)

# Check if the game has been won
def game_win(board, target):
    """
    Checks if the player has won the game by reaching the target value.
    
    Args:
        board (list): The current game board.
        target (int): The target value to reach for winning.
    
    Returns:
        bool: True if the game is won, False otherwise.
    """
    for row in board:
        if target in row:
            return True
    return False

# Check if the game is over (no more valid moves)
def game_over(board):
    """
    Checks if the game is over (no more valid moves or empty spots).
    
    Args:
        board (list): The current game board.
    
    Returns:
        bool: True if the game is over, False otherwise.
    """
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return False
            if c < 3 and board[r][c] == board[r][c + 1]:
                return False
            if r < 3 and board[r][c] == board[r + 1][c]:
                return False
    return True

# Main function to run the game
def play_game():
    """
    Runs the main game loop where the player interacts with the game board.
    """
    target = 2048  # Set target score for the game to be won
    board = create()

    while True:
        display(board)

        # Check if the game is over
        if game_over(board):
            print("Game Over! Sorry, try again.")
            break

        # Check if the game is won
        if game_win(board, target):
            print(f"Congrats! You've won by reaching {target}.")
            break

        # Player's move input
        print("Use a, b, c, d to move or q to quit.")
        move = input("Enter move (a-left, b-right, c-up, d-down, q-quit): ").strip()

        if move == 'a':
            move_left(board)
        elif move == 'b':
            move_right(board)
        elif move == 'c':
            move_up(board)
        elif move == 'd':
            move_down(board)
        elif move == 'q':
            print("Game has been quit.")
            break
        else:
            print("Invalid input. Please enter a valid move (a, b, c, d, q).")
            continue  # Ensures the loop continues on invalid input
