# lakshya rana.
# script has been protected by copyright.
# all rights belongs to me, complete coding is handwritten by me.
# please don't copy the codes its completely my hardwork.
# run it, enjoy it, play it, review it.

import random 

NUM_SQUARES = 63
TAB = "\t"                    
EMPTY = " "
Y_0 = "|"
X_3 = "----"
TIE = "TIE"


def display_instruct():
    """Display game instructions."""  
    print \
    """
                               INSTRUCTIONS

    Welcome to the greatest intellectual challenge of all time: ABBA-DABBA-JABBA.  
    This will be a showdown between your human brain and my silicon processor.  
    
    You will make your move known by enter_0ing a number, 0 - 62.  The move 
    will correspond to the board position as illustrated:
    
    starting: 0     ending: 1
    starting: 0     ending: 9
    starting: 9     ending: 10
    starting: 1     ending: 10
    
                    00----01
                    |      |
                    |      |
                    |      |
                    09----10
                    
    Whoever scores the last move, owns that block.

                    00 ---- 01
                    |       |
                    |   C   |
                    |       |
                    09 ---- 10

    At the end whoever scores higher wins the game.

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """


def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in("y", "n"):
        response = raw_input(question).lower()
        if response not in("y", "n"):
            print "\nPlease make your choice in either 'y' or 'n'."
    return response


def ask_number(question):
    """Ask for a number within a range."""
    response = None
    while response not in("1", "2"):
        response = raw_input(question)
        if response not in("1", "2"):
            print "\nIllegal action......you dumb HOMOSAPIEN!!!!....register different."
    return response


def ask_name(question):
    """Ask name from the user."""
    name = raw_input(question)
    while name in EMPTY:
        print "\nDon't leave this field empty, enter your name."
        name = raw_input(question)
    return name


def match_alias_0():
    """Ask to change name from human."""
    human = None
    while human == None:
        human = ask_name("\nEnter your name 'human', i want to know my opponent:")
        human = human.upper()
        human_0 = human[0]
        if human == computer:
            print "\nThe name you entered is same as that of me."
            print "\nPlease enter different name, you copy cat."
            human = None
    while human_0 == computer[0]:
        print "\nYour name's first letter and mine's is same."
        print "\nEnter different first letter than me."
        human_0 = ask_name("\nEnter different single letter only:")
        human_0 = human_0[0]
        human_0 = human_0.upper()

    print "\nYour name is", human, "and your house name will be", human_0, "."
    print "\nBattle between", human, "and", computer, "begins now."
    
    return human, human_0


def match_alias_1():
    """Ask to change name from both players."""
    player_1 = None
    player_2 = None
    while player_1 == None:
        player_1 = ask_name("\nInsert the name of first player:")
        player_1 = player_1.upper()
        player_2 = ask_name("\nInsert the name of second player:")
        player_2 = player_2.upper()
        player_1_0 = player_1[0]
        player_2_0 = player_2[0]
        if player_1 == player_2:
            print "\nThe names of both player are same.please enter different names."
            player_1 = None
    while player_1_0 == player_2_0:
        print "\nThe first letter of name of both players is same.Enter different first letter."
        print "\n", player_2, "!!..."
        player_2_0 = ask_name("\nEnter different single letter only:")
        player_2_0 = player_2_0[0]
        player_2_0 = player_2_0.upper()

    print "\nFirst player is", player_1, "and your house name will be", player_1_0, "."
    print "\nSecond player is", player_2, "and your house name will be", player_2_0, "."
    print "\nBattle between", player_1, "and", player_2, "begins now."
    
    return player_1, player_2, player_1_0, player_2_0


def pieces_0():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("\nDo you require the first move? (y/n):")
    if go_first == "y":
        print "\nThen take the first move.you will need it\n"
        turn = human
    else:
        print "\nYour bravery will be your undoing...i will go first\n"
        turn = computer
    return turn


def pieces_1():
    """Determine if player 1 or player 2 goes first."""
    
    print "\nWho goes first....\n\n1.", player_1, "\t\t2.", player_2
    
    go_first = ask_number("\nWhich one... '1' or '2':")
    if go_first == "1":
        turn = player_1
    else:
        turn = player_2
        
    print "\n", turn, "goes first..."
    
    return turn


def initial_local_0():
    """Provides initial values to the local variables with computer battle."""
    rank_comp = 0
    rank_homo = 0
    tally_comp = 0
    tally_homo = 0
    human_score = 1500
    cyber_score = 1500

    return rank_comp, rank_homo, human_score, cyber_score, tally_comp, tally_homo


def initial_local_1():
    """Provides initial values to the local variables with player battle."""
    rank_player_1 = 0
    rank_player_2 = 0
    tally_player_1 = 0
    tally_player_2 = 0
    player_1_score = 1500
    player_2_score = 1500

    return rank_player_1, rank_player_2, player_1_score, player_2_score, tally_player_1, tally_player_2


def block_name():
    """Create space for first letter of the name."""
    block = []
    for square in range(NUM_SQUARES):
        block.append(EMPTY)
    return block


def horizon_board():
    """Create horizontal board."""
    board_X = []
    for square in range(NUM_SQUARES):
        board_X.append(TAB)
    return board_X


def verti_board():
    """Create vertical board."""
    board_Y = []
    for square in range(NUM_SQUARES):
        board_Y.append(EMPTY)
    return board_Y


def legal_moves(board_X, board_Y):
    """Make list of legal moves."""
    moves_X = []
    moves_Y = []
    
    for square in range(NUM_SQUARES):
        if board_X[square] == TAB:
            moves_X.append(square) 

    for square in range(NUM_SQUARES):
        if board_Y[square] == EMPTY:
            moves_Y.append(square)
    return moves_X, moves_Y


def mark_stack(board_X, board_Y):
    """Removes invalid moves."""
    legal = legal_moves(board_X, board_Y)
    mark_X = legal[0]
    mark_Y = legal[1]
    
    for i in range(0, 55, 9):
        mark_X.remove(i)

    for i in range(54, 63, 1):
        mark_Y.remove(i)
    return mark_X, mark_Y

        
def char_moves():
    """Converts integer move to character."""
    moves = []
    for square in range(NUM_SQUARES):
        moves.append(str(square))
    return moves


def ask_human(string):
    """Asks human to make the move."""
    moves = char_moves()
    report = None
    while report not in moves:
        report = raw_input(string)
        if report not in moves:
            print "\nINVAlID MOVE."
            print "\nOh!! stupid human, please enter a valid number."
    return report


