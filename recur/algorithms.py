from functools import reduce


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


def make_change(amt, vals, idx=0):
    """Counts the number of possible change combinations.

    Args:
        amt (int): Amount to make change of.
        vals (list): Collection of values from which to make change.
        idx (int): Index of current value.

    Returns:
        (int): Number of ways to make change.
    """

    return _make_change(amt, vals, idx, dict())


def _seq_sum(seq):
    """Sums a given sequence.

    Args:
        seq (list): Collection of numeric values.

    Returns:
        (number): Sum of the sequence of numbers provided.
    """

    return reduce((lambda x, y: x + y), seq, 0)


def _find_combinations(amt, vals, idx, memo, seq=None):
    """Identifies possible combinations from provided values to equal given amount.

    Args:
        amt (int): Amount to make change of.
        vals (list): Collection of values from which to make change.
        idx (int): Index of current value.

    Returns:
        (None)
    """

    if seq is not None and amt - _seq_sum(seq) == 0:
        key = "+".join(str(v) for v in seq)

        if key not in memo:
            memo[key] = seq[0:]

        return

    if idx >= len(vals):
        return

    tmp = None

    if seq is None:
        tmp = []
    else:
        tmp = seq[0:]

    while amt - _seq_sum(tmp) >= 0:
        _find_combinations(amt, vals, idx + 1, memo, tmp)
        tmp.append(vals[idx])
        tmp = sorted(tmp)


def find_combinations(amt, vals, idx=0):
    """Identifies possible combinations from provided values to equal given amount.

    Args:
        amt (int): Amount to make change of.
        vals (list): Collection of values from which to make change.
        idx (int): Index of current value.

    Returns:
        (list): Collection of sequences that sum to given amount.
    """

    memo = dict()
    _find_combinations(amt, vals, idx, memo)

    return sorted(list(memo.values()), key=len)
