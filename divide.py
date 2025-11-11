def divide(a, b):
    # バグ: bが0のときの処理なし
    return a / b

def calc_average(numbers):
    total = 0
    for n in numbers:
        total += divide(n, len(numbers))  # バグ: 平均計算として意味不明
    return total  # バグ: 割り算を二重にしていない

def main():
    nums = [10, 0, 5]
    print("Average:", calc_average(nums))  # バグ: divideでZeroDivisionErrorの可能性

if __name__ == "__main__":
    main()

