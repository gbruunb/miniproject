import pygame
from pygame.locals import *
from chess import *

def main():
    pygame.init()

    board_size = 8
    square_size = 60 

    screen = pygame.display.set_mode((board_size * square_size, board_size * square_size), DOUBLEBUF)
    pygame.display.set_caption("Chess-prasangk-nsangkum")

    size = (square_size, square_size)
    
    # Load assets
    bg_dirt = pygame.transform.scale(pygame.image.load('assets/bg_dirt.png'), size)
    bg_grass = pygame.transform.scale(pygame.image.load('assets/bg_grass.png'), size)
    
    water_pawn = pygame.transform.scale(pygame.image.load('assets/water_pawn.png'), size)
    fire_pawn = pygame.transform.scale(pygame.image.load('assets/fire_pawn.png'), size)
    water_rook = pygame.transform.scale(pygame.image.load('assets/water_rook.png'), size)
    fire_rook = pygame.transform.scale(pygame.image.load('assets/fire_rook.png'), size)
    water_king = pygame.transform.scale(pygame.image.load('assets/water_king.png'), size)
    fire_king = pygame.transform.scale(pygame.image.load('assets/fire_king.png'), size)
    water_queen = pygame.transform.scale(pygame.image.load('assets/water_queen.png'), size)
    fire_queen = pygame.transform.scale(pygame.image.load('assets/fire_queen.png'), size)
    water_knight = pygame.transform.scale(pygame.image.load('assets/water_knight.png'), size)
    fire_knight = pygame.transform.scale(pygame.image.load('assets/fire_knight.png'), size)
    water_bishop = pygame.transform.scale(pygame.image.load('assets/water_bishop.png'), size)
    fire_bishop = pygame.transform.scale(pygame.image.load('assets/fire_bishop.png'), size)

    pieces = [[None] * 8 for _ in range(8)] 
    pieces[1] = [fire_pawn] * 8 
    pieces[6] = [water_pawn] * 8 

    # fire
    pieces[0][0] = fire_rook 
    pieces[0][1] = fire_knight 
    pieces[0][2] = fire_bishop
    pieces[0][3] = fire_king 
    pieces[0][4] = fire_queen 
    pieces[0][5] = fire_bishop
    pieces[0][6] = fire_knight
    pieces[0][7] = fire_rook 

    # water
    pieces[7][0] = water_rook 
    pieces[7][1] = water_knight 
    pieces[7][2] = water_bishop
    pieces[7][3] = water_king 
    pieces[7][4] = water_queen 
    pieces[7][5] = water_bishop
    pieces[7][6] = water_knight
    pieces[7][7] = water_rook 

    selected_piece = None
    selected_pos = None
    highlights = [[False] * 8 for _ in range(8)]
    
    piece_types = {
        water_pawn: 'water_pawn', fire_pawn: 'fire_pawn',
        water_rook: 'rook', fire_rook: 'rook',
        water_king: 'king', fire_king: 'king',
        water_queen: 'queen', fire_queen: 'queen',
        water_knight: 'knight', fire_knight: 'knight',
        water_bishop: 'bishop', fire_bishop: 'bishop'
    }
    
    piece_teams = {
        water_pawn: 'water', fire_pawn: 'fire',
        water_rook: 'water', fire_rook: 'fire',
        water_king: 'water', fire_king: 'fire',
        water_queen: 'water', fire_queen: 'fire',
        water_knight: 'water', fire_knight: 'fire',
        water_bishop: 'water', fire_bishop: 'fire'
    }

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                clicked_col = mouse_x // square_size
                clicked_row = mouse_y // square_size
                
                if 0 <= clicked_row < board_size and 0 <= clicked_col < board_size:
                    clicked_piece = pieces[clicked_row][clicked_col]
                    
                    if selected_piece and highlights[clicked_row][clicked_col]:
                        # move piece
                        pieces[clicked_row][clicked_col] = selected_piece
                        pieces[selected_pos[0]][selected_pos[1]] = None
                        
                        # cancel select
                        selected_piece = None
                        selected_pos = None
                        highlights = [[False] * 8 for _ in range(8)]
                        
                    elif clicked_piece: 
                        selected_piece = clicked_piece
                        selected_pos = (clicked_row, clicked_col)
                        highlights = [[False] * 8 for _ in range(8)]
                        
                        if clicked_piece in piece_types:
                            piece_type = piece_types[clicked_piece]
                            highlights = Chess.get_valid_moves(piece_type, clicked_row, clicked_col, board_size, pieces, piece_teams, clicked_piece)
                    else:
                        selected_piece = None
                        selected_pos = None
                        highlights = [[False] * 8 for _ in range(8)]

        Chess.create_board(screen, board_size, square_size, bg_dirt, bg_grass)
        Chess.draw_highlights(screen, board_size, square_size, highlights)
        Chess.setup_chessboard(screen, board_size, square_size, pieces) 
        pygame.display.flip()

if __name__ == "__main__":
    main()
