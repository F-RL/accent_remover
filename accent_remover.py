import unicodedata
import codecs

def remove_accents(s: str) -> str:
    r_s = ""
    s_n = unicodedata.normalize("NFD", s)
    for c in s_n:
        b_c = codecs.encode(c, "utf-8")
        if len(b_c) > len(c):
            r_s = s_n.replace(b_c.decode("utf-8"), "")
    return r_s

if __name__ == "__main__":
    from sys import argv
    if len(argv) != 2:
        print("Wrong number of arguments\nTry \"py accent_remover.py [YOUR STRING]\"")

    result = remove_accents(argv[-1])
    print(result)
