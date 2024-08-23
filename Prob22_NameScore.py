def get_single_score(name: str) -> int:
    """Gets score for given name. e.g. COLIN = 53"""
    score = 0
    for letter in name:
        assert (ord(letter) >= ord('A'))
        assert (ord(letter) <= ord('Z'))
        letter_score = ord(letter) - ord('A') + 1
        score += letter_score
    return score


assert (get_single_score("COLIN") == 53)


def get_sorted_names() -> list[str]:
    names = open("/Users/rudra/Documents/code/VSCodeFiles/Python/Euler's Project Code/Prob22_names.txt").read().split(',')
    new_names = []
    for name in names:
        new_names.append(name.replace('"', ''))
    new_names.sort()  # alphabetically sorts the list
    names = new_names
    return names


names = get_sorted_names()

total_score = 0
for i, name in enumerate(names):
    position = i + 1
    mul_score = position * get_single_score(name)
    total_score += mul_score

print(total_score)
