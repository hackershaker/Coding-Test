def change(before: str, after: str) -> int: # 65:A ~ 90:Z
    right = ord(after)-ord(before) if ord(after) >= ord(before) else 26 - (ord(before)-ord(after))
    left = ord(before)-ord(after) if ord(before) >= ord(after) else 26 - (ord(after)-ord(before))

    return min(left, right)


def findright(wordlist, idx, name):
    right = 1
    while True:
        if right == len(name):
            break
        if (
            name[(idx + right) % len(name)] == "A"
            or wordlist[(idx + right) % len(name)] == name[(idx + right) % len(name)]
        ):
            right += 1
        else:
            break
    rightidx = (idx + right) % len(name)
    return rightidx, abs(right)


def findleft(wordlist, idx, name):
    left = -1
    while True:
        if abs(left) == len(name):
            break
        if (
            name[(idx + left + len(name)) % len(name)] == "A"
            or wordlist[(idx + left + len(name)) % len(name)]
            == name[(idx + left + len(name)) % len(name)]
        ):
            left -= 1
        else:
            break
    leftidx = (idx + left + len(name)) % len(name)
    return leftidx, abs(left)


def solution(name):

    def minimumJoystick(idx: int, word: str, count):  # 현재 위치, 현재 단어
        # print(f"index:{idx}, word:{word}, current count: {count}")
        if word == name:
            return count

        # left
        leftidx, leftmove = findleft(word, idx, name)
        # print(f"index move {idx} to {leftidx}, moving distance is {leftmove}")
        ifleftcount = (
            minimumJoystick(
                leftidx,
                word[:leftidx] + name[leftidx] + word[leftidx + 1:],
                count + leftmove + change(word[leftidx], name[leftidx]),
            )
        )

        # right
        rightidx, rightmove = findright(word, idx, name)
        # print(f"index move {idx} to {rightidx}, moving distance is {rightmove}")
        ifrightcount = (
            minimumJoystick(
                rightidx,
                word[:rightidx] + name[rightidx] + word[rightidx + 1:],
                count + rightmove + change(word[rightidx], name[rightidx]),
            )
        )

        # print(
        #     f"start from {idx}, left move count : {ifleftcount}, right move count: {ifrightcount}, {word} -> {name}"
        # )
        return min(ifleftcount, ifrightcount)

    initword = name[0] + "A"*(len(name)-1)
    answer = minimumJoystick(0, initword, change("A", name[0]))

    return answer
