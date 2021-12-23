import numpy as np
from fracdiff import fdiff


def add_diff(_df, _d_num, _name):

    if len(_df) >= 12:
        _diff_ar = fdiff(_df[_name], n=_d_num, window=10, mode="valid")
        _paddings = len(_df) - len(_diff_ar)  # 差分后数据长度变短，需要在前面填充多少数据
        _diff = np.nan_to_num(np.concatenate((np.full(_paddings, 0), _diff_ar)), nan=0)  # 将所有nan替换为0
        _df[_name] = _diff
    else:
        _df[_name] = np.nan  # 数据行数不足12的填充为空数据

    return _df
