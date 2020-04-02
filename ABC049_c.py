s = input()
t = ""

ans = "YES"
while len(s) > 0:
    if s[-1] == "m" or s[-1] == "e":
        if s[-5:] == "dream" or s[-5:] == "erase":
            s = s[:-5]
        else:
            ans = "NO"
            break
    elif s[-1] == "r":
        if s[-7:] == "dreamer":
            s = s[:-7]
        elif s[-6:] == "eraser":
            s = s[:-6]
        else:
            ans = "NO"
            break
    else:
        ans = "NO"
        break

print(ans)
