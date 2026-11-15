def next_level(level, score):
    if score >= 0.8:
        return min(level + 1, 6)
    elif score < 0.5:
        return max(level - 1, 1)
    return level


print(next_level(6, 0.9))
print(next_level(3, 0.3))
print(next_level(1, 0.2))
print(next_level(3, 0.6))
print(next_level(3, 0.8))
