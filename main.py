import matplotlib.pyplot as plt
import threading

plt.xlabel("X-Werte")
plt.ylabel("Y-Werte")

plt.ion()


def plot_graph(i):
    # print(f"--------------------------------Checking 3n+1 for {i}-----------------------------------------")
    data = []
    x = int(i)
    while x != 1:
        if x in data:
            print(f"!!!!!!!!!!!!!!!!!!!!!!!{i} is a cycle?!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

        data.append(x)

        if x % 2 == 0:
            x = int(x / 2)

        elif x % 2 == 1:
            x = int(x * 3 + 1)

        else:
            print("Error")
            break

    # print(f"--------------------------------Finished checking 3n+1 for {i}--------------------------------")
    plt.plot(data)
    data = []


def main():
    for i in range(1, 1000):
        t = threading.Thread(target=plot_graph, args=(i,))
        t.start()


main()
plt.show()
