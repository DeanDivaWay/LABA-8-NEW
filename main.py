def kbig(nums: str, k: str) -> int:
    nums = [int(i) for i in nums.split()]
    for i in range(int(k) - 1):
        nums.remove(max(nums))
    return max(nums)


if __name__ == "__main__":
    l = input("Введите список чисел:\n")
    ind_el = input("Введите номер числа по убываю, которое нужно найти:\n")
    print(f'Ответ: {kbig(l, ind_el)}')
