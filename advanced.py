def relationship_status(from_member, to_member, social_graph):
    if to_member in social_graph[from_member]["following"]:
        if from_member in social_graph[to_member]["following"]:
            return "friends"
        else:
            return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"

def eta(first_stop, second_stop, route_map):
    total_travel_time = 0
    current_stop = first_stop
    while current_stop != second_stop:
        for (start, end), time_info in route_map.items():
            if start == current_stop:
                total_travel_time += time_info['travel_time_mins']
                current_stop = end
                break
    return total_travel_time

def tic_tac_toe(board):
    size = len(board)
    for i in range(size):
        if all(board[i][0] == board[i][j] != '' for j in range(size)):
            return board[i][0]
        if all(board[0][i] == board[j][i] != '' for j in range(size)):
            return board[0][i]
    if all(board[0][0] == board[i][i] != '' for i in range(size)):
        return board[0][0]
    if all(board[0][size-1] == board[i][size-1-i] != '' for i in range(size)):
        return board[0][size-1]
    return "NO WINNER"
