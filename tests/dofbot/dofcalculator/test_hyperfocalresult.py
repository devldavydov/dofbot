from dofbot.dofcalculator.hyperfocalresult import HyperFocalResult


def test_hyperfocalresult_str():
    hf = HyperFocalResult(24, 3.5, 3.45)
    assert 'HyperFocal(FL=24 FN=3.5) [3.45]' == str(hf)