def display_board(board_Y, board_X, block):
    """Display the board."""
    print "\n\t00", board_X[01], "01", board_X[02], "02", board_X[03], "03", board_X[04], "04", board_X[05], "05", board_X[06], "06", board_X[07], "07", board_X[ 8], "08"
    print "\t", board_Y[00], "\t", board_Y[01], "\t", board_Y[02], "\t", board_Y[03], "\t", board_Y[04], "\t", board_Y[05], "\t", board_Y[06], "\t", board_Y[07], "\t", board_Y[ 8]
    print "\t", board_Y[00], " ", block[00], " ", board_Y[01], " ", block[01], " ", board_Y[02], " ", block[02], " ", board_Y[03], " ", block[03], " ", board_Y[04], " ", block[04], " ", board_Y[05], " ", block[05], " ", board_Y[06], " ", block[06], " ", board_Y[07], " ", block[07], " ", board_Y[ 8]
    print "\t", board_Y[00], "\t", board_Y[01], "\t", board_Y[02], "\t", board_Y[03], "\t", board_Y[04], "\t", board_Y[05], "\t", board_Y[06], "\t", board_Y[07], "\t", board_Y[ 8]
    print "\t09", board_X[10], "10", board_X[11], "11", board_X[12], "12", board_X[13], "13", board_X[14], "14", board_X[15], "15", board_X[16], "16", board_X[17], "17"
    print "\t", board_Y[ 9], "\t", board_Y[10], "\t", board_Y[11], "\t", board_Y[12], "\t", board_Y[13], "\t", board_Y[14], "\t", board_Y[15], "\t", board_Y[16], "\t", board_Y[17]
    print "\t", board_Y[ 9], " ", block[ 9], " ", board_Y[10], " ", block[10], " ", board_Y[11], " ", block[11], " ", board_Y[12], " ", block[12], " ", board_Y[13], " ", block[13], " ", board_Y[14], " ", block[14], " ", board_Y[15], " ", block[15], " ", board_Y[16], " ", block[16], " ", board_Y[17]
    print "\t", board_Y[ 9], "\t", board_Y[10], "\t", board_Y[11], "\t", board_Y[12], "\t", board_Y[13], "\t", board_Y[14], "\t", board_Y[15], "\t", board_Y[16], "\t", board_Y[17]
    print "\t18", board_X[19], "19", board_X[20], "20", board_X[21], "21", board_X[22], "22", board_X[23], "23", board_X[24], "24", board_X[25], "25", board_X[26], "26"
    print "\t", board_Y[18], "\t", board_Y[19], "\t", board_Y[20], "\t", board_Y[21], "\t", board_Y[22], "\t", board_Y[23], "\t", board_Y[24], "\t", board_Y[25], "\t", board_Y[26]
    print "\t", board_Y[18], " ", block[18], " ", board_Y[19], " ", block[19], " ", board_Y[20], " ", block[20], " ", board_Y[21], " ", block[21], " ", board_Y[22], " ", block[22], " ", board_Y[23], " ", block[23], " ", board_Y[24], " ", block[24], " ", board_Y[25], " ", block[25], " ", board_Y[26]
    print "\t", board_Y[18], "\t", board_Y[19], "\t", board_Y[20], "\t", board_Y[21], "\t", board_Y[22], "\t", board_Y[23], "\t", board_Y[24], "\t", board_Y[25], "\t", board_Y[26]     
    print "\t27", board_X[28], "28", board_X[29], "29", board_X[30], "30", board_X[31], "31", board_X[32], "32", board_X[33], "33", board_X[34], "34", board_X[35], "35"
    print "\t", board_Y[27], "\t", board_Y[28], "\t", board_Y[29], "\t", board_Y[30], "\t", board_Y[31], "\t", board_Y[32], "\t", board_Y[33], "\t", board_Y[34], "\t", board_Y[35]
    print "\t", board_Y[27], " ", block[27], " ", board_Y[28], " ", block[28], " ", board_Y[29], " ", block[29], " ", board_Y[30], " ", block[30], " ", board_Y[31], " ", block[31], " ", board_Y[32], " ", block[32], " ", board_Y[33], " ", block[33], " ", board_Y[34], " ", block[34], " ", board_Y[35]
    print "\t", board_Y[27], "\t", board_Y[28], "\t", board_Y[29], "\t", board_Y[30], "\t", board_Y[31], "\t", board_Y[32], "\t", board_Y[33], "\t", board_Y[34], "\t", board_Y[35] 
    print "\t36", board_X[37], "37", board_X[38], "38", board_X[39], "39", board_X[40], "40", board_X[41], "41", board_X[42], "42", board_X[43], "43", board_X[44], "44"
    print "\t", board_Y[36], "\t", board_Y[37], "\t", board_Y[38], "\t", board_Y[39], "\t", board_Y[40], "\t", board_Y[41], "\t", board_Y[42], "\t", board_Y[43], "\t", board_Y[44]
    print "\t", board_Y[36], " ", block[36], " ", board_Y[37], " ", block[37], " ", board_Y[38], " ", block[38], " ", board_Y[39], " ", block[39], " ", board_Y[40], " ", block[40], " ", board_Y[41], " ", block[41], " ", board_Y[42], " ", block[42], " ", board_Y[43], " ", block[43], " ", board_Y[44]
    print "\t", board_Y[36], "\t", board_Y[37], "\t", board_Y[38], "\t", board_Y[39], "\t", board_Y[40], "\t", board_Y[41], "\t", board_Y[42], "\t", board_Y[43], "\t", board_Y[44]
    print "\t45", board_X[46], "46", board_X[47], "47", board_X[48], "48", board_X[49], "49", board_X[50], "50", board_X[51], "51", board_X[52], "52", board_X[53], "53"
    print "\t", board_Y[45], "\t", board_Y[46], "\t", board_Y[47], "\t", board_Y[48], "\t", board_Y[49], "\t", board_Y[50], "\t", board_Y[51], "\t", board_Y[52], "\t", board_Y[53]
    print "\t", board_Y[45], " ", block[45], " ", board_Y[46], " ", block[46], " ", board_Y[47], " ", block[47], " ", board_Y[48], " ", block[48], " ", board_Y[49], " ", block[49], " ", board_Y[50], " ", block[50], " ", board_Y[51], " ", block[51], " ", board_Y[52], " ", block[52], " ", board_Y[53]
    print "\t", board_Y[45], "\t", board_Y[46], "\t", board_Y[47], "\t", board_Y[48], "\t", board_Y[49], "\t", board_Y[50], "\t", board_Y[51], "\t", board_Y[52], "\t", board_Y[53]
    print "\t54", board_X[55], "55", board_X[56], "56", board_X[57], "57", board_X[58], "58", board_X[59], "59", board_X[60], "60", board_X[61], "61", board_X[62], "62\n"


    # problem coming here for switching turns.
    # now solved................... bang-bang.                 oct. 1 2o16 12:17
def next_turn_0(turn, move, move_0, board_Y, board_X):         # 10/1/2016  12:17 AM
    """Switch turns accordingly against computer."""

    # updated.
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X) 
    duet_0 = (move, move + 9)
    duet_1 = (move - 1, move)
    if duet_0 in X_box_3 and duet_1 in Y_box_3:
        if turn == computer:
            print "\n\nOh!!! my house......... again my turn....."
            return computer
        else:
            print "\n\nOh!!! damn, ......your house....... your turn again....."
            return human
        
    if move_0 == Y_0:
        duet_2 = (move + 1, move + 10)
        duet_3 = (move, move + 1)
    else:
        duet_2 = (move - 9, move)
        duet_3 = (move - 10, move - 9)
        
    if duet_2 in X_box_3 and duet_3 in Y_box_3:
        if turn == computer:
            print "\n\nOh!!! my house......... again my turn....."
            return computer
        else:
            print "\n\nOh!!! damn, ......your house....... your turn again....."
            return human
    else:
        if turn == computer:
            return human
        else:
            return computer


