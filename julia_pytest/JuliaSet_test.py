import pytest

@pytest.mark.parametrize("desired_width,max_iterations", [(1000, 300), (1000, 1000), (10000, 300), (100, 100)])
def test_julia_set(desired_width, max_iterations):
    # In order to achieve this we returned the output variable.
    import JuliaSet as js
    output = js.calc_pure_python(desired_width, max_iterations)
    assert sum(output) == 33219980
