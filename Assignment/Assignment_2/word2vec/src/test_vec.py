from w2v import Vec

def test_sim_diff_words():




if __name__ == "__main__":
    # w2v_model_path = "../glove50/glove_50_fast.wordvectors"
    # model = load_model(w2v_model_path)
    # assert model is not None, "Model Loading failed"
    test_sim_diff_words(model)
    tssw(model)
    tip(model)
    tms(model, "internship")
    norm_word(model,"tech")