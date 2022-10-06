def solution(n, m, x, y, r, c, k):
    pathlist = [[[x, y]]]
    answer = []

    def dfs(path, r=r, c=c, k=k):
        p = path.pop()
        print(p)
        if len(p) > k:
            # print("length exceeded")
            return
        node = p[-1]
        print("current path and node: ", p, node)
        if node == [r, c]:
            if len(p) == k:
                # print("path found! ", p)
                answer.append(p)
                return
            else:
                return

        u, d, l, r = (
            [node[0], node[1] - 1],
            [node[0], node[1] + 1],
            [node[0] - 1, node[1]],
            [node[0] + 1, node[1]],
        )
        # print(u,d,l,r)
        for k in u, d, r, l:
            # print("nextnode : ", k)
            if k[0] < 1 or n < k[0] or k[1] < 1 or m < k[1]:
                # print("not available")
                continue
            else:
                p.append(k)
                pathlist.append(p)
                # print("go")
                dfs(pathlist)

    dfs(pathlist)
    print(answer)
    return answer


print(solution(2, 2, 1, 1, 2, 2, 2))
