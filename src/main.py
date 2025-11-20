from utils import RAW_DATA_DIR

def main():
    print(f"Checking RAW_DATA_DIR at: {RAW_DATA_DIR}")
    if not RAW_DATA_DIR.exists():
        print("RAW_DATA_DIR does not exist!")
    else:
        print("RAW_DATA_DIR exists.")
        for file in RAW_DATA_DIR.iterdir():
            print(f" - {file.name}")


if __name__ == "__main__":
    main()
