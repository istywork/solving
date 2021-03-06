from cmath import pi
import collections
import sys
import math

input = sys.stdin.readline

T = int(input().rstrip())

def convertToAngle(y,x,r) :

    degree = math.degrees(math.atan2(y,x))
    degree = degree if degree > 0 else degree + 360
    cover = 2*math.degrees(math.asin(r/16))
    return degree-cover, degree+cover

def solve(lines) :

    def solve_line(S, M) :

        covered_s = S
        covered_m = S
        idx = 0
        cnt = 0

        while idx < len(lines) :
            maxEnd = 0
            while idx < len(lines) and lines[idx][0] <= covered_m :
                maxEnd = max(maxEnd, lines[idx][1])
                idx += 1
            covered_m = maxEnd
            cnt += 1

            if covered_m >= M and covered_s <= S :
                return cnt

        # while문을 다 돌렸는데 S ~ M이 커버가 안된다면 실패
        return -10000000

    lines.sort()
    cnt = float('inf')

    for idx, line in enumerate(lines) :

        start = line[0]
        end = line[1]

        if start <= 0 or end >= 360:

            if start <=0 :
                range_end = 360+start
                range_start = end

            else :
                range_end = start
                range_start = end-360

            cnt = min(cnt, solve_line(range_start, range_end) + 1 )
    return cnt

for _ in range(T) :
    N = int(input().rstrip())
    R = 8
    check_points = []

    for _ in range(N) :
        y, x, r = map(float, input().rstrip().split())
        check_points.append(convertToAngle(y,x,r))

    ans = solve(check_points)

    if ans < 0 :
        print("IMPOSSIBLE")
    else :
        print(ans)