def next_turn_1(turn, move, move_0, board_Y, board_X):         # 10/1/2016  12:17 AM
    """Switch turns accordingly against player."""

    # updated.
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X) 
    duet_0 = (move, move + 9)
    duet_1 = (move - 1, move)
    if duet_0 in X_box_3 and duet_1 in Y_box_3:
        print "\n\n", turn, "'s house again his turn..."
        return turn
        
    if move_0 == Y_0:
        duet_2 = (move + 1, move + 10)
        duet_3 = (move, move + 1)
    else:
        duet_2 = (move - 9, move)
        duet_3 = (move - 10, move - 9)
        
    if duet_2 in X_box_3 and duet_3 in Y_box_3:
        print "\n\n", turn, "'s house again his turn..."
        return turn
        
    else:
        if turn == player_1:
            return player_2
        else:
            return player_1
    
        
def winner(block, tally_comp, tally_homo):
    """Determine the game winner against computer."""
    # mistake.
    if EMPTY not in block:
        if tally_homo > tally_comp:
            return human
        elif tally_comp > tally_homo:
            return computer
        elif tally_comp == tally_homo:
            return TIE
    return None

def congrat_winner(the_winner):
    """Congratulate the winner against computer."""
    
    print "\n",name.upper(),"WON.\n"
            print "No, no!  It cannot be!  Somehow you tricked me, human. \n" \
                  "But never again!  I, the computer, so swears it!"
    elif cyber_score > human_score:
        print "\nCOMPUTER WON.\n"
            print "As I predicted, human, I am triumphant once more.  \n" \
                  "Proof that computers are superior to humans in all regards."
        elif human_score == cyber_score:
            print "\nYou were most lucky, human, and somehow managed to tie me.  \n" \
                  "Celebrate today... for this is the best you will ever achieve."

def human_move(board_X, board_Y):
    """Get human move.""" 
    legal = legal_moves(board_X, board_Y)
    drop_move = (( 8,  9), ( 9,  8), (17, 18), (18, 17), (26, 27), (27, 26),
                 (35, 36), (36, 35), (44, 45), (45, 44), (53, 54), (54, 53))
    move = None
    while move == None:
        enter_0 = int(ask_human("\n\nWhere will you move your starting number? (0-62):"))
        enter_1 = int(ask_human("\nWhere will you move your ending number? (0-62):"))
        moves = (enter_0, enter_1)
        if enter_1 == enter_0 + 1:
            move = enter_1
            move_0 = X_3
            port = 0
        elif enter_0 == enter_1 + 1:
            move = enter_0
            move_0 = X_3
            port = 0
        elif enter_1 == enter_0 + 9:
            move = enter_0
            move_0 = Y_0
            port = 1
        elif enter_0 == enter_1 + 9:
            move = enter_1
            move_0 = Y_0
            port = 1
        else:
            move = None
            print "\nInvalid move, foolish human !, you can't make move there."
            continue
        
        if move not in legal[port]:
            move = None
            print "\nThis place is already occupied, foolish human!, choose another."
            continue
        
        if moves in drop_move:
            move = None
            print "\nInvalid move, foolish human !, you can't make move there."
            continue
        
        print "\nFine....\n"
        
        if move_0 == Y_0:
            board_Y[move] = move_0
        else:
            board_X[move] = move_0
        return move, move_0
        

def X_axis(board_X):
    """Determines horizontal board's mensuration."""
    line_X =  ((1, 10), (02, 11), (03, 12), (04, 13), (05, 14), (06, 15), (07, 16), ( 8, 17), 
              (10, 19), (11, 20), (12, 21), (13, 22), (14, 23), (15, 24), (16, 25), (17, 26),
              (19, 28), (20, 29), (21, 30), (22, 31), (23, 32), (24, 33), (25, 34), (26, 35),
              (28, 37), (29, 38), (30, 39), (31, 40), (32, 41), (33, 42), (34, 43), (35, 44),
              (37, 46), (38, 47), (39, 48), (40, 49), (41, 50), (42, 51), (43, 52), (44, 53),
              (46, 55), (47, 56), (48, 57), (49, 58), (50, 59), (51, 60), (52, 61), (53, 62))

    X_box_0 = ()
    X_box_1 = ()
    X_box_2 = ()
    X_box_3 = ()
    
    for row in line_X:
        if board_X[row[0]] == board_X[row[1]] == TAB:
            X_box_0 += (row[0], row[1]),         # a nice one.
        elif board_X[row[0]] != TAB and board_X[row[1]] == TAB:
            X_box_1 += (row[0], row[1]),
        elif board_X[row[0]] == TAB and board_X[row[1]] != TAB:
            X_box_2 += (row[0], row[1]),
        elif board_X[row[0]] == board_X[row[1]] != TAB:
            X_box_3 += (row[0], row[1]),
            
    return X_box_0, X_box_1, X_box_2, X_box_3
  

def Y_axis(board_Y):
    """Determines vertical board's mensuration."""
    line_Y = ((0, 01), (01, 02), (02, 03), (03, 04), (04, 05), (05, 06), (06, 07), (07,  8),
             ( 9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17),
             (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26),
             (27, 28), (28, 29), (29, 30), (30, 31), (31, 32), (32, 33), (33, 34), (34, 35),
             (36, 37), (37, 38), (38, 39), (39, 40), (40, 41), (41, 42), (42, 43), (43, 44),
             (45, 46), (46, 47), (47, 48), (48, 49), (49, 50), (50, 51), (51, 52), (52, 53))

    Y_box_0 = ()
    Y_box_1 = ()
    Y_box_2 = ()
    Y_box_3 = ()
    
    for row in line_Y:
        if board_Y[row[0]] == board_Y[row[1]] == EMPTY:
            Y_box_0 += (row[0], row[1]),
        elif board_Y[row[0]] != EMPTY and board_Y[row[1]] == EMPTY:
            Y_box_1 += (row[0], row[1]),
        elif board_Y[row[0]] == EMPTY and board_Y[row[1]] != EMPTY:
            Y_box_2 += (row[0], row[1]),
        elif board_Y[row[0]] == board_Y[row[1]] != EMPTY:
            Y_box_3 += (row[0], row[1]),

    return Y_box_0, Y_box_1, Y_box_2, Y_box_3


