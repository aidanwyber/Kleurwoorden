import json

with open("wordlist-ascii-NL.txt") as file:
    # https://github.com/OpenTaal/opentaal-wordlist/blob/master/elements/wordlist-ascii.txt
    words = [x.strip().lower() for x in file.readlines()]

accept = list("abcdef")
letter_subs = {"o": "0", "l": "1", "i": "1", "z": "2", "s": "5", "t": "7", "g": "9"}


def is_colour(word):
    return len(word) == 6 and all(
        [letter in letter_subs.keys() or letter in accept for letter in word]
    )


colour_words = [word for word in words if is_colour(word)]


def sub_word(word):
    return "".join(
        [letter_subs[letter] if letter in letter_subs else letter for letter in word]
    )


colours = ["#" + sub_word(word).upper() for word in colour_words]

output = {}
for x in zip(colour_words, colours):
    output[x[0]] = x[1]

with open("colour_words.json", "w") as out:
    out.write(json.dumps(output))

print(f"Written {len(colours)} colour words.")
