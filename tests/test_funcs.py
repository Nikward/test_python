import pytest

from main import get_vis_russia, geo_logs
from main import get_unique_values
from main import name_chanel_max


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


@pytest.mark.parametrize('stats, expected_res', [
    ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
    ({'facebook': 88, 'yandex': 169, 'vk': 115, 'google': 100, 'email': 42, 'ok': 543}, "ok"),
    ({'facebook': 600, 'yandex': 344, 'vk': 115, 'google': 100, 'email': 42, 'ok': 543}, "facebook"),
    ({'facebook': 88, 'yandex': 169, 'vk': 700, 'google': 100, 'email': 42, 'ok': 543}, "vk")
])
def test_max_chanell(stats, expected_res):
    res = name_chanel_max(stats)
    assert expected_res == res