# mistake in it.
def first_segment(board_X, board_Y):
    """Prepares safe move for computer."""

    U_Y_box = ((-9, -8), (-8, -7), (-7, -6), (-6, -5),
               (-5, -4), (-4, -3), (-3, -2), (-2, -1))
    D_Y_box = ((54, 55), (55, 56), (56, 57), (57, 58),
               (58, 59), (59, 60), (60, 61), (61, 62))
    L_X_box = ((-1,  8), ( 8, 17), (17, 26),
               (26, 35), (35, 44), (44, 53))
    R_X_box = (( 9, 18), (18, 27), (27, 36),
               (36, 45), (45, 54), (54, 63))

    
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X)

    X_box   = (X_box_1, X_box_2)
    box_Y_0 = (Y_box_0, Y_box_1)
    box_Y_1 = (Y_box_0, Y_box_2)
    box_Y_2 = (Y_box_0, Y_box_1, Y_box_2)

    # right empty, 2 filled.
    for pair_1 in Y_box_0:
        for stack in X_box:
            for pair_0 in stack:
                if pair_0[0] == pair_1[1]:
                    # all condition.
                    match = (pair_0[0] + 1, pair_0[1] + 1)
                    for double in R_X_box:
                        if match == double :
                            move = pair_1[1]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_1) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_2) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
        
        # upper empty, 1 filled.
        for pair_0 in X_box_2:
            if pair_0[0] == pair_1[1]:
                # all condition.
                match = (pair_1[0] - 9, pair_1[1] - 9)
                for double in U_Y_box:
                    if match == double:
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
                if (match in Y_box_0) and (board_X[pair_0[0] - 9] == TAB):
                    move = pair_0[0]
                    move_0 = X_3
                    return move, move_0
                elif (match in Y_box_1) and (board_X[pair_0[0] - 9] == TAB):
                    move = pair_0[0]
                    move_0 = X_3
                    return move, move_0
                elif (match in Y_box_2) and (board_X[pair_0[0] - 9] == TAB):
                    move = pair_0[0]
                    move_0 = X_3
                    return move, move_0
                elif match in Y_box_0:
                    move = pair_0[0]
                    move_0 = X_3
                    return move, move_0
        # left empty, 2 filled.
        for stack in X_box:
            for pair_0 in stack:
                if pair_0[0] == pair_1[1]:
                    # all condition.
                    match = (pair_0[0] - 1, pair_0[1] - 1)
                    for double in L_X_box:
                        if match == double:
                            move = pair_1[0]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_1) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_2) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
        
        # below empty, 1 filed.
        for pair_0 in X_box_1:
            if pair_0[0] == pair_1[1]:
                # all condition.
                match = (pair_1[0] + 9, pair_1[1] + 9)
                for double in D_Y_box:
                    if match == double:
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0
                if (match in Y_box_0) and (board_X[pair_0[1] + 9] == TAB):
                    move = pair_0[1]
                    move_0 = X_3
                    return move, move_0
                elif (match in Y_box_1) and (board_X[pair_0[1] + 9] == TAB):
                    move = pair_0[1]
                    move_0 = X_3
                    return move, move_0
                elif (match in Y_box_2) and (board_X[pair_0[1] + 9] == TAB):
                    move = pair_0[1]
                    move_0 = X_3
                    return move, move_0
                elif match in Y_box_0:
                    move = pair_0[1]
                    move_0 = X_3
                    return move, move_0

    # both X empty.
    for pair_0 in X_box_0:
        
        # right empty, 2 left.
        # both Y empty.
        for stack in box_Y_0:
               # here is the culprit.
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    # all condition.
                    match = (pair_0[0] + 1, pair_0[1] + 1)
                    for double in R_X_box:
                        if match == double:
                            move = pair_1[1]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_1) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_2) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                
                # upper empty, 1 left.
        # both Y empty.
        for stack in box_Y_2:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    # all condition.
                    match = (pair_1[0] - 9, pair_1[1] - 9)
                    for double in U_Y_box:
                        if match == double:
                            move = pair_0[0]
                            move_0 = X_3
                            return move, move_0
                    if (match in Y_box_0) and (board_X[pair_0[0] - 9] == TAB):
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
                    elif (match in Y_box_1) and (board_X[pair_0[0] - 9] == TAB):
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
                    elif (match in Y_box_2) and (board_X[pair_0[0] - 9] == TAB):
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
                    elif match in Y_box_0:
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0

                # left empty, 2 left.
        # both Y empty.
        for stack in box_Y_1:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    # all condition.
                    match = (pair_0[0] - 1, pair_0[1] - 1)
                    for double in L_X_box:
                        if match == double:
                            move = pair_1[0]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_1) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif (match in X_box_2) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0

                # below empty, 1 left.
        # both Y empty.
        for stack in box_Y_2:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    # all condition.
                    match = (pair_1[0] + 9, pair_1[1] + 9)
                    for double in D_Y_box:
                        if match == double:
                            move = pair_0[1]
                            move_0 = X_3
                            return move, move_0
                    if (match in Y_box_0) and (board_X[pair_0[1] + 9] == TAB):
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0
                    elif (match in Y_box_1) and (board_X[pair_0[1] + 9] == TAB):
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0
                    elif (match in Y_box_2) and (board_X[pair_0[1] + 9] == TAB):
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0
                    elif match in Y_box_0:
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0


