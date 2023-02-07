board = {
    "tl": "_",  "tm": "_", "tr": "_",
    "ml": "_",  "m": "_", "mr": "_",
    "bl": "_",  "bm": "_", "br": "_"
}
player_1_turn = True
p1_wins = 0
p2_wins = 0
stalemates = 0
wins = "P1 wins: " + str(p1_wins) + "\nP2 wins: " + str(p2_wins)
print(wins)

print("""
To fill in a space, first type in the initial letter of the vertical position (t)op, ,(m)id or (b)ottom.
Then input the initial letter of the horizontal position (l)eft, (m)id or (r)ight.
To select the center space simply input "m".
for example typing lr will fill in the (l)ower (r)ight space of the board.
""")
while True:


    if "_" not in board.values():
        print("Its a tie")
        board = {
            "tl": "_", "tm": "_", "tr": "_",
            "ml": "_", "m": "_", "mr": "_",
            "bl": "_", "bm": "_", "br": "_"
        }
        player_1_turn = True
        stalemates += 1
        print("P1 wins: " + str(p1_wins) + "\nP2 wins: " + str(p2_wins) + "\nTies: " + str(stalemates))



    print(board["tl"] + board["tm"] + board["tr"])
    print(board["ml"] + board["m"] + board["mr"])
    print(board["bl"] + board["bm"] + board["br"])


    if (board["tl"] == board["tm"] == board["tr"] == "X" or board["ml"] == board["m"] == board["mr"] == "X" or
        board["bl"] == board["bm"] == board["br"] == "X" or board["tl"] == board["ml"] == board["bl"] == "X" or
        board["tm"] == board["m"] == board["bm"] == "X" or board["tr"] == board["mr"] == board["br"] == "X" or
        board["bl"] == board["m"] == board["tr"] == "X" or board["br"] == board["m"] == board["tl"] == "X"):
        print("player 1 has won!")
        p1_wins += 1
        print("P1 wins: " + str(p1_wins) + "\nP2 wins: " + str(p2_wins) + "\nTies: " + str(stalemates))
        player_1_turn = True
        board = {
            "tl": "_", "tm": "_", "tr": "_",
            "ml": "_", "m": "_", "mr": "_",
            "bl": "_", "bm": "_", "br": "_"
        }

    elif (board["tl"] == board["tm"] == board["tr"] == "O" or board["ml"] == board["m"] == board["mr"] == "O" or
          board["bl"] == board["bm"] == board["br"] == "O" or board["tl"] == board["ml"] == board["bl"] == "O" or
          board["tm"] == board["m"] == board["bm"] == "O" or board["tr"] == board["mr"] == board["br"] == "O" or
          board["bl"] == board["m"] == board["tr"] == "O" or board["br"] == board["m"] == board["tl"] == "O"):
        print("player 2 has won!")
        p2_wins += 1
        print("P1 wins: " + str(p1_wins) + "\nP2 wins: " + str(p2_wins) + "\nTies: " + str(stalemates))
        player_1_turn = True
        board = {
            "tl": "_", "tm": "_", "tr": "_",
            "ml": "_", "m": "_", "mr": "_",
            "bl": "_", "bm": "_", "br": "_"
        }

    elif player_1_turn:
        move = input("Make your move player one: ").lower()
        try:
            if board[move] == "X" or board[move] == "O":
                print("That space is already taken infidel!")
        except KeyError:
            print("That is not a valid input")
        if move in board.keys():
            board[move] = "X"
            player_1_turn = False

    else:
        move = input("Make your move player two: ").lower()
        try:
            if board[move] == "X" or board[move] == "O":
                print("That space is already taken!")
        except KeyError:
            print("That is not a valid input")
        if move in board.keys():
            board[move] = "O"
            player_1_turn = True


