def solution():
    soundlist = input().split(" ")
    if "".join(soundlist) == "12345678":
        print("ascending")
    elif "".join(soundlist) == "87654321":
        print("descending")
    else:
        print("mixed")

if __name__ == "__main__":
    solution()