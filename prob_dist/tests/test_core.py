from discrete_pmf import binom_pmf

def test_binom_pmf_output():
    result = binom_pmf([0, 1, 2], n=2, p_list=[0.5], plot=False)
    assert isinstance(result, dict)
