import datetime
import os
import locale

def write_build_date():
    locale.setlocale(locale.LC_TIME, "da_DK.utf8")
    build_date = datetime.datetime.now().strftime("%d. %B %Y")
    with open("builddate.txt", "w") as f:
        f.write(f"{build_date}")

if __name__ == "__main__":
    write_build_date()
