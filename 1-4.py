import argparse

def optimal_weight(W, golds, bars_num):
    d = [[True] + [False] * W]

    for i in range(bars_num):
        d.append(d[-1][:])
        for w in range(golds[i], W + 1):
            d[-1][w] = d[-2][w] or d[-2][w - golds[i]]
        d = d[-1:]
    for w in range(W, -1, -1):
        if d[-1][w]:
            return w

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Take bag capacity, weights weight and number of weights bars  - ")
    parser.add_argument("-W", type=int, help="Give capacity of the bag")
    parser.add_argument("-w", nargs="+", type=int, help="Give weights of weights bars")
    parser.add_argument("-n", type=int, help="Give the number of weights bars")

    input_args = parser.parse_args()

    capacity = input_args.W
    weights  = input_args.w
    bars_num = input_args.n

    print(optimal_weight(capacity, weights, bars_num))