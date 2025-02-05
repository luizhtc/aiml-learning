import matplotlib.pyplot as plt

def plot_cluster(data, labels, title):
    colors = ['red', 'green', 'purple', 'black']
    plt.figure(figsize=(8, 4))

    for i, l in zip(range(-1, 3), ['Noise', 'Setosa', 'Versicolor', 'Virginica']):
        if i == -1:
            plt.scatter(data[labels == i, 0], data[labels == i, 3], c=colors[i], label=l, alpha=0.5, s=50, marker='x')

        if i != -1:
            plt.scatter(data[labels == i, 0], data[labels == i, 3], c=colors[i], label=l, alpha=0.5, s=50)

        plt.legend()
        plt.title(title)
        plt.xlabel('Sepal Length')
        plt.ylabel('Petal Width')
        plt.show()
