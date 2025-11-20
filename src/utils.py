from pathlib import Path

RAW_DATA_DIR = Path("./data/raw")

def main():
    if not RAW_DATA_DIR.exists():
        print("RAW_DATA_DIR does not exist!")
    else:
        print("RAW_DATA_DIR exists.")
        for file in RAW_DATA_DIR.iterdir():
            print(f" - {file.name}")

if __name__ == "__main__":
    main()