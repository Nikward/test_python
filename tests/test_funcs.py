import pytest

from main import get_vis_russia, geo_logs
from main import get_unique_values, ids


@pytest.mark.parametrize('geo_logs, expected_res', [(geo_logs, 'Россия')])
def test_vis_russia(geo_logs, expected_res):
    res = get_vis_russia(geo_logs)
    for element in get_vis_russia(res):
        assert (list(element.values())[0][-1]) == expected_res


@pytest.mark.parametrize('ids, expected_res', [
    ({'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]}, [98, 35, 15, 213, 54, 119]),
    ({'user1': [213, 213, 888, 15, 213],
      'user2': [54, 54, 119, 90, 119],
      'user3': [213, 98, 98, 98]}, [98, 15, 213, 54, 119, 888, 90])
])
def test_inique_value(ids, expected_res):
    res = get_unique_values(ids)
    assert res == expected_res
