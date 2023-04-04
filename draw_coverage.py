from matplotlib import pyplot as plt
import sys
from typing import NamedTuple


class depth_entry(NamedTuple):
    id: str
    position: int
    value: int


def read_depth(file_path):
    with open(file_path, "r", encoding='utf-8') as handler:
        for line in handler.readlines():
            line = line.split()
            identifier = line[0]
            position = int(line[1])
            value = int(line[2])
            if value > 400:
                value = 400
            yield depth_entry(identifier, position, value)


def main():
    HORIZONTAL_LINES = "black"
    FILL_COLOR = "#a7aba8"
    EDGE_COLOR = "black"
    x = []
    y = []
    for entry in read_depth(sys.argv[1]):
        x.append(entry.position)
        y.append(entry.value)
    fig = plt.figure(figsize=(100, 2))
    ax = fig.subplots(1)
    ax.fill_between(x, y, color=FILL_COLOR,
                    edgecolor=EDGE_COLOR, linewidth=0.5)
    plt.xlim(0, max(x))
    plt.ylim(0, 421)
    plt.hlines(100, 0, max(x), color=HORIZONTAL_LINES, linewidth=0.5)
    plt.hlines(200, 0, max(x), color=HORIZONTAL_LINES, linewidth=0.5)
    plt.hlines(300, 0, max(x), color=HORIZONTAL_LINES, linewidth=0.5)
    plt.hlines(400, 0, max(x), color=HORIZONTAL_LINES, linewidth=0.5)
    plt.xticks(range(0, max(x), 200), fontsize=8)
    for i in range(0, len(x), 300):
        plt.text(i, 90, 100, fontsize=8)
        plt.text(i, 190, 200, fontsize=8)
        plt.text(i, 290, 300, fontsize=8)
        plt.text(i, 390, 400, fontsize=8)

    fig.savefig(sys.argv[0])


if __name__ == "__main__":
    main()
