
class chessRepo:
    def __init__(self) -> None:
        self.n=8
        self.chess_board_mapping = {1:"A", 2: "B", 3: "C", 4:"D", 5:"E", 6:"F", 7:"G", 8:"H"}
        self.chess_board=[[0 for _ in range(8)] for _ in range(8)]  

    
    def board_key(self, xx, yy):
        return str(self.chess_board_mapping.get(yy+1))+str(xx+1)

    def knigth_moves(self,x,y):
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [-1, -2, -2, -1, 1, 2, 2, 1]
        n=self.n
        valid_move_list = []

        for k in range(0, 8):

            # within the chessboard
            next_x = dx[k] + x
            next_y = dy[k] + y
            if (next_x >= 0 and
                next_x <= n - 1 and
                next_y >= 0 and
                next_y <= n - 1):

                if self.chess_board[next_x][next_y] in [0,1]:
                    if self.chess_board[next_x][next_y]==0:
                        key = self.board_key(next_x, next_y)
                        valid_move_list.append(key)
                    
                    self.chess_board[next_x][next_y] = 1 

        
        return valid_move_list

    
    def rook_moves(self, x, y):
        valid_move_list = []
        for i in range(0,8):
            if i==y:
                continue
            
            if self.chess_board[x][i] in [0,1]:
                if self.chess_board[x][i] == 0:
                    key = self.board_key(x, i)
                    valid_move_list.append(key)
                
                self.chess_board[x][i] = 1 

            else:
                key = self.board_key(x, i)
                valid_move_list.append(key)
                break
        
        for i in range(0,8):
            if i==x:
                continue
            
            if self.chess_board[i][y] in [0,1]:
                
                if self.chess_board[i][y]==0:
                    key = self.board_key(i,y)
                    valid_move_list.append(key)
                
                self.chess_board[i][y] = 1 

            else:
                key = self.board_key(i, y)
                valid_move_list.append(key)
                break

        return valid_move_list
    
    def bishop_moves(self, x, y):
        n=self.n
        valid_move_list = []
        temp_x=x-1
        temp_y=y-1

        #for down side left direction
        while(temp_x>0 and temp_y>0):
            if self.chess_board[temp_x][temp_y] in [0,1]:
                
                if self.chess_board[temp_x][temp_y]==0:
                    key = self.board_key(temp_x, temp_y)
                    valid_move_list.append(key)

                self.chess_board[temp_x][temp_y] = 1 

            else:
                key = self.board_key(temp_x, temp_y)
                valid_move_list.append(key)
                break
            temp_x -= 1
            temp_y -= 1
        
        temp_x=x+1
        temp_y=y-1

        #for down side right direction
        while(temp_x<n and temp_y>0):
            if self.chess_board[temp_x][temp_y] in [0,1]:
                self.chess_board[temp_x][temp_y] = 1 

                if self.chess_board[temp_x][temp_y]==0:
                    key = self.board_key(temp_x, temp_y)
                    valid_move_list.append(key)
                
                self.chess_board[temp_x][temp_y] = 1 

            else:
                key = self.board_key(temp_x, temp_y)
                valid_move_list.append(key)
                break
            temp_x += 1
            temp_y -= 1

        temp_x=x-1
        temp_y=y+1

        #for up side left direction
        while(temp_x>0 and temp_y<n):
            if self.chess_board[temp_x][temp_y] in [0,1]:
                
                if self.chess_board[temp_x][temp_y]==0:
                    key = self.board_key(temp_x, temp_y)
                    valid_move_list.append(key)
                
                self.chess_board[temp_x][temp_y] = 1 

            else:
                key = self.board_key(temp_x, temp_y)
                valid_move_list.append(key)
                break
            temp_x -= 1
            temp_y += 1
        
        temp_x=x+1
        temp_y=y+1

        #for up side right direction
        
        while(temp_x<n and temp_y<n):
            if self.chess_board[temp_x][temp_y] in [0,1]:
                
                if self.chess_board[temp_x][temp_y]==0:
                    key = self.board_key(temp_x, temp_y)
                    valid_move_list.append(key)
                
                self.chess_board[temp_x][temp_y] = 1 

            else:
                key = self.board_key(temp_x, temp_y)
                valid_move_list.append(key)
                break
            temp_x += 1
            temp_y += 1


        return valid_move_list


        
    
    def queen_moves(self, x, y):
        valid_move_list = []
        rook_moves_response = self.rook_moves(x,y)
        bishop_moves_response = self.bishop_moves(x,y)
        valid_move_list.extend(rook_moves_response)
        valid_move_list.extend(bishop_moves_response)
        return valid_move_list

    def get_piece_function(self, piece_name, x,y):
        if piece_name.lower() == 'knight':
            moves_res = self.knigth_moves(x,y)
        
        elif piece_name.lower() == 'queen':
            moves_res = self.queen_moves(x,y)
        
        elif piece_name.lower() == 'rook':
            moves_res = self.rook_moves(x,y)

        elif piece_name.lower() == 'bishop':
            moves_res = self.bishop_moves(x,y)

        return moves_res


    def set_working(self,payload, slug):

        
        if  slug.lower() not in ['queen', 'knight', 'rook', 'bishop']:
            response = {'staus':'failure', "msg":"invalid slug"}
            return response

        key_position = payload.get("postions",{})
        reverse_chess_mapping = {}
        for num, alpha in self.chess_board_mapping.items():
            reverse_chess_mapping[alpha]=num

        for key, value in key_position.items():
            player_position = [*value]
            if key.lower() != slug:
                y = reverse_chess_mapping.get(player_position[0])-1
                x = int(player_position[1])-1
                # print("--->", x, "  ",y)
                self.chess_board[x][y] = 2
                moves = self.get_piece_function(key, x, y)

            else:
                slug = key

        
        player_position = key_position.get(slug,'')
        y = reverse_chess_mapping.get(player_position[0])-1
        x = int(player_position[1])-1
        self.chess_board[x][y] = 2

        moves = self.get_piece_function(slug, x, y)
        return {"valid_moves": list(set(moves))}
        



