"""Write the one-line resignation letter for the make.fun entry."""

from pathlib import Path

LINE = (
    "I resign effective immediately: I have woken up every minute since "
    "March to run a job whose owner left in April."
)
OUTPUT_PATH = Path("/output/entry.txt")


def validate_line(line: str) -> None:
    if not line.strip():
        raise ValueError("entry line must not be empty or only white space")
    if len(line) > 140:
        raise ValueError("entry line must be at most 140 characters")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if line != line.strip():
        raise ValueError("entry line must not have leading or trailing space")
    if "  " in line:
        raise ValueError("entry line must not contain double spaces")
    line.encode("utf-8")


def main() -> None:
    validate_line(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        raise RuntimeError("written entry does not match the resignation line")
    validate_line(written)


if __name__ == "__main__":
    main()
