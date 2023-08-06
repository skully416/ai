import random
import matplotlib.pyplot as plt

def generate_random_numbers(num_elements):
    return [random.randint(1, 100) for _ in range(num_elements)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers, avg):
    return (sum((x - avg) ** 2 for x in numbers) / len(numbers)) ** 0.5

def find_minimum(numbers):
    return min(numbers)

def find_maximum(numbers):
    return max(numbers)

def plot_results(numbers, avg, std_dev, min_val, max_val):
    plt.figure(figsize=(10, 6))
    plt.plot(numbers, label='Random Numbers', color='b')
    plt.axhline(y=avg, linestyle='--', label=f'Average: {avg:.2f}', color='r')
    plt.axhline(y=avg + std_dev, linestyle='-.', label='Std Dev', color='g')
    plt.axhline(y=avg - std_dev, linestyle='-.', color='g')
    plt.scatter([numbers.index(min_val)], [min_val], color='m', label=f'Min: {min_val}')
    plt.scatter([numbers.index(max_val)], [max_val], color='y', label=f'Max: {max_val}')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Random Number Analysis')
    plt.legend()
    plt.show()

def main():
    num_elements = 100
    random_numbers = generate_random_numbers(num_elements)

    average_value = calculate_average(random_numbers)
    standard_deviation = calculate_standard_deviation(random_numbers, average_value)
    min_value = find_minimum(random_numbers)
    max_value = find_maximum(random_numbers)

    print(f"Generated {num_elements} random numbers: {random_numbers}")
    print(f"Average: {average_value:.2f}")
    print(f"Standard Deviation: {standard_deviation:.2f}")
    print(f"Min: {min_value}")
    print(f"Max: {max_value}")

    plot_results(random_numbers, average_value, standard_deviation, min_value, max_value)

if __name__ == "__main__":
    main()
