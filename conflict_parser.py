def parse_conflict(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    inside_conflict = False
    current = {'head': [], 'incoming': []}
    conflicts = []
    stage = None

    for line in lines:
        if line.startswith("<<<<<<<"):
            inside_conflict = True
            stage = 'head'
        elif line.startswith("======="):
            stage = 'incoming'
        elif line.startswith(">>>>>>>"):
            inside_conflict = False
            conflicts.append(current.copy())
            current = {'head': [], 'incoming': []}
        elif inside_conflict:
            current[stage].append(line)

    return conflicts