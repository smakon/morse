# . is 1
# - is 0
import keyboard as key

result = " "
words = {"A": "10",
         "B": "0111",
         "C": "0101",
         "D": "011",
         "E": "1",
         "F": "1101",
         "G": "001",
         "H": "1111",
         "I": "11",
         "J": "1000",
         "K": "010",
         "L": "1011",
         "M": "00",
         "N": "01",
         "O": "000",
         "P": "1001",
         "Q": "0010",
         "R": "101",
         "S": "111",
         "T": "0",
         "U": "110",
         "V": "1110",
         "W": "100",
         "X": "0110",
         "Y": "0100",
         "Z": "0011",
         }
wordeee = []


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k

def word():
    global wordeee, words
    res = "".join(wordeee)
    val = words.values()
    if str(res) in val:
        global result
        result += get_key(words, res)
        wordeee.clear()
        return result
    else:
        print("Err")
        wordeee.clear()


key.add_hotkey('1', lambda: wordeee.append("1"))
key.add_hotkey('0', lambda: wordeee.append("0"))
key.add_hotkey('space', lambda: word())
key.add_hotkey('q', lambda: print(result))
key.wait("esc")
