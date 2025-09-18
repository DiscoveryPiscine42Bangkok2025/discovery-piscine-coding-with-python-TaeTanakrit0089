#!/usr/bin/env python3

VALID_PIECES = set("KQRBP")


def parse_board(board_text):
    """Parse the board text into a list and validation"""
    rows = [line.rstrip("\n")
            for line in board_text.splitlines() if line.strip() != ""]
    if not rows:
        return None

    board_size = len(rows)

    if any(len(row) != len(rows[0]) for row in rows):
        return None
    if len(rows[0]) != board_size:
        return None

    king_count = 0
    king_position = None
    for row_index in range(board_size):
        for col_index in range(board_size):
            ch = rows[row_index][col_index]

            valid_pieces = VALID_PIECES.union({'.'})

            if ch not in valid_pieces:
                return None

            if ch == 'K':
                king_count += 1
                king_position = (row_index, col_index)

    if king_count != 1:
        return None

    return rows, board_size, king_position


def in_bounds(row, col, board_size):
    """Validate if (row, col) is within the board boundaries"""
    return 0 <= row < board_size and 0 <= col < board_size


def first_piece_along(board, board_size, start_row, start_col, delta_row, delta_col):
    """Shoot a ray from (start_row+delta_row, start_col+delta_col) in the given direction"""
    row, col = start_row + delta_row, start_col + delta_col
    while in_bounds(row, col, board_size):
        cell = board[row][col]
        if cell in VALID_PIECES:
            return cell
        row += delta_row
        col += delta_col
    return '.'


def king_in_check(board, board_size, king_row, king_col):
    """Check if King is in attacked by Pawn/Bishop/Rook/Queen"""

    # Pawn (กินทแยงหนึ่งช่อง)
    for delta_col in (-1, 1):
        row = king_row + 1
        col = king_col + delta_col
        if in_bounds(row, col, board_size) and board[row][col] == 'P':
            return True

    # Bishop/Queen แนวทแยง
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for delta_row, delta_col in diagonal_directions:
        piece = first_piece_along(
            board, board_size, king_row, king_col, delta_row, delta_col)
        if piece in ('B', 'Q'):
            return True

    # Rook/Queen แนวตรง
    orthogonal_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for delta_row, delta_col in orthogonal_directions:
        piece = first_piece_along(
            board, board_size, king_row, king_col, delta_row, delta_col)
        if piece in ('R', 'Q'):
            return True

    return False


def checkmate(board_text):
    """Print "Success" if King is in check, otherwise "Fail"."""
    parsed = parse_board(board_text)
    if parsed is None:
        return
    board, board_size, (king_row, king_col) = parsed

    if king_in_check(board, board_size, king_row, king_col):
        print("Success")
    else:
        print("Fail")
