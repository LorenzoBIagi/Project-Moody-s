import numpy as np
import math


# ================================================================
# STEP 1 – f(x) = p(x) * v_A(x) per un trinomial tree
# ================================================================
# Convenzioni:
#   x_k = 0 -> down (fattore d, prob pd)
#   x_k = 1 -> middle (fattore m, prob pm)
#   x_k = 2 -> up (fattore u, prob pu)
#
# f(x) = p(x) v_A(x) con:
#   S_k(x) = S0 * Π_{i=1}^k f(x_i)
#   avg_S(x) = (1/N) Σ_k S_k(x)
#   payoff v_A(x) = max(avg_S(x) - K, 0)
#   p(x) = Π_k p_{x_k}
# ================================================================

def path_to_weighted_payoff_trinomial(x_path, S0, K,
                                      u, m, d,
                                      pu, pm, pd):
    """
    x_path: lista/array di lunghezza N con valori in {0,1,2}
              0 = down (d), 1 = middle (m), 2 = up (u).

    Ritorna: p(x) * v_A(x), senza fattore di sconto e^{-rT}.
    """
    x = np.asarray(x_path, dtype=int) #giusto per settarlo bene
    N = x.size

    # fattori e probabilità per i 3 stati
    factors = np.array([d, m, u], dtype=float)   # state 0,1,2
    probs   = np.array([pd, pm, pu], dtype=float)

    # traiettoria del sottostante
    step_factors = factors[x]          # ti traduce x_k in una lista dei fattori
    S_path = S0 * np.cumprod(step_factors)
    avg_S = S_path.mean()

    payoff = max(avg_S - K, 0.0)

    # probabilità del cammino
    p_path = float(np.prod(probs[x]))

    return p_path * payoff


def make_f_trinomial(S0, K,
                     u, m, d,
                     pu, pm, pd,
                     N):
    """
    Restituisce un callable f(x_digits) = p(x) * v_A(x)
    sul dominio {0,1,2}^N.
    """
    def f(x_digits):
        return path_to_weighted_payoff_trinomial(
            x_digits, S0, K,
            u, m, d,
            pu, pm, pd
        )
    return f



