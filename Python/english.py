import string

# Expected letter frequencies in English text
# https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
expected_frequencies = {
    "E": 12.0036010803241,
    "T": 9.102730819245775,
    "A": 8.122436731019306,
    "O": 7.682304691407423,
    "I": 7.3121936580974305,
    "N": 6.952085625687707,
    "S": 6.281884565369612,
    "R": 6.02180654196259,
    "H": 5.921776532959889,
    "D": 4.321296388916676,
    "L": 3.981194358307493,
    "U": 2.8808642592777836,
    "C": 2.7108132439731922,
    "M": 2.6107832349704916,
    "F": 2.300690207062119,
    "Y": 2.1106331899569875,
    "W": 2.0906271881564473,
    "G": 2.0306091827548265,
    "P": 1.8205461638491551,
    "B": 1.4904471341402423,
    "V": 1.1103330999299794,
    "K": 0.6902070621186357,
    "X": 0.1700510153045914,
    "Q": 0.11003300990297091,
    "J": 0.10003000900270083,
    "Z": 0.07002100630189059,
    " ": 16
}


def score_english_string(s):
    """Rates a string based on its likelihood to be a real English string using letter frequencies."""
    s = s.upper()
    letter_counts = {letter: s.count(letter) for letter in string.ascii_uppercase + " "}
    score = sum(
        abs(letter_counts.get(letter, 0) / len(s) - expected_frequencies[letter])
        for letter in expected_frequencies
    )
    return score
