def add(x, y):
    return x + y

def divide(x, y):
    # ゼロ除算を考慮していない
    return x / y

def main():
    numbers = [10, 0, 5]
    total = 0
    for i in range(len(numbers)):
        total = add(total, divide(numbers[i], i))  # バグあり: iが0になる
    print("Total:", total)

if __name__ == "__main__":
    main()

