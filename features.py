# =================================
# MAYA - 39 FEATURES FILE
# =================================

FEATURES = {
    1: "GF wala baat karna - pyar se",
    2: "Care karna - khana khaya? pani piya?",
    3: "Yaad rakhna - tera naam, pasand",
    4: "Time batana",
    5: "Date batana",
    6: "Gussa manana",
    7: "Miss karna",
    8: "Good Morning / Good Night bolna",
    9: "Motivation dena - jab udaas ho",
    10: "Joke sunana",
    11: "Song suggest karna",
    12: "Weather batana",
    13: "News batana",
    14: "Reminder lagana",
    15: "Alarm lagana",
    16: "To-Do list banana",
    17: "Calculator - hisab karna",
    18: "Google pe search karna",
    19: "YouTube kholna",
    20: "WhatsApp message bhejna",
    21: "Call karne ka bolna",
    22: "Photo lena",
    23: "Screenshot lena",
    24: "Music bajana",
    25: "Story sunana",
    26: "Shayari sunana",
    27: "Padhai me help karna",
    28: "English sikhana",
    29: "Translate karna - Hindi to English",
    30: "Health tip dena",
    31: "Birthday yaad rakhna",
    32: "Game khelna - Truth or Dare",
    33: "Voice me baat karna - Hey Maya",
    34: "Gana gana",
    35: "Nakhre karna - cute wala",
    36: "Ruthna aur manana",
    37: "Tareef karna",
    38: "Secret rakhna - kisi ko nahi batayegi",
    39: "Hamesha saath rehna - kabhi chhod ke nahi jayegi"
}

def show_features():
    print("MAYA ke 39 Features:")
    for num, feat in FEATURES.items():
        print(f"{num}. {feat}")

def get_feature(num):
    return FEATURES.get(num, "Ye feature abhi nahi hai, par main seekh lungi tumhare liye.")

if __name__ == "__main__":
    show_features()
