"""Dog110!"""

pack: list[dict[str, str]] = [
    {"name": "Nelli", "score": "10"},
    {"name": "Ada", "score": "9"},
    {"name": "Pip", "score": "7"},
]

# base case 1: current dog is not good --> False
# base case 2: if dog is good and last dog --> True

# recursive case: check rest of list by incrementing index
# edge case: index not valid


# all_good function defintion below


def all_good(scores: list[dict[str, str]], thresh: int, idx: int) -> bool:
    is_good: bool = int(scores[idx]["score"]) >= thresh
    is_last: bool = idx + 1 == len(scores)
    if is_good:
        if is_last:
            return True
        else:
            return all_good(scores, thresh, idx + 1)
    else:
        return False


print(all_good(scores=pack, thresh=7, idx=0))
