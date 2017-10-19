import sys


def min_diff(alpha, beta):
    sorted_alpha = sorted(alpha)
    sorted_beta = sorted(beta)

    diff = sys.maxsize

    alpha_idx = 0
    beta_idx = 0

    while alpha_idx < len(sorted_alpha) and beta_idx < len(sorted_beta):
        tmp = abs(sorted_alpha[alpha_idx] - sorted_beta[beta_idx])

        if tmp < diff:
            diff = tmp

        if sorted_alpha[alpha_idx] > sorted_beta[beta_idx]:
            beta_idx += 1
        else:
            alpha_idx += 1

    return diff
