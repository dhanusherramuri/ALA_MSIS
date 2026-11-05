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

#### ALGORITHM 6 : LAYER_NORM ####

def layer_norm(e, gamma, beta, eps = 0.0):

     """
    Input : e in R^{d_e} (or R^{d_e x l}: each column normalised independently)
            gamma, beta in R^{d_e}
    Output: e_hat in same shape as e
    eps = 0 reproduces the paper exactly; GPT-2's released code uses eps = 1e-5.
    """
     
     e = np.asarray(e, dtype = np.float64)
     d_e = e.shape[0]
     m = np.sum(e, axis = 0, keepdims = True) / d_e
     v = np.sum((e - m) ** 2, axis = 0, keepdims = True) / d_e
     g = gamma.reshape((-1,) + (1,) * (e.ndim - 1))
     b = beta.reshape((-1,) + (1,) * (e.ndim - 1))
     return ( e - m ) / np.sqrt(v + eps) * g + b

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

    #Algorithm 6
    e = rng.normal(3.0, 5.0, D_E)
    out = layer_norm(e, np.ones(D_E), np.zeros(D_E))
    assert abs(out.mean()) < 1e-10 and abs(out.var() - 1) < 1e-10
    g, b = rng.normal(size=D_E), rng.normal(size=D_E)
    Em = rng.normal(size=(D_E, 5))
    cols = np.stack([layer_norm(Em[:, i], g, b) for i in range(5)], axis=1)
    assert np.allclose(layer_norm(Em, g, b), cols)

    print("TEST PASSED!!")