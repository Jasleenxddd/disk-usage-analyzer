import os
import argparse
import sys

def get_size(path):
    total_size = 0
    try:
        if os.path.isfile(path):
            return os.path.getsize(path)

        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.exists(file_path):
                    total_size += os.path.getsize(file_path)
    except PermissionError:
        return 0

    return total_size


def format_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"


def analyze_directory(path, top_n):
    if not os.path.exists(path):
        print("Error: Path does not exist.")
        sys.exit(1)

    if not os.path.isdir(path):
        print("Error: Provided path is not a directory.")
        sys.exit(1)

    items = []

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        size = get_size(item_path)
        items.append((item, size))

    items.sort(key=lambda x: x[1], reverse=True)

    print(f"\nTop {top_n} largest items in {path}:\n")
    for i, (name, size) in enumerate(items[:top_n], start=1):
        print(f"{i}. {name:<25} {format_size(size)}")


def main():
    parser = argparse.ArgumentParser(description="Analyze disk usage of a directory.")
    parser.add_argument("path", help="Directory path to analyze")
    parser.add_argument("--top", type=int, default=5, help="Number of top items to display")

    args = parser.parse_args()
    analyze_directory(args.path, args.top)


if __name__ == "__main__":
    main()
