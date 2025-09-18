import pygame

class Chess:

    def create_board(screen, board_size, square_size, bg_dirt, bg_grass):
        for row in range(board_size):
            for col in range(board_size):
                tile_image = bg_dirt if (row + col) % 2 == 0 else bg_grass
                screen.blit(tile_image, (col * square_size, row * square_size))

    def setup_chessboard(screen, board_size, square_size, pieces):
        for row in range(board_size):
            for col in range(board_size):
                if pieces[row][col]:
                    piece_image = pieces[row][col]
                    screen.blit(piece_image, (col * square_size, row * square_size))

    def draw_highlights(screen, board_size, square_size, highlights):
        for row in range(board_size):
            for col in range(board_size):
                if highlights[row][col]:
                    highlight_surface = pygame.Surface((square_size, square_size))
                    highlight_surface.set_alpha(128) 
                    highlight_surface.fill(pygame.Color("#FFFF00"))
                    screen.blit(highlight_surface, (col * square_size, row * square_size))

    def get_valid_moves(piece_type, row, col, board_size, pieces, piece_teams, current_piece):
        valid_moves = [[False] * board_size for _ in range(board_size)]
        current_team = piece_teams.get(current_piece, None)
        
        if piece_type == 'water_pawn':
            if row > 0 and not pieces[row-1][col]:
                valid_moves[row-1][col] = True
                if row == 6 and not pieces[row-2][col]:
                    valid_moves[row-2][col] = True
            for dc in [-1, 1]:
                if row > 0 and 0 <= col + dc < board_size:
                    target_piece = pieces[row-1][col+dc]
                    if target_piece and piece_teams.get(target_piece) != current_team:
                        valid_moves[row-1][col+dc] = True
                    
        elif piece_type == 'fire_pawn':
            if row < board_size-1 and pieces[row+1][col] is None:
                valid_moves[row+1][col] = True
                if row == 1 and pieces[row+2][col] is None:
                    valid_moves[row+2][col] = True
            for dc in [-1, 1]:
                if row < board_size-1 and 0 <= col + dc < board_size:
                    target_piece = pieces[row+1][col+dc]
                    if target_piece and piece_teams.get(target_piece) != current_team:
                        valid_moves[row+1][col+dc] = True
                    
        elif piece_type == 'knight':
            knight_moves = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
            for dr, dc in knight_moves:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < board_size and 0 <= new_col < board_size:
                    target_piece = pieces[new_row][new_col]
                    if target_piece is None or piece_teams.get(target_piece) != current_team:
                        valid_moves[new_row][new_col] = True
                    
        else:
            movement = {
                'bishop': [[-1, -1], [1, 1], [-1, 1], [1, -1]],  
                'rook': [[-1, 0], [1, 0], [0, -1], [0, 1]],   
                'queen': [[-1, -1], [1, 1], [-1, 1], [1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]],  
                'king': [[-1, -1], [1, 1], [-1, 1], [1, -1], [-1, 0], [1, 0], [0, -1], [0, 1]] 
            }
            
            if piece_type in movement:
                max_steps = 1 if piece_type == 'king' else 8
                directions = movement[piece_type]
                
                for dr, dc in directions:
                    for step in range(1, max_steps + 1):
                        new_row = row + dr * step
                        new_col = col + dc * step
                        
                        if 0 <= new_row < board_size and 0 <= new_col < board_size:
                            target_piece = pieces[new_row][new_col] 
                            if target_piece is None:  
                                valid_moves[new_row][new_col] = True
                            elif piece_teams.get(target_piece) != current_team:  
                                valid_moves[new_row][new_col] = True
                                break
                            else:
                                break
                        else:
                            break
        
        return valid_moves