def second_segment(board_X, board_Y):
    """Prepares move of lowest harm to computer."""

    # the mechanism.
    
    least = []
    deck = ()
    
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X)
    
    for pair_0 in X_box_0:
        # first 2 segment box.
        for pair_1 in Y_box_3:
            if pair_0[0] == pair_1[1]:
                # check, fill horizontally above.
                board_X[pair_0[0]] = X_3
                # tuple, done moves.
                club_0 = ()
                # total filled boxes, assign 0.
                least_0 = 0
                # filling boxes.
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    # collecting all moves done.
                    club_0 += (last[0], last[1]),
                    least_0 += 1            # got total filled boxes.
                    last = last_segment(board_X, board_Y)
                board_X[pair_0[0]] = TAB    # undo main move.
                least.append(least_0)       # adding least to list.
                # main move with least added to tuple.
                deck += (least_0, pair_0[0], X_3),
                 # process of undoing all moves.

                for case_0 in club_0:
                    if case_0[1] == Y_0:
                        board_Y[case_0[0]] = EMPTY
                    elif case_0[1] == X_3:
                        board_X[case_0[0]] = TAB
                # check, fill horizontally below.
                board_X[pair_0[1]] = X_3
                club_1 = ()
                least_1 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_1 += (last[0], last[1]),
                    least_1 += 1
                    last = last_segment(board_X, board_Y)
                board_X[pair_0[1]] = TAB
                least.append(least_1)
                deck += (least_1, pair_0[1], X_3),
                for case_1 in club_1:
                    if case_1[1] == Y_0:
                        board_Y[case_1[0]] = EMPTY
                    else:
                        board_X[case_1[0]] = TAB

    # next 2 segment box.          
    for pair_2 in X_box_3:
        for pair_3 in Y_box_0:
            if pair_2[0] == pair_3[1]:
                board_Y[pair_3[0]] = Y_0
                club_2 = ()
                least_2 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_2 += (last[0], last[1]),
                    least_2 += 1
                    last = last_segment(board_X, board_Y)
                board_Y[pair_3[0]] = EMPTY
                least.append(least_2)
                deck += (least_2, pair_3[0], Y_0),
                for case_2 in club_2:
                    if case_2[1] == Y_0:
                        board_Y[case_2[0]] = EMPTY
                    else:
                        board_X[case_2[0]] = TAB
                board_Y[pair_3[1]] = Y_0
                club_3 = ()
                least_3 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_3 += (last[0], last[1]),
                    least_3 += 1
                    last = last_segment(board_X, board_Y)
                board_Y[pair_3[1]] = EMPTY
                least.append(least_3)
                deck += (least_3, pair_3[1], Y_0),
                for case_3 in club_3:
                    if case_3[1] == Y_0:
                        board_Y[case_3[0]] = EMPTY
                    else:
                        board_X[case_3[0]] = TAB
    for pair_4 in X_box_1:
        for pair_5 in Y_box_1:
            if pair_4[0] == pair_5[1]:
                board_Y[pair_5[1]] = Y_0
                club_4 = ()
                least_4 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_4 += (last[0], last[1]),
                    least_4 += 1
                    last = last_segment(board_X, board_Y)
                board_Y[pair_5[1]] = EMPTY
                least.append(least_4)
                deck += (least_4, pair_5[1], Y_0),
                for case_4 in club_4:
                    if case_4[1] == Y_0:
                        board_Y[case_4[0]] = EMPTY
                    else:
                        board_X[case_4[0]] = TAB
                board_X[pair_4[1]] = X_3
                club_5 = ()
                least_5 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_5 += (last[0], last[1]),
                    least_5 += 1
                    last = last_segment(board_X, board_Y)
                board_X[pair_4[1]] = TAB
                least.append(least_5)
                deck += (least_5, pair_4[1], X_3),
                for case_5 in club_5:
                    if case_5[1] == Y_0:
                        board_Y[case_5[0]] = EMPTY
                    else:
                        board_X[case_5[0]] = TAB
        for pair_6 in Y_box_2:
            if pair_4[0] == pair_6[1]:
                board_Y[pair_6[0]] = Y_0
                club_6 = ()
                least_6 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_6 += (last[0], last[1]),
                    least_6 += 1
                    last = last_segment(board_X, board_Y)
                board_Y[pair_6[0]] = EMPTY
                least.append(least_6)
                deck += (least_6, pair_6[0], Y_0),
                for case_6 in club_6:
                    if case_6[1] == Y_0:
                        board_Y[case_6[0]] = EMPTY
                    else:
                        board_X[case_6[0]] = TAB
                board_X[pair_4[1]] = X_3
                club_7 = ()
                least_7 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_7 += (last[0], last[1]),
                    least_7 += 1
                    last = last_segment(board_X, board_Y)
                board_X[pair_4[1]] = TAB
                least.append(least_7)
                deck += (least_7, pair_4[1], X_3),
                for case_7 in club_7:
                    if case_7[1] == Y_0:
                        board_Y[case_7[0]] = EMPTY
                    else:
                        board_X[case_7[0]] = TAB
    for pair_7 in X_box_2:
        for pair_8 in Y_box_2:
            if pair_7[0] == pair_8[1]:
                board_X[pair_7[0]] = X_3
                club_8 = ()
                least_8 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_8 += (last[0], last[1]),
                    least_8 += 1
                    last = last_segment(board_X, board_Y)
                board_X[pair_7[0]] = TAB
                least.append(least_8)
                deck += (least_8, pair_7[0], X_3),
                for case_8 in club_8:
                    if case_8[1] == Y_0:
                        board_Y[case_8[0]] = EMPTY
                    else:
                        board_X[case_8[0]] = TAB
                board_Y[pair_8[0]] = Y_0
                club_9 = ()
                least_9 = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_9 += (last[0], last[1]),
                    least_9 += 1
                    last = last_segment(board_X, board_Y)
                board_Y[pair_8[0]] = EMPTY
                least.append(least_9)
                deck += (least_9, pair_8[0], Y_0),
                for case_9 in club_9:
                    if case_9[1] == Y_0:
                        board_Y[case_9[0]] = EMPTY
                    else:
                        board_X[case_9[0]] = TAB
        for pair_9 in Y_box_1:
            if pair_7[0] == pair_9[1]:
                board_X[pair_7[0]] = X_3
                club_A = ()
                least_A = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_A += (last[0], last[1]),
                    least_A += 1
                    last = last_segment(board_X, board_Y)
                board_X[pair_7[0]] = TAB
                least.append(least_A)
                deck += (least_A, pair_7[0], X_3),
                for case_A in club_A:
                    if case_A[1] == Y_0:
                        board_Y[case_A[0]] = EMPTY
                    else:
                        board_X[case_A[0]] = TAB
                board_Y[pair_9[1]] = Y_0
                club_B = ()
                least_B = 0
                last = last_segment(board_X, board_Y)
                while last != None:
                    if last[1] == Y_0:
                        board_Y[last[0]] = Y_0
                    else:
                        board_X[last[0]] = X_3
                    club_B += (last[0], last[1]),
                    least_B += 1
                    last = last_segment(board_X, board_Y)
                board_Y[pair_9[1]] = EMPTY
                least.append(least_B)
                deck += (least_B, pair_9[1], Y_0),
                for case_B in club_B:
                    if case_B[1] == Y_0:
                        board_Y[case_B[0]] = EMPTY
                    else:
                        board_X[case_B[0]] = TAB

    least.sort()
    for triad in deck:
        if triad[0] == least[0]:
            move = triad[1]
            move_0 = triad[2]
            return move, move_0

    
def last_segment(board_X, board_Y):
    """Checks for the house."""

    # gear box.
    
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X)

    # both horizontal lines are occupied.
    for pair_0 in X_box_3:
        # one of the 2 vertical line is occupied.
        for pair_1 in Y_box_1:
            # match, horizontal and vertical lines are of same box.
            if pair_0[0] == pair_1[1]:
                move = pair_1[1]
                move_0 = Y_0
                return move, move_0 
             
        # vice-versa of line candidate.    
        for pair_1 in Y_box_2:
            if pair_0[0] == pair_1[1]:
                move = pair_1[0]
                move_0 = Y_0
                return move, move_0
        
    # both vertical lines are occupied.
    for pair_0 in Y_box_3:
        # one of the 2 horizontal line is occupied.
        for pair_1 in X_box_1:
            # check, legalization of lines.
            if pair_0[1] == pair_1[0]:
                move = pair_1[1]
                move_0 = X_3
                return move, move_0

        # vice-versa of line candidate. 
        for pair_1 in X_box_2:
            if pair_0[1] == pair_1[0]:
                move = pair_1[0]
                move_0 = X_3
                return move, move_0
 

