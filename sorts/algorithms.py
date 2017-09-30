def _partition(seq, begin, end, pivot):
    left = begin
    right = end

    while left <= right:

        while seq[left] < pivot:
            left += 1

        while pivot < seq[right]:
            right -= 1

        if left <= right:
            tmp = seq[left]
            seq[left] = seq[right]
            seq[right] = tmp

            left += 1
            right -= 1

    return left


def _quicksort(seq, begin, end):
    if begin >= end:
        return

    pivot = seq[(begin + end) // 2]
    idx = _partition(seq, begin, end, pivot)

    _quicksort(seq, begin, idx - 1)
    _quicksort(seq, idx, end)


def quicksort(seq):
    end = len(seq)
    _quicksort(seq, 0, end - 1)


def _merge(seq, tmp, begin, mid, end):
    left = begin
    left_end = mid
    right = mid + 1
    right_end = end
    tmp_idx = begin

    while left <= left_end and right <= right_end:
        if seq[left] < seq[right]:
            tmp[tmp_idx] = seq[left]
            left += 1
        else:
            tmp[tmp_idx] = seq[right]
            right += 1

        tmp_idx += 1

    left_rem = left_end - left + 1
    right_rem = right_end - right + 1

    if left_rem >= 1:
        tmp[tmp_idx:tmp_idx + left_rem] = seq[left:left_end + 1]

    if right_rem >= 1:
        tmp[tmp_idx:tmp_idx + right_rem] = seq[right:right_end + 1]

    seq[begin:end + 1] = tmp[begin:end + 1]


def _mergesort(seq, tmp, begin, end):
    if begin >= end:
        return

    mid = (begin + end) // 2
    _mergesort(seq, tmp, begin, mid)
    _mergesort(seq, tmp, mid + 1, end)
    _merge(seq, tmp, begin, mid, end)


def mergesort(seq):
    end = len(seq)
    _mergesort(seq, [None for _ in range(end)], 0, end - 1)
