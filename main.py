import os
from ai_helper import ai_resolve

from conflict_parser import parse_conflict
from resolver import resolve_conflict
# from ai_helper import ai_resolve  # Optional

if __name__ == "__main__":
    file_path = input("Enter the path to conflicted file: ")
    conflicts = parse_conflict(file_path)

    for i, conflict in enumerate(conflicts):
        print(f"\n--- Conflict #{i + 1} ---")
        resolution = resolve_conflict(conflict)
        print(resolution)
        
        # If using AI:
        ai_result = ai_resolve(''.join(conflict['head']), ''.join(conflict['incoming']))
        print("AI Suggested Merge:\n", ai_result)