def merge(self, start, end):
    temp = []
    mid = int((start + end) / 2)
    leftIndex = start
    rightIndex = mid + 1
    while True:
        if(getChoice(self.list[leftIndex], self.list[rightIndex])):
            temp.append(self.list[leftIndex])
            leftIndex += 1
        else:
            temp.append(self.list[rightIndex])
            rightIndex += 1
        if leftIndex > mid:
            for i in range(rightIndex, end + 1):
                temp.append(self.list[i])
            break
        elif rightIndex > end:
            for i in range(leftIndex, mid + 1):
                temp.append(self.list[i])
            break


def getChoice(e1, e2):
    if e1 < e2:
        return True
    else:
        return False
