def filter_number_from_string(a: str) -> str:
    n_s = "".join(list(filter(lambda x: x.isdigit() or x == ".", a)))
    f = float(n_s)
    s = f"{f:.4f}"
    return s
