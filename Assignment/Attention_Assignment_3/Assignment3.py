import numpy as np


L_MAX = 1024     # maximum sequence length
D_E = 768        # model width
N_LAYERS = 12    # L
N_HEADS = 12     # H
D_MLP = 3072
N_V = 50257      # vocabulary size
D_ATTN = D_E // N_HEADS   # 64 = d_attn = d_mid (per head)
D_MID = D_ATTN
D_OUT = D_E               # output width of MHAttention (Alg. 5)


#### ALGORITHM 1  : TOKEN EMBEDDING ###

def token_embedding(v, We):
    """
    Input : v  token ID (int, 0-indexed), or an integer array of IDs
            We in R^{d_e x N_V}, token embedding matrix
    Output: e  in R^{d_e}  (or R^{d_e x len(v)} if v is an array)
    """

    return We[:, v]

### TESTS #####

if __name__ == "__main__":
    rng = np.random.default_rng(0)

    # HYPERPARAMETER CONSISTENCY
    assert N_HEADS * D_MID == D_E and D_ATTN == 64

    # Algorithm 1
    We = rng.normal(0,00.2, (D_E, N_V))
    assert token_embedding(464, We).shape == (D_E,)
    assert np.allclose(token_embedding(464,We), We[:,464])
    assert token_embedding(np.array([1,2,3]), We).shape == (D_E, 3)

    print("TEST PASSED!!")