def resolve_conflict(conflict):
    head = ''.join(conflict['head'])
    incoming = ''.join(conflict['incoming'])

    return (
        "# --- HEAD version ---\n" + head +
        "# --- Incoming version ---\n" + incoming
    )