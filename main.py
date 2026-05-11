import re
from pathlib import Path

def swap(
        directory: str,
        suffix: str,
        find: str,
        replace: str,
        case_sensitive: bool = False
) -> dict[str, int]:
    
    directory = Path(directory)
    suffix = suffix if suffix.startswith('.') else f'.{suffix}'
    flags = re.IGNORECASE if case_sensitive else 0
    pattern = re.compile(re.escape(find), flags)

    changed = {}

    for filepath in sorted(directory.glob(f"*{suffix}")):
        original = filepath.read_text(encoding='utf-8')
        count = len(pattern.findall(original))
        if count:
            filepath.write_text(pattern.sub(replace, original), encoding='utf-8')
            changed[str(filepath)] = count

    return changed