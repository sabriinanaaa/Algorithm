s = list(map(str, input().strip().split()))
print(" ".join(str(i) for i in s))


def quicksort(data, left, right):
    if left >= right:
        return

    pivot = data[right]
    i = left
    j = right-1

    while True:
        while data[i] < pivot and i < right:
            i += 1
        while data[j] >= pivot and j >= left:
            j -= 1
        if i < j:
            data[i], data[j] = data[j], data[i]
            print(" ".join(str(i) for i in data))
        else:
            break
    if right != i:
        data[right] = data[i]
        data[i] = pivot
        print(" ".join(str(i) for i in data))

    quicksort(data, left, i-1)   # 對pivot左邊再做一次
    quicksort(data, i+1, right)  # 對pivot右邊再做一次


quicksort(s, 0, len(s)-1)


# s = list(map(str, input().strip().split()))
# print(s)

# def quicksort(data, left, right):
#     if left >= right:
#         return

#     i = left                      # 左邊
#     j = right-1                     # 右邊
#     pivot = data[right]                 # pivot
#     print("left=", data[i], "right=", data[j], "pivot=", pivot)

#     while i != j:
#         # if data[j] < pivot:  # if右邊小於pivot，右邊和左邊調換
#         #     data[i], data[j] = data[j], data[i]
#         while data[j] >= pivot and j >= left:   # 從右邊開始找，if比pivot"大"就在往前找
#             j = j - 1
#         while data[i] < pivot and i < right:  # 從左邊開始找，if比pivot"小"就在往後找
#             i = i + 1
#         if i < j:                        # 當左右代理人沒有相遇時，互換值
#             data[i], data[j] = data[j], data[i]
#         print("i=", i, "j=", j, "\n", " ".join(str(i) for i in data))

#     # 將基準點歸換至代理人相遇點
#     # print(i, j)
#     data[j], data[right] = data[right], data[j]
#     # data[right] = data[j+1]
#     data[j] = pivot

#     quicksort(data, i+1, right)  # 繼續處理較大部分的子循環
#     quicksort(data, left, i-1)   # 繼續處理較小部分的子循環


# quicksort(s, 0, len(s)-1)

# 85 24 63 50 17 51 96 58
# from left
# data = [85, 24, 63, 50, 17, 51, 96, 58]

# def quicksort(data, left, right):  # 輸入資料，和從兩邊開始的位置
#     if left >= right:            # 如果左邊大於右邊，就跳出function
#         return

#     i = left                      # 左邊的代理人
#     j = right                     # 右邊的代理人
#     key = data[left]                 # 基準點
#     print("left=", data[i], "right=", data[j], "pivot=", key)

#     while i != j:
#         while data[j] > key and i < j:   # 從右邊開始找，找比基準點小的值
#             j -= 1
#         while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值
#             i += 1
#         if i < j:                        # 當左右代理人沒有相遇時，互換值
#             data[i], data[j] = data[j], data[i]
#             print(data)

#     # 將基準點歸換至代理人相遇點
#     data[left] = data[i]
#     data[i] = key

#     quicksort(data, left, i-1)   # 繼續處理較小部分的子循環
#     quicksort(data, i+1, right)  # 繼續處理較大部分的子循環


# quicksort(data, 0, len(data)-1)
# print(data)

# def quicksort(data, left, right):
#     if left < right:
#         x = partition(data, left, right)
#         quicksort(data, left, x - 1)
#         quicksort(data, x+1, right)


# def partition(data, left, right):
#     pivot = data[right]
#     i = left -1
#     for j in range(left, right):
#         if data[j] < pivot:
#             i += i
#             data[i], data[j] = data[j], data[i]
#     i += i
#     data[i], data[j] = data[j], data[i]
#     return i

# quicksort(s, 0, len(s)-1)
