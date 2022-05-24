class qtwo:
    def pair_of_ele(self, arr, total):
        lookup = {}
        for i, num in enumerate(arr):

            if total - num in lookup:
                return (lookup[total - num], i)
            lookup[num] = i


arr = [10, 20, 30, 40, 50, 60, 70]
sum = 80

print("index1 = %d, index2 = %d" %
      qtwo().pair_of_ele((10, 20, 10, 40, 50, 60, 70), 80))