def simulate_first(board_X, board_Y):
    """Copy of 'first_segment' with mistake."""
    
    U_Y_box = ((-9, -8), (-8, -7), (-7, -6), (-6, -5),
               (-5, -4), (-4, -3), (-3, -2), (-2, -1))
    D_Y_box = ((54, 55), (55, 56), (56, 57), (57, 58),
               (58, 59), (59, 60), (60, 61), (61, 62))
    L_X_box = ((-1,  8), ( 8, 17), (17, 26),
               (26, 35), (35, 44), (44, 53))
    R_X_box = (( 9, 18), (18, 27), (27, 36),
               (36, 45), (45, 54), (54, 63))

    
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X)

    X_box   = (X_box_1, X_box_2)
    box_Y_0 = (Y_box_0, Y_box_1)
    box_Y_1 = (Y_box_0, Y_box_2)
    box_Y_2 = (Y_box_0, Y_box_1, Y_box_2)

    for pair_1 in Y_box_0:
        for stack in X_box:
            for pair_0 in stack:
                if pair_0[0] == pair_1[1]:
                    match = (pair_0[0] + 1, pair_0[1] + 1)
                    for double in R_X_box:
                        if match == double :
                            move = pair_1[1]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0 or X_box_1 or X_box_2) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
        
        for pair_0 in X_box_2:
            if pair_0[0] == pair_1[1]:
                match = (pair_1[0] - 9, pair_1[1] - 9)
                for double in U_Y_box:
                    if match == double:
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
                if (match in Y_box_0 or Y_box_1 or Y_box_2) and (board_X[pair_0[0] - 9] == TAB):
                    move = pair_0[0]
                    move_0 = X_3
                    return move, move_0
                elif match in Y_box_0:
                    move = pair_0[0]
                    move_0 = X_3
                    return move, move_0
        for stack in X_box:
            for pair_0 in stack:
                if pair_0[0] == pair_1[1]:
                    match = (pair_0[0] - 1, pair_0[1] - 1)
                    for double in L_X_box:
                        if match == double:
                            move = pair_1[0]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0 or X_box_1 or X_box_2) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
        for pair_0 in X_box_1:
            if pair_0[0] == pair_1[1]:
                match = (pair_1[0] + 9, pair_1[1] + 9)
                for double in D_Y_box:
                    if match == double:
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0
                if (match in Y_box_0 or Y_box_1 or Y_box_2) and (board_X[pair_0[1] + 9] == TAB):
                    move = pair_0[1]
                    move_0 = X_3
                    return move, move_0
                elif match in Y_box_0:
                    move = pair_0[1]
                    move_0 = X_3
                    return move, move_0
    for pair_0 in X_box_0:
        for stack in box_Y_0:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    match = (pair_0[0] + 1, pair_0[1] + 1)
                    for double in R_X_box:
                        if match == double:
                            move = pair_1[1]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0 or X_box_1 or X_box_2) and (board_Y[pair_1[1] + 1] == EMPTY):
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[1]
                        move_0 = Y_0
                        return move, move_0
        for stack in box_Y_2:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    match = (pair_1[0] - 9, pair_1[1] - 9)
                    for double in U_Y_box:
                        if match == double:
                            move = pair_0[0]
                            move_0 = X_3
                            return move, move_0
                    if (match in Y_box_0 or Y_box_1 or Y_box_2) and (board_X[pair_0[0] - 9] == TAB):
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
                    elif match in Y_box_0:
                        move = pair_0[0]
                        move_0 = X_3
                        return move, move_0
        for stack in box_Y_1:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    match = (pair_0[0] - 1, pair_0[1] - 1)
                    for double in L_X_box:
                        if match == double:
                            move = pair_1[0]
                            move_0 = Y_0
                            return move, move_0
                    if (match in X_box_0 or X_box_1 or X_box_2) and (board_Y[pair_1[0] - 1] == EMPTY):
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
                    elif match in X_box_0:
                        move = pair_1[0]
                        move_0 = Y_0
                        return move, move_0
        for stack in box_Y_2:
            for pair_1 in stack:
                if pair_0[0] == pair_1[1]:
                    match = (pair_1[0] + 9, pair_1[1] + 9)
                    for double in D_Y_box:
                        if match == double:
                            move = pair_0[1]
                            move_0 = X_3
                            return move, move_0
                    if (match in Y_box_0 or Y_box_1 or Y_box_2) and (board_X[pair_0[1] + 9] == TAB):
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0
                    elif match in Y_box_0:
                        move = pair_0[1]
                        move_0 = X_3
                        return move, move_0


