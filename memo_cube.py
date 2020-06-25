"""Generate the state of the cube
    into letter pairs using a data structure like lists"""


class Cube:
    # TODO make a second class than prints the color instead of the letter
    # TODO keep track of solved edges
    # todo generate list of unsolved pieces
    # TODO make func that checks if the edges/corners are solved
    # ------------------init the solved state of the cube------------------
    def __init__(self):
        self.memo_li = []
        self.edges_not_avail = []
        self.solved_edges = []
        self.flipped_edges = []
        self.unsolved_edges = []

        self.U_edges = ['A', 'B', '1', 'D']
        self.U_corners = ['A', 'B', '1', 'D']
        self.F_edges = ['2', 'J', 'I', 'L']
        self.F_corners = ['E', '3', 'K', 'L']
        self.L_edges = ['E', 'F', 'G', 'H']
        self.L_corners = ['J', 'F', 'G', 'H']
        self.R_edges = ['M', 'N', 'O', 'P']
        self.R_corners = ['2', 'N', 'O', 'P']
        self.B_edges = ['Z', 'R', 'S', 'T']
        self.B_corners = ['R', 'M', 'S', 'T']
        self.D_edges = ['C', 'V', 'W', 'X']
        self.D_corners = ['C', 'V', 'W', 'Z']

        self.U_edges_init = ['A', 'B', '1', 'D']
        self.U_corners_init = ['A', 'B', '1', 'D']
        self.F_edges_init = ['2', 'J', 'I', 'L']
        self.F_corners_init = ['E', '3', 'K', 'L']
        self.L_edges_init = ['E', 'F', 'G', 'H']
        self.L_corners_init = ['J', 'F', 'G', 'H']
        self.R_edges_init = ['M', 'N', 'O', 'P']
        self.R_corners_init = ['2', 'N', 'O', 'P']
        self.B_edges_init = ['Z', 'R', 'S', 'T']
        self.B_corners_init = ['R', 'M', 'S', 'T']
        self.D_edges_init = ['C', 'V', 'W', 'X']
        self.D_corners_init = ['C', 'V', 'W', 'Z']

        self.list_of_edges = ['UB', 'UR', 'UL', 'DF', 'DB', 'DR', 'DL', 'FR', 'FL', 'BR', 'BL']

        self.pos_to_letters = {'UF': "1 2", 'UB': "A Z", 'UR': "B M", 'UL': "D E", 'DF': "C I",
                               'DB': "W S", 'DR': "V O", 'DL': "X G", 'FR': "J P", 'FL': "L F",
                               'BR': "T N", 'BL': "R H"}
        self.edge_val = iter([self.U_edges[2], self.U_edges[0], self.U_edges[1], self.U_edges[3],
                              self.F_edges[1], self.F_edges[3],
                              self.B_edges[1], self.B_edges[3],
                              self.D_edges[0], self.D_edges[1], self.D_edges[2], self.D_edges[3]])

    # -------------------------------display cube faces ------------------------------------

    def display_u_face(self):
        print('---------U face---------')
        print(f"\t  {self.U_corners[0]}  {self.U_edges[0]}  {self.U_corners[1]}\n"
              f"\t  {self.U_edges[3]} 'W' {self.U_edges[1]}"
              f"\n\t  {self.U_corners[3]}  {self.U_edges[2]}  {self.U_corners[2]}")
        print('------------------------')

    def display_f_face(self):
        print('---------F face---------')
        print(f"\t  {self.F_corners[0]}  {self.F_edges[0]}  {self.F_corners[1]}\n"
              f"\t  {self.F_edges[3]} 'G' {self.F_edges[1]}"
              f"\n\t  {self.F_corners[3]}  {self.F_edges[2]}  {self.F_corners[2]}")
        print('------------------------')

    def display_l_face(self):
        print('---------L face---------')
        print(f"\t  {self.L_corners[0]}  {self.L_edges[0]}  {self.L_corners[1]}\n"
              f"\t  {self.L_edges[3]} 'O' {self.L_edges[1]}"
              f"\n\t  {self.L_corners[3]}  {self.L_edges[2]}  {self.L_corners[2]}")
        print('------------------------')

    def display_r_face(self):
        print('---------R face---------')
        print(f"\t  {self.R_corners[0]}  {self.R_edges[0]}  {self.R_corners[1]}\n"
              f"\t  {self.R_edges[3]} 'R' {self.R_edges[1]}"
              f"\n\t  {self.R_corners[3]}  {self.R_edges[2]}  {self.R_corners[2]}")
        print('------------------------')

    def display_b_face(self):
        print('---------B face---------')
        print(f"\t  {self.B_corners[0]}  {self.B_edges[0]}  {self.B_corners[1]}\n"
              f"\t  {self.B_edges[3]} 'B' {self.B_edges[1]}"
              f"\n\t  {self.B_corners[3]}  {self.B_edges[2]}  {self.B_corners[2]}")
        print('------------------------')

    def display_d_face(self):
        print('---------D face---------')
        print(f"\t  {self.D_corners[0]}  {self.D_edges[0]}  {self.D_corners[1]}\n"
              f"\t  {self.D_edges[3]} 'Y' {self.D_edges[1]}"
              f"\n\t  {self.D_corners[3]}  {self.D_edges[2]}  {self.D_corners[2]}")
        print('------------------------')

    # ---------------------------------------turn cube faces ------------------------------------

    def turn_u(self, turns=1):
        for i in range(turns):
            # --------- U layer--------------
            self.U_edges = [self.U_edges[-1]] + self.U_edges[:-1]
            self.U_corners = [self.U_corners[-1]] + self.U_corners[:-1]

            self.L_edgescopy = self.L_edges[:]
            self.L_cornerscopy = self.L_corners[:]
            # ---F layer to L layer-------
            a3 = self.F_edges[0]
            self.L_edges[0] = a3
            b3 = self.F_corners[0]
            self.L_corners[0] = b3
            b3 = self.F_corners[1]
            self.L_corners[1] = b3
            # ----R layer to F layer-------
            a3 = self.R_edges[0]
            self.F_edges[0] = a3
            b3 = self.R_corners[0]
            self.F_corners[0] = b3
            b3 = self.R_corners[1]
            self.F_corners[1] = b3
            # ----B layer to R layer-------
            a3 = self.B_edges[0]
            self.R_edges[0] = a3
            b3 = self.B_corners[0]
            self.R_corners[0] = b3
            b3 = self.B_corners[1]
            self.R_corners[1] = b3
            # ----L layer to B layer-------
            a3 = self.L_edgescopy[0]
            self.B_edges[0] = a3
            b3 = self.L_cornerscopy[0]
            self.B_corners[0] = b3
            b3 = self.L_cornerscopy[1]
            self.B_corners[1] = b3

    def turn_f(self, turns=1):
        for i in range(turns):
            #  ---turn F-----
            self.F_edges = [self.F_edges[-1]] + self.F_edges[:-1]
            self.F_corners = [self.F_corners[-1]] + self.F_corners[:-1]

            # ------------------------------------
            self.L_edgescopy = self.L_edges[:]
            self.L_cornerscopy = self.L_corners[:]
            self.R_edgescopy = self.R_edges[:]
            self.R_cornerscopy = self.R_corners[:]
            self.D_edgescopy = self.D_edges[:]
            self.D_cornerscopy = self.D_corners[:]

            # ---U layer to R layer-------
            a3 = self.U_edges[2]
            self.R_edges[3] = a3
            b3 = self.U_corners[3]
            self.R_corners[0] = b3
            b3 = self.U_corners[2]
            self.R_corners[3] = b3
            # ----R layer to D layer-------
            a3 = self.R_edgescopy[3]
            self.D_edges[0] = a3
            b3 = self.R_cornerscopy[0]
            self.D_corners[1] = b3
            b3 = self.R_cornerscopy[3]
            self.D_corners[0] = b3
            # ----D layer to L layer-------
            a3 = self.D_edgescopy[0]
            self.L_edges[1] = a3
            b3 = self.D_cornerscopy[0]
            self.L_corners[1] = b3
            b3 = self.D_cornerscopy[1]
            self.L_corners[2] = b3
            # ----L layer to U layer-------
            a3 = self.L_edgescopy[1]
            self.U_edges[2] = a3
            b3 = self.L_cornerscopy[2]
            self.U_corners[3] = b3
            b3 = self.L_cornerscopy[1]
            self.U_corners[2] = b3

    def turn_l(self, turns=1):
        for i in range(turns):
            self.L_edges = [self.L_edges[-1]] + self.L_edges[:-1]
            self.L_corners = [self.L_corners[-1]] + self.L_corners[:-1]
            # -------------- cycle side corners and edges-------------------
            edge_group = [self.U_edges[3], self.F_edges[3], self.D_edges[3], self.B_edges[1]]
            edge_group = [edge_group[-1]] + edge_group[:-1]
            self.U_edges[3] = edge_group[0]
            self.F_edges[3] = edge_group[1]
            self.D_edges[3] = edge_group[2]
            self.B_edges[1] = edge_group[3]

            corner_group1 = [self.U_corners[0],
                             self.F_corners[0],
                             self.D_corners[0],
                             self.B_corners[2]]
            corner_group2 = [self.U_corners[3],
                             self.F_corners[3],
                             self.D_corners[3],
                             self.B_corners[1]]
            corner_group1 = [corner_group1[-1]] + corner_group1[:-1]
            corner_group2 = [corner_group2[-1]] + corner_group2[:-1]

            self.U_corners[0] = corner_group1[0]
            self.F_corners[0] = corner_group1[1]
            self.D_corners[0] = corner_group1[2]
            self.B_corners[2] = corner_group1[3]
            self.U_corners[3] = corner_group2[0]
            self.F_corners[3] = corner_group2[1]
            self.D_corners[3] = corner_group2[2]
            self.B_corners[1] = corner_group2[3]

    def turn_r(self, turns=1):
        for i in range(turns):
            self.R_edges = [self.R_edges[-1]] + self.R_edges[:-1]
            self.R_corners = [self.R_corners[-1]] + self.R_corners[:-1]
            # -----------------------------------------------------------------------------
            edge_group = [self.U_edges[1], self.F_edges[1], self.D_edges[1], self.B_edges[3]]
            edge_group = [edge_group[-1]] + edge_group[:-1]
            self.U_edges[1] = edge_group[2]
            self.F_edges[1] = edge_group[3]
            self.D_edges[1] = edge_group[0]
            self.B_edges[3] = edge_group[1]
            # -----------------------------------
            corner_group1 = [self.U_corners[1],
                             self.B_corners[3],
                             self.D_corners[1],
                             self.F_corners[1]]
            corner_group2 = [self.U_corners[2],
                             self.B_corners[0],
                             self.D_corners[2],
                             self.F_corners[2]]
            corner_group1 = [corner_group1[-1]] + corner_group1[:-1]
            corner_group2 = [corner_group2[-1]] + corner_group2[:-1]

            self.U_corners[1] = corner_group1[0]
            self.F_corners[1] = corner_group1[3]
            self.D_corners[1] = corner_group1[2]
            self.B_corners[3] = corner_group1[1]
            self.U_corners[2] = corner_group2[0]
            self.F_corners[2] = corner_group2[3]
            self.D_corners[2] = corner_group2[2]
            self.B_corners[0] = corner_group2[1]

    def turn_d(self, turns=1):
        for i in range(turns):
            self.D_edges = [self.D_edges[-1]] + self.D_edges[:-1]
            self.D_corners = [self.D_corners[-1]] + self.D_corners[:-1]
            # -----------------------------------------------------------------------------
            edge_group = [self.L_edges[2], self.F_edges[2], self.R_edges[2], self.B_edges[2]]
            edge_group = [edge_group[-1]] + edge_group[:-1]
            self.L_edges[2] = edge_group[0]
            self.F_edges[2] = edge_group[1]
            self.R_edges[2] = edge_group[2]
            self.B_edges[2] = edge_group[3]
            # -----------------------------------
            corner_group1 = [self.L_corners[3],
                             self.F_corners[3],
                             self.R_corners[3],
                             self.B_corners[3]]
            corner_group2 = [self.L_corners[2],
                             self.F_corners[2],
                             self.R_corners[2],
                             self.B_corners[2]]
            corner_group1 = [corner_group1[-1]] + corner_group1[:-1]
            corner_group2 = [corner_group2[-1]] + corner_group2[:-1]

            self.L_corners[3] = corner_group1[0]
            self.F_corners[3] = corner_group1[1]
            self.R_corners[3] = corner_group1[2]
            self.B_corners[3] = corner_group1[3]
            self.L_corners[2] = corner_group2[0]
            self.F_corners[2] = corner_group2[1]
            self.R_corners[2] = corner_group2[2]
            self.B_corners[2] = corner_group2[3]

    def turn_b(self, turns=1):
        for i in range(turns):
            self.B_edges = [self.B_edges[-1]] + self.B_edges[:-1]
            self.B_corners = [self.B_corners[-1]] + self.B_corners[:-1]
            # -----------------------------------------------------------------------------
            edge_group = [self.U_edges[0], self.L_edges[3], self.D_edges[2], self.R_edges[1]]
            edge_group = [edge_group[-1]] + edge_group[:-1]
            self.U_edges[0] = edge_group[0]
            self.L_edges[3] = edge_group[1]
            self.D_edges[2] = edge_group[2]
            self.R_edges[1] = edge_group[3]
            # -----------------------------------
            corner_group1 = [self.U_corners[1],
                             self.L_corners[0],
                             self.D_corners[3],
                             self.R_corners[2]]
            corner_group2 = [self.U_corners[0],
                             self.L_corners[3],
                             self.D_corners[2],
                             self.R_corners[1]]
            corner_group1 = [corner_group1[-1]] + corner_group1[:-1]
            corner_group2 = [corner_group2[-1]] + corner_group2[:-1]

            self.U_corners[1] = corner_group1[0]
            self.L_corners[0] = corner_group1[1]
            self.D_corners[3] = corner_group1[2]
            self.R_corners[2] = corner_group1[3]
            self.U_corners[0] = corner_group2[0]
            self.L_corners[3] = corner_group2[1]
            self.D_corners[2] = corner_group2[2]
            self.R_corners[1] = corner_group2[3]

    def edge_letter_to_val_at_loc(self, key):
        """ :returns value for the letter's spot specified"""
        edge_pairs = {'A': self.U_edges[0], 'B': self.U_edges[1], '1': self.U_edges[2],
                      'D': self.U_edges[3], '2': self.F_edges[0], 'J': self.F_edges[1],
                      'I': self.F_edges[2], 'L': self.F_edges[3], 'E': self.L_edges[0],
                      'F': self.L_edges[1], 'G': self.L_edges[2], 'H': self.L_edges[3],
                      'M': self.R_edges[0], 'N': self.R_edges[1], 'O': self.R_edges[2],
                      'P': self.R_edges[3], 'Z': self.B_edges[0], 'R': self.B_edges[1],
                      'S': self.B_edges[2], 'T': self.B_edges[3], 'C': self.D_edges[0],
                      'V': self.D_edges[1], 'W': self.D_edges[2], 'X': self.D_edges[3]
        }
        return edge_pairs[key]

    def edge_used(self, le):
        if le == 'A' or le == 'Z':
            self.edges_not_avail.append('UB')
            return 'UB'
        elif le == 'B' or le == 'M':
            self.edges_not_avail.append('UR')
            return 'UR'
        elif le == 'C' or le == 'I':
            self.edges_not_avail.append('DF')
            return 'DF'
        elif le == 'D' or le == 'E':
            self.edges_not_avail.append('UL')
            return 'UL'
        elif le == 'V' or le == 'O':
            self.edges_not_avail.append('DR')
            return 'DR'
        elif le == 'X' or le == 'G':
            self.edges_not_avail.append('DL')
            return 'DL'
        elif le == 'W' or le == 'S':
            self.edges_not_avail.append('DB')
            return 'DB'
        elif le == 'J' or le == 'P':
            self.edges_not_avail.append('FR')
            return 'FR'
        elif le == 'L' or le == 'F':
            self.edges_not_avail.append('FL')
            return 'FL'
        elif le == 'T' or le == 'N':
            self.edges_not_avail.append('BR')
            return 'BR'
        elif le == 'R' or le == 'H':
            self.edges_not_avail.append('BL')
            return 'BL'

    def get_buffer_val(self, pos):
        bufferpairs = {
            'UB': self.U_edges[0],
            'UR': self.U_edges[1],
            'UL': self.U_edges[3],
            'FR': self.F_edges[1],
            'FL': self.F_edges[3],
            'BL': self.B_edges[1],
            'BR': self.B_edges[3],
            'DF': self.D_edges[0],
            'DR': self.D_edges[1],
            'DB': self.D_edges[2],
            'DL': self.D_edges[3]
        }
        return bufferpairs[pos]

    def is_edge_solved(self):
        for i in self.list_of_edges:
            # get pos of edge eg 'UB'
            # take ub and get le A and Z
            # if val in U layer[0] is A or Z return 1 or -1 (if is flipped -1)
            # else return 0
            # print(i, 'i')
            le1, le2 = self.pos_to_letters[i].split(' ')
            # print(le1)
            # print(le2)
            edge_val = self.get_buffer_val(i)
            # print(edge_val, 'edge val')

            if le1 == edge_val:
                self.solved_edges.append(i)
                # print('the edge is solved')

            elif le2 == edge_val:
                self.flipped_edges.append(i)
                # print('the edge is flipped')
            else:
                self.unsolved_edges.append(i)
                # print('the edge is not solved')
            # print('-----------------')

    def show_cube(self):
        self.display_u_face()
        self.display_l_face()
        self.display_f_face()
        self.display_b_face()
        self.display_r_face()
        self.display_d_face()

    def edge_start_solve_li(self):
        if self.U_edges[0] == self.U_edges_init[0] or self.B_edges[0] == self.B_edges_init[0]:
            self.solved_edges.append('UB')
        elif self.U_edges[1] == self.U_edges_init[1] or self.R_edges[0] == self.R_edges_init[0]:
            self.solved_edges.append('UR')
        elif self.U_edges[3] == self.U_edges_init[3] or self.L_edges[0] == self.L_edges_init[0]:
            self.solved_edges.append('UL')
        elif self.D_edges[0] == self.D_edges_init[0] or self.F_edges[2] == self.F_edges_init[2]:
            self.solved_edges.append('DF')
        elif self.D_edges[1] == self.D_edges_init[1] or self.R_edges[2] == self.R_edges_init[2]:
            self.solved_edges.append('DR')
        elif self.D_edges[3] == self.D_edges_init[3] or self.L_edges[2] == self.L_edges_init[2]:
            self.solved_edges.append('DL')
        elif self.D_edges[2] == self.D_edges_init[2] or self.B_edges[2] == self.B_edges_init[2]:
            self.solved_edges.append('DB')
        elif self.F_edges[1] == self.F_edges_init[1] or self.R_edges[3] == self.R_edges_init[3]:
            self.solved_edges.append('FR')
        elif self.B_edges[3] == self.B_edges_init[3] or self.R_edges[1] == self.R_edges_init[1]:
            self.solved_edges.append('BR')
        elif self.L_edges[3] == self.L_edges_init[3] or self.B_edges[1] == self.B_edges_init[1]:
            self.solved_edges.append('BL')
        elif self.F_edges[3] == self.F_edges_init[3] or self.L_edges[1] == self.L_edges_init[1]:
            self.solved_edges.append('DB')

    def memo_edges(self):
        # put in func called get current state
        # Find the Piece in the UF position
        # TODO make a dict of opposite pairs
        # TODO make it memo with the UF UR swap if there is parity
        # First time with UF
        # get the memo in UF and then see where that piece goes
        # and then get the memo for that next piece
        # continue until one of these conditions is met
        # 1. all the edges are solved
        # 2. the buffer piece was hit and not all of the edges were solved
        # -------------------------
        # how to properly cycle break
        # 1. get the list of solved/memoed pieces
        # 2. pick one to cycle break to
        # -----------------------------------------------------------------
        # resources used:
        #   memo list: the letter pairs for memo
        #   list of unsolved edges: needs to be updated every time letters are added to memo list
        # self.edge_letter_to_val_at_loc(): takes memo letters and gets the value at the letter's starting location

        uf_val = self.U_edges[2]
        uf_loc = self.edge_used(uf_val)
        self.memo_li.append(uf_val)
        self.unsolved_edges.remove(uf_loc)
        print(self.unsolved_edges)


        if True:
            # Get new buffer
            # TODO put this in a new func? (getting a new buffer)
            buffer_loc = self.unsolved_edges[0]
            self.unsolved_edges.remove(buffer_loc)
            le1, _ = self.pos_to_letters[buffer_loc].split(' ')
            self.memo_li.append(le1)

            edge_val = self.get_buffer_val(buffer_loc)
            print(edge_val, 'edge val')
            self.memo_li.append(edge_val)
            edge_loc = self.edge_used(edge_val)
            self.unsolved_edges.remove(edge_loc)

            sticker6 = self.edge_letter_to_val_at_loc(edge_val)
            self.memo_li.append(sticker6)

        buffer_loc = self.unsolved_edges[0]
        self.unsolved_edges.remove(buffer_loc)
        le1, _ = self.pos_to_letters[buffer_loc].split(' ')
        self.memo_li.append(le1)

        edge_val = self.get_buffer_val(buffer_loc)
        print(edge_val, 'edge val')
        self.memo_li.append(edge_val)
        edge_loc = self.edge_used(edge_val)
        self.unsolved_edges.remove(edge_loc)

        sticker6 = self.edge_letter_to_val_at_loc(edge_val)
        self.memo_li.append(sticker6)

        buffer_loc = self.unsolved_edges[0]
        self.unsolved_edges.remove(buffer_loc)
        le1, _ = self.pos_to_letters[buffer_loc].split(' ')
        self.memo_li.append(le1)

        edge_val = self.get_buffer_val(buffer_loc)
        print(edge_val, 'edge val')
        self.memo_li.append(edge_val)
        edge_loc = self.edge_used(edge_val)
        try:
            self.unsolved_edges.remove(edge_loc)
        except:
            pass

        sticker6 = self.edge_letter_to_val_at_loc(edge_val)
        self.memo_li.append(sticker6)

        try:
            self.unsolved_edges.remove(piece5)
        except ValueError:
            print('piece not in unsolved edges')

    def scramble_cube_txt(self, new_s):
        for le in new_s:
            if le == "U":
                self.turn_u()
            elif le == "D":
                cube.turn_d()
            elif le == "R":
                cube.turn_r()
            elif le == "L":
                cube.turn_l()
            elif le == "F":
                cube.turn_f()
            elif le == "B":
                cube.turn_b()
            elif le == "U2":
                self.turn_u(2)
            elif le == "D2":
                cube.turn_d(2)
            elif le == "R2":
                cube.turn_r(2)
            elif le == "L2":
                cube.turn_l(2)
            elif le == "F2":
                cube.turn_f(2)
            elif le == "B2":
                cube.turn_b(2)
            elif le == "U'":
                self.turn_u(3)
            elif le == "D'":
                cube.turn_d(3)
            elif le == "R'":
                cube.turn_r(3)
            elif le == "L'":
                cube.turn_l(3)
            elif le == "F'":
                cube.turn_f(3)
            elif le == "B'":
                cube.turn_b(3)
            # TODO add primes and double turns


