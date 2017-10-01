def _make_change(amt, vals, idx, ledger):
    """Counts the number of possible change combinations.

    Args:
        amt (int): Amount to make change of.
        vals (list): Collection of values from which to make change.
        idx (int): Index of current value.
        ledger (dict): Dictionary of counts of ways based on remainder amount and value.

    Returns:
        (int): Number of ways to make change.
    """

    if amt == 0:
        return 1

    if idx >= len(vals):
        return 0

    key = "{amt}-{idx}".format(amt=amt, idx=idx)

    if key in ledger:
        return ledger[key]

    rem = amt
    ways = 0

    while rem >= 0:
        ways += _make_change(rem, vals, idx + 1, ledger)
        rem -= vals[idx]

    ledger[key] = ways

    return ways


def make_change(amt, vals, idx):
    """Counts the number of possible change combinations.

    Args:
        amt (int): Amount to make change of.
        vals (list): Collection of values from which to make change.
        idx (int): Index of current value.

    Returns:
        (int): Number of ways to make change.
    """

    return _make_change(amt, vals, idx, dict())