def place_block_0(block, turn, move, move_0, board_Y, board_X, tally_comp, tally_homo):
    """Fill the blocks."""
    
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X)
    duet_0 = (move, move + 9)
    duet_1 = (move - 1, move)
    if move_0 == Y_0:
        duet_2 = (move + 1, move + 10)
        duet_3 = (move, move + 1)
        if (duet_0 in X_box_3 and duet_1 in Y_box_3) and (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == computer:
                block[move] = computer[0]
                block[move - 1] = computer[0]
                tally_comp += 2
            else:
                block[move] = human_0
                block[move - 1] = human_0
                tally_homo += 2
        elif (duet_0 in X_box_3 and duet_1 in Y_box_3):
            if turn == computer:
                block[move - 1] = computer[0]
                tally_comp += 1
            else:
                block[move - 1] = human_0
                tally_homo += 1
        elif (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == computer:
                block[move] = computer[0]
                tally_comp += 1
            else:
                block[move] = human_0
                tally_homo += 1
        else:
            tally_comp += 0
            tally_homo += 0
    else:
        duet_2 = (move - 9, move)
        duet_3 = (move - 10, move - 9)
        if (duet_0 in X_box_3 and duet_1 in Y_box_3) and (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == computer:
                block[move - 1] = computer[0]
                block[move - 10] = computer[0]
                tally_comp += 2
            else:
                block[move - 1] = human_0
                block[move - 10] = human_0
                tally_homo += 2
        elif (duet_0 in X_box_3 and duet_1 in Y_box_3):
            if turn == computer:
                block[move - 1] = computer[0]
                tally_comp += 1
            else:
                block[move - 1] = human_0
                tally_homo += 1
        elif (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == computer:
                block[move - 10] = computer[0]
                tally_comp += 1
            else:
                block[move - 10] = human_0
                tally_homo += 1
        else:
            tally_comp += 0
            tally_homo += 0
    return tally_comp, tally_homo

def place_block_1(block, turn, move, move_0, board_Y, board_X):
    """Fill the blocks."""
    
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X)
    duet_0 = (move, move + 9)
    duet_1 = (move - 1, move)
    if move_0 == Y_0:
        duet_2 = (move + 1, move + 10)
        duet_3 = (move, move + 1)
        if (duet_0 in X_box_3 and duet_1 in Y_box_3) and (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == player_1:
                block[move] = player_1_0
                block[move - 1] = player_1_0
                tally_player_1 += 2
            else:
                block[move] = player_2_0
                block[move - 1] = player_2_0
                tally_player_2 += 2
        elif (duet_0 in X_box_3 and duet_1 in Y_box_3):
            if turn == player_1:
                block[move - 1] = player_1_0
                tally_player_1 += 1
            else:
                block[move - 1] = player_2_0
                tally_player_2 += 1
        elif (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == player_1:
                block[move] = player_1_0
                tally_player_1 += 1
            else:
                block[move] = player_2_0
                tally_player_2 += 1
        else:
            tally_player_1 += 0
            tally_player_2 += 0
    else:
        duet_2 = (move - 9, move)
        duet_3 = (move - 10, move - 9)
        if (duet_0 in X_box_3 and duet_1 in Y_box_3) and (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == player_1:
                block[move - 1] = player_1_0
                block[move - 10] = player_1_0
                tally_player_1 += 2
            else:
                block[move - 1] = player_2_0
                block[move - 10] = player_2_0
                tally_player_2 += 2
        elif (duet_0 in X_box_3 and duet_1 in Y_box_3):
            if turn == player_1:
                block[move - 1] = player_1_0
                tally_player_1 += 1
            else:
                block[move - 1] = player_2_0
                tally_player_2 += 1
        elif (duet_2 in X_box_3 and duet_3 in Y_box_3):
            if turn == player_1:
                block[move - 10] = player_1_0
                tally_player_1 += 1
            else:
                block[move - 10] = player_2_0
                tally_player_2 += 1
        else:
            tally_player_1 += 0
            tally_player_2 += 0


def computer_move(board_X, board_Y):
    """Make computer move."""
    step = []
    mark = mark_stack(board_X, board_Y)
    account = random.choice(mark)
    proceed = random.choice(account)
    last = last_segment(board_X, board_Y)
    first = first_segment(board_X, board_Y)
    trace = simulate_first(board_X, board_Y)
    second = second_segment(board_X, board_Y)
       
    print "\nI shall  go  for  the  place....\n"

    if level == "0":
        if account == mark[0]:
            step.insert(1, X_3)
        else:
            step.insert(1, Y_0)
        step.insert(0, proceed)
    elif level == "1":
        if last == None:
            if account == mark[0]:
                step.insert(1, X_3)
            else:
                step.insert(1, Y_0)
            step.insert(0, proceed)
        else:
            step = last
    elif level == "2":
        if last == None:
            if trace == None:
                step = second
            else:
                step = first
        else:
            step = last
    elif level == "3":
        if last == None:
            if first == None:
                step = second
            else:
                step = first
        else:
            step = last
    move = step[0]
    
    if step[1] == Y_0:
        board_Y[move] = step[1] 
        move_0 = board_Y[move]
        print move, "to", move + 9
    else:
        board_X[move] = step[1]
        move_0 = board_X[move]
        print move - 1, "to", move
    return move, move_0


def score_board_0(human_score, cyber_score , turn, rank_comp, rank_homo, move, move_0, board_X, board_Y, tally_comp, tally_homo):
    """Manipulates and display the scores against computer."""
    last_score = (155, 997, 2037, 8765, 32331, 77683, 189343, 478539, 923648,
                  2390450, 5846346, 7983460, 30003690, 69368573, 81102300,
                  123400039, 500500987, 965650055, 1000000000, 7123344090,
                  9001872347, 20934829023, 69204083849, 92834499249,
                  333333333333, 880322838492, 899999999999, 1000100010001,
                  4309294599934, 7839247389294, 45490322045929, 50910430420440,
                  302058293495293, 877666555544444)
    first_score = (93, 78, 57, 81, 65, 92, 59, 86, 64, 70)
    second_score = (46, 18, 37, 53, 25, 9, 10, 31, 54, 22, 43, 05)
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X) 

    if turn == computer:
        if move_0 == Y_0:
            board_Y[move] = EMPTY 
        else:
            board_X[move] = TAB

        if last_segment(board_X, board_Y) == None:
            if first_segment(board_X, board_Y) == None:
                add_comp = random.choice(second_score)
            else:
                add_comp = random.choice(first_score)
        else:
            add_comp = 0
            for i in range(rank_comp):
                add_comp += last_score[i]
        cyber_score += add_comp

        print "\n\t\t\t\tSCORE BOARD"
        print "\n\t", human, "=", human_score, "\t\t\t", computer, "=", cyber_score, "\n"
        
        if last_segment(board_X, board_Y) == None:
            print "\t\t\t\t\t+", add_comp
        else:
            for i in range(rank_comp):
                print "\t\t\t\t\t", "+" * (i + 1), last_score[i]
                
        print "\n\t\t\t\tHOUSE BOARD"
        print "\n\t", human, "=", tally_homo, "\t\t\t\t", computer, "=", tally_comp, "\n"

        if move_0 == Y_0:
            board_Y[move] = Y_0 
        else:
            board_X[move] = X_3
    else:
        duet_0 = (move, move + 9)
        duet_1 = (move - 1, move)
        
        if move_0 == Y_0:
            duet_2 = (move + 1, move + 10)
            duet_3 = (move, move + 1)
        else:
            duet_2 = (move - 9, move)
            duet_3 = (move - 10, move - 9)
            
        if duet_0 in X_box_3 and duet_1 in Y_box_3:
            temp = 0
            add_homo = 0
            for i in range(rank_homo):
                add_homo += last_score[i]
        elif duet_2 in X_box_3 and duet_3 in Y_box_3:
            temp = 0
            add_homo = 0
            for i in range(rank_homo):
                add_homo += last_score[i]
        elif last_segment(board_X, board_Y) != None:
            temp = 1
            add_homo = random.choice(second_score)
        else:
            temp = 2
            add_homo = random.choice(first_score)

        human_score += add_homo
        
        print "\n\t\t\t\tSCORE BOARD"
        print "\n\t", human, "=", human_score, "\t\t\t", computer, "=", cyber_score, "\n"

        if temp == 1 or temp == 2:
            print "\t+", add_homo
        else:
            for i in range(rank_homo):
                print "\t", "+" * (i + 1), last_score[i]
            
        print "\n\t\t\t\tHOUSE BOARD"
        print "\n\t", human, "=", tally_homo, "\t\t\t\t", computer, "=", tally_comp, "\n"
 
    return human_score, cyber_score


def score_board_1(player_2_score, player_1_score , turn, rank_player_1, rank_player_2, move, move_0, board_X, board_Y, tally_player_1, tally_player_2):
    """Manipulates and display the scores against player."""
    last_score = (155, 997, 2037, 8765, 32331, 77683, 189343, 478539, 923648,
                  2390450, 5846346, 7983460, 30003690, 69368573, 81102300,
                  123400039, 500500987, 965650055, 1000000000, 7123344090,
                  9001872347, 20934829023, 69204083849, 92834499249,
                  333333333333, 880322838492, 899999999999, 1000100010001,
                  4309294599934, 7839247389294, 45490322045929, 50910430420440,
                  302058293495293, 877666555544444)
    first_score = (93, 78, 57, 81, 65, 92, 59, 86, 64, 70)
    second_score = (46, 18, 37, 53, 25, 9, 10, 31, 54, 22, 43, 05)
    Y_box_0, Y_box_1, Y_box_2, Y_box_3 = Y_axis(board_Y)
    X_box_0, X_box_1, X_box_2, X_box_3 = X_axis(board_X) 

    duet_0 = (move, move + 9)
    duet_1 = (move - 1, move)
        
    if move_0 == Y_0:
        duet_2 = (move + 1, move + 10)
        duet_3 = (move, move + 1)
    else:
        duet_2 = (move - 9, move)
        duet_3 = (move - 10, move - 9)
            
    if duet_0 in X_box_3 and duet_1 in Y_box_3:
        temp = 0
        if turn == player_2:
            add_player_2 = 0
            for i in range(rank_player_2):
                add_player_2 += last_score[i]
            player_2_score += add_player_2
        else:
            add_player_1 = 0
            for i in range(rank_player_1):
                add_player_1 += last_score[i]
            player_1_score += add_player_1
    elif duet_2 in X_box_3 and duet_3 in Y_box_3:
        temp = 0
        if turn == player_2:
            add_player_2 = 0
            for i in range(rank_player_2):
                add_player_2 += last_score[i]
            player_2_score += add_player_2
        else:
            add_player_1 = 0
            for i in range(rank_player_1):
                add_player_1 += last_score[i]
            player_1_score += add_player_1
    elif last_segment(board_X, board_Y) != None:
        temp = 1
        if turn == player_2:
            add_player_2 = random.choice(second_score)
            player_2_score += add_player_2
        else:
            add_player_1 = random.choice(second_score)
            player_1_score += add_player_1
    else:
        temp = 2
        if turn == player_2:
            add_player_2 = random.choice(first_score)
            player_2_score += add_player_2
        else:
            add_player_1 = random.choice(first_score)
            player_1_score += add_player_1

    print "\n\t\t\t\tSCORE BOARD" 
    print "\n\t", player_2, "=", player_2_score, "\t\t\t", player_1, "=", player_1_score, "\n"

    if temp == 1 or temp == 2:
        if turn == player_2:
            print "\t+", add_player_2
        else:
            print "\t\t\t\t\t+", add_player_1
    else:
        if turn == player_2:
            for i in range(rank_player_2):
                print "\t", "+" * (i + 1), last_score[i]
        else:
            for i in range(rank_player_1):
                print "\t\t\t\t\t", "+" * (i + 1), last_score[i]

    print "\n\t\t\t\tHOUSE BOARD"
    print "\n\t", player_2, "=", tally_player_2, "\t\t\t\t", player_1, "=", tally_player_1, "\n"
 
    return player_2_score, player_1_score


def rank_turn_0(turn, rank_comp, rank_homo):
    """Tells back-to-back moves against computer."""
    if turn == computer:
        rank_homo = 0
        rank_comp += 1
    else:
        rank_comp = 0
        rank_homo += 1
    return rank_comp, rank_homo


def rank_turn_1(turn, rank_player_1, rank_player_2):
    """Tells back-to-back moves against player."""
    if turn == player_1:
        rank_player_2 = 0
        rank_player_1 += 1
    else:
        rank_player_1 = 0
        rank_player_2 += 1
    return rank_player_1, rank_player_2


def main_0():
    """Functions assemble."""
    rank_comp, rank_homo, human_score, cyber_score, tally_comp, tally_homo = initial_local_0()
    turn = pieces_0()
    block = block_name() 
    board_Y = verti_board()
    board_X = horizon_board()

    print"\nAs you dare to step in this death valley with", computer, ",\nYou are now proprietor of 1500 points along with", computer, "."
    print "\nENOY THE BATTLE."
    print "\n\t\t\t\tSCORE BOARD"
    print "\n\t", human, "=", human_score, "\t\t\t", computer, "=", cyber_score, "\n\n"
    print "\n\t\t\t\tHOUSE BOARD"
    print "\n\t", human, "=", tally_homo, "\t\t\t\t", computer, "=", tally_comp, "\n"

    display_board(board_Y, board_X, block)
   
    while not winner(block, human_score, cyber_score):
        if turn == human:
            move, move_0 = human_move(board_X, board_Y)
        else:
            move, move_0 = computer_move(board_X, board_Y)
        tally_comp, tally_homo = place_block_0(block, turn, move, move_0, board_Y, board_X, tally_comp, tally_homo)
        rank_comp, rank_homo = rank_turn_0(turn, rank_comp, rank_homo)
        human_score, cyber_score = score_board_0(human_score, cyber_score , turn, rank_comp, rank_homo, move, move_0, board_X, board_Y, tally_comp, tally_homo)
        display_board(board_Y, board_X, block)
        turn = next_turn_0(turn, move, move_0, board_Y, board_X)
        
    winner(board_Y, board_X, human_score, computer_score)


def main_1():
    rank_player_1, rank_player_2, player_1_score, player_2_score, tally_player_1, tally_player_2 = initial_local_1()
    turn = pieces_1()
    block = block_name() 
    board_Y = verti_board()
    board_X = horizon_board()

    print "\nAs you both dare to step in this death valley, \nYou both are proprietor of 1500 points."
    print "\nENOY THE BATTLE."
    print "\n\t\t\t\tSCORE BOARD"
    print "\n\t", player_2, "=", player_2_score, "\t\t\t", player_1, "=", player_1_score, "\n\n"
    print "\n\t\t\t\tHOUSE BOARD"
    print "\n\t", player_2, "=", tally_player_2, "\t\t\t\t", computer, "=", tally_player_1, "\n"

    display_board(board_Y, board_X, block)

    while not winner(block, tally_comp, tally_homo):
        print "\n", turn, "!!!...Your turn...."
        move, move_0 = human_move(board_X, board_Y)
        tally_player_1, tally_player_2 = place_block_1(block, turn, move, move_0, board_Y, board_X, tally_player_1, tally_player_2)
        rank_player_1, rank_player_2 = rank_turn_1(turn, rank_player_1, rank_player_2)
        player_2_score, player_1_score = score_board_1(player_2_score, player_1_score , turn, rank_player_1, rank_player_2, move, move_0, board_X, board_Y, tally_player_1, tally_player_2)
        display_board(board_Y, board_X, block)
        turn = next_turn_1(turn, move, move_0, board_Y, board_X)
        
    the_winner = winner(board_Y, board_X, tally_comp, tally_homo)

    
insert = None
while insert != "3":
    print\
    """
           MAIN MENU.
        
        0 - How to play.
        1 - Let's battle.
        2 - Credits.
        3 - Exit.
    """
    insert = raw_input("\nWhat's in your mind....(0-3):")
    if insert == "0":
        display_instruct()
    elif insert == "1":
        play_again = None
        while play_again != "2":
            opponent = ask_number("\nChoose your opponent...\n\n1.Player against Player.\t\t2.Player against Computer.\n\nPress '1' or '2':")
            if opponent == "1":
                player_1, player_2, player_1_0, player_2_0 = match_alias_1()

                print "\nGet ready", player_1, "and", player_2, "you will now have to face each other."
                
                main_1()
            else:
                print "\nLet's see your level human."
                
                level = None
                kit = ["0", "1", "2", "3"]
                while level not in kit:
                    print\
                    """
                        0 - VERY LOW.
                        1 - LOW.
                        2 - HIGH.
                        3 - VERY HIGH.
                    """ 
                    level = raw_input("\nLevel you belong....(0-3):")
                    if level == "0":
                        computer = "ZARVIS"
                        print "\nNow i can judge you human, you are such a newbie."
                    elif level == "1":
                        computer = "MEGATRON"
                        print "\nYour choice says you are still a novice at this."
                    elif level == "2":
                        computer = "TERMINATOR"
                        print "\nOh!!!... you are in deep trouble, this step will cost you."
                    elif level == "3":
                        computer = "ULTRON"
                        print "\nEnter the dragon human, this time i will not be so kind."
                    else:
                        print "\nAnother sign that shows that you are such an idiot, renter_0."
                human, human_0 = match_alias_0()
                
                print "\nGet ready", human, ", you will now have to face", computer, "."
            
                main_0()
            play_again = ask_number("\n1.Play again.\t\t2.Main menu.\n\nTap digit '1' or '2':")
    elif insert == "2":
        print "\n\n\n\t\t\t\tCREDITS."
        print "\n\t\t\t      Lakshya Rana."
    elif insert == "3":
        command = ask_number("\nAre you sure to exit.\n\n1-Yes.\t\t\t2-No.\n\nHit either '1' or '2':")
        if command == "1":
            print "\nGood - Bye."
        else:
            print "\nYou must be having guts.......welcome back."
            insert = None
    else:
        print "Sorry, but your choice", insert, "isn't a valid one."

raw_input("\n\n\nPress enter key to exit.....")
