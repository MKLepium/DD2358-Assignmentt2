import pytest

def test_dgemm_numpy():
    import Exercise4
    res_numpy = Exercise4.dgemm_numpy(200)
    assert all([res_numpy[0][0] == res_numpy[i][j] for i in range(100) for j in range(100)])
    

def test_dgemm_list():
    import Exercise4
    res_list = Exercise4.dgemm_list(200)
    for element in res_list:
        for sub_element in element:
            assert sub_element == 200.0
    


def test_dgemm_array():
    import Exercise4
    res_array = Exercise4.dgemm_array(200)
    for element in res_array:
        assert element == 200.0


