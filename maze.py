from matplotlib import pyplot as plt

def maze(file, savefile, path_to_goal, clear=False):
    if clear:
        plt.clf()
    walls = [[], []]
    start = [[], []]
    end = [[], []]
    path = [[], []]

    with open(file, 'r') as maze:
        l = 0
        for line in maze:
            for c, col in enumerate(line.strip('\n')):
                if col == '#':
                    walls[0].append(c)
                    walls[1].append(-l)
                elif col == 'A':
                    start[0].append(c)
                    start[1].append(-l)
                elif col == 'B':
                    end[0].append(c)
                    end[1].append(-l)
                elif (c, l) in path_to_goal:
                    path[0].append(c)
                    path[1].append(-l)


            l += 1

    plt.scatter(walls[0], walls[1], marker='s', color='black', s=50)
    plt.scatter(start[0], start[1], marker='$S$', color='red')
    plt.scatter(end[0], end[1], marker='$E$', color='red')
    plt.scatter(path[0], path[1], marker='o', color='red')
    plt.axis('off')
    plt.savefig(savefile)