def minion_game(string):
    # your code goes here
    # s = input()
    k = ['A', 'E', 'I', 'O', 'U']

    k_points = 0
    s_points = 0

    for i in range(len(string)):
        if string[i] in k:
            k_points += len(string) - i
        else:
            s_points += len(string) - i

    if k_points > s_points:
        print('Kevin', k_points)
    elif s_points > k_points:
        print('Stuart', s_points)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)`