cube = Cube()
s = open("scrambles.txt", "r")
new_s = s.readline()
new_s = new_s.split(' ')
cube.scramble_cube_txt(new_s)
#
#


# Easy
# cube.turn_f(2)
# cube.turn_r()
# cube.turn_d(2)
# cube.turn_u(3)
# cube.turn_r(3)
# cube.turn_l()
# cube.turn_f(3)


# Hard
# cube.turn_u()
# cube.turn_f()
# cube.turn_b()
# cube.turn_l()
# cube.turn_r()
# cube.turn_u()
# cube.turn_d()
# cube.turn_r(3)
# cube.turn_f()
# cube.turn_u(2)

# cube.is_edge_solved()  # where this is put is important, after the cube is scrambled
cube.is_edge_solved()  # where this is put is important, after the cube is scrambled
cube.memo_edges()

# print('UR' in cube.used_edges)
# cube.show_cube()
print(cube.solved_edges, cube.unsolved_edges, cube.flipped_edges)


# print(cube.memo_li)
comma_offset = 2
for i in range(len(cube.memo_li)):
    if i % 2 == 0:
        cube.memo_li.insert(i + comma_offset, ',')
        comma_offset += 1

# Fixme Error when buffer is solved
try:
    cube.memo_li.pop(-1)
except IndexError:
    print('The list of solutions is empty.')
man = ' '.join([str(elem) for elem in cube.memo_li])
flip = ' '.join([str(elem) for elem in cube.flipped_edges])
if len(cube.flipped_edges) > 1:
    print(man, 'flipped edges', flip)
else:
    print(man, 'flipped edge', flip)
# cube.display_r_face()
# cube.display_b_face()
# cube.display_d_face()

# take value in buffer and find its spot
# Hi mom
