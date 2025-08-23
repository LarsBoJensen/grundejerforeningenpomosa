import datetime
import os
import locale

def write_build_date():
    try:
        locale.setlocale(locale.LC_TIME, "da_DK.utf8")
    except locale.Error:
        try:
            # Try alternative Danish locale names
            locale.setlocale(locale.LC_TIME, "da_DK.UTF-8")
        except locale.Error:
            try:
                locale.setlocale(locale.LC_TIME, "da_DK")
            except locale.Error:
                # Fallback to default locale if Danish is not available
                print("Warning: Danish locale not available, using default locale")
                pass
    
    build_date = datetime.datetime.now().strftime("%d. %B %Y")
    with open("builddate.txt", "w") as f:
        f.write(f"{build_date}")
    with open("docs/builddate.txt", "w") as f:
        f.write(f"{build_date}")

if __name__ == "__main__":
    write_build_date()
