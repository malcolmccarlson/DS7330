import pandas as pd


# This is the board presented to the end users
# It has the the mapping of the board
def numbered_board():
    print("   1 | 2  | 3  \n",
          "-------------\n",
          "  4 | 5 | 6  \n",
          "-------------\n",
          "  7 | 8  | 9  \n")

# Player Input
# This sets the which player is X and which is O
def get_input():
    p1 = input("Player 1: Please enter an x or an o. ")
    p2 = ''
    if p1 == 'x':
        p2 = 'o'

    if p1 == 'o':
        p2 = 'x'
    return p1, p2


# Generate Board as a dataframe
# This dataframe is where the game play will be captured
def create_board():
    data={"c1":[0, 0, 0],
          "c2":[0, 0, 0],
          "c3":[0, 0, 0]}
    boarddf = pd.DataFrame(data, columns=["c1", "c2", "c3"])
    return boarddf


# Board mapping to location value, row and column
def board_mapping(locNum, df):
    if locNum == 1:
        locval = df.at[0, "c1"]
        brow = 0
        bcolumn = "c1"
        return locval, brow, bcolumn
    elif locNum == 2:
        locval = df.at[0, "c2"]
        brow = 0
        bcolumn = "c2"
        return locval, brow, bcolumn
    elif locNum == 3:
        locval = df.at[0, "c3"]
        brow = 0
        bcolumn = "c3"
        return locval, brow, bcolumn
    elif locNum == 4:
        locval = df.at[1, "c1"]
        brow = 1
        bcolumn = "c1"
        return locval, brow, bcolumn
    elif locNum == 5:
        locval = df.at[1, "c2"]
        brow = 1
        bcolumn = "c2"
        return locval, brow, bcolumn
    elif locNum == 6:
        locval = df.at[1, "c3"]
        brow = 1
        bcolumn = "c3"
        return locval, brow, bcolumn
    elif locNum == 7:
        locval = df.at[2, "c1"]
        brow = 2
        bcolumn = "c1"
        return locval, brow, bcolumn
    elif locNum == 8:
        locval = df.at[2, "c2"]
        brow = 2
        bcolumn = "c2"
        return locval, brow, bcolumn
    elif locNum == 9:
        locval = df.at[2, "c3"]
        brow = 2
        bcolumn = "c3"
        return locval, brow, bcolumn
    else:
        print("Error.  Should not see this.")


# Pass in player 1,2  character choices and a new board
def playgame(plval, p2val, boardInstance):
    while True:
        p1_loc = input("Player 1.  Make your move!")
        p1locval, p1row, p1column = board_mapping(p1_loc, boardInstance)
        print(p1locval, p1row, p1column)
        if p1locval == 0:
            boardInstance.loc[p1row, p1column]=plval
            p1testresult = testforwin(boardInstance)
            print(boardInstance)
            if p1testresult is True:
                print("Player 1 Wins")
                return True
        else:
            print("Slot {} is taken.  Choose another.".format(p1_loc))
            playgame(plval, p2val, boardInstance)
        p2_loc = input("Player 2.  Make your move!")
        p2locval, p2row, p2column = board_mapping(p2_loc, boardInstance)
        if p2locval == 0:
            boardInstance.loc[p2row, p2column]=p2val
            p2testresult = testforwin(boardInstance)
            print(boardInstance)
            if p2testresult is True:
                print("Player 2 Wins")
                return True
        else:
            print("Slot {} is taken.  Choose another.").format(p2_loc)
            playgame(plval, p2val, boardInstance)


# Test for Win
# This method gets run after each player makes their move
def testforwin(df):
    if df.at[0, "c1"] == df.at[0, "c2"] == df.at[0, "c3"]:
        return True
    elif df.at[1, "c1"] == df.at[1, "c2"] == df.at[1, "c3"]:
        return True
    elif df.at[2, "c1"] == df.at[2, "c2"] == df.at[2, "c3"]:
        return True
    elif df.at[0, "c1"] == df.at[1, "c1"] == df.at[2, "c1"]:
        return True
    elif df.at[0, "c2"] == df.at[1, "c2"] == df.at[2, "c2"]:
        return True
    elif df.at[0, "c3"] == df.at[1, "c3"] == df.at[2, "c3"]:
        return True
    elif df.at[0, "c1"] == df.at[1, "c2"] == df.at[2, "c3"]:
        return True
    elif df.at[0, "c3"] == df.at[1, "c2"] == df.at[2, "c1"]:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Welcome to Tic Tac Toe!")
    pl1, pl2 = get_input()
    bd = create_board()
    print("Player 1 is {}.".format(pl1), "Player 2 is {}.".format(pl2))
    print("The board layout is as follows:")
    numbered_board()
    print("Each player will get a turn to choose a number for their move.\nGood Luck!")
    playgame(pl1, pl2, bd)
