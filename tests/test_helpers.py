import builtins
import or78_helpers


def test_input_yes_no_variants(monkeypatch):
    inputs = iter(['y', 'Y', 'Yes', 'n', 'N'])
    results = []
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    results.append(or78_helpers.input_yes_no('prompt'))  # 'y'
    results.append(or78_helpers.input_yes_no('prompt'))  # 'Y'
    results.append(or78_helpers.input_yes_no('prompt'))  # 'Yes'
    results.append(or78_helpers.input_yes_no('prompt'))  # 'n'
    results.append(or78_helpers.input_yes_no('prompt'))  # 'N'
    assert results == [True, True, True, False, False]
