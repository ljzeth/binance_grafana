import os

_ = os.path.abspath(os.path.dirname(__file__))  # 返回当前文件路径


root_path = os.path.abspath(os.path.join(_, '..'))  # 返回根目录文件夹

LOG_SAVE_DIR = os.path.join(_, 'log')
# 币安api设置

Wechat_Config = {
    'corpsecret':'FoJsxkyVOs',
    'agentid': 100,
    'corpid':'ww73'
}

INITIAL_CASH = {'psy_ns1': 100}

API_DICT = {

    # 最好使用策略名字 尽量不要使用特殊字符

    'psy_ns1':
        {
            'apiKey': '77ltPUEK',
            'secret': 'sIVTb7aG',
        },
    'BC_12H':
        {
            'apiKey': 'mFGrY4w25',
            'secret': 'cFRuGKXu9T2',
        },
    'RCCG_12H':
        {
            'apiKey': 'y2HFYE5gwoD',
            'secret': 'dgZfDTY6IE',
        },
    'psy_cta@163.com':
        {
            'apiKey': 'BCCi3fgGx',
            'secret': 'bu9Upg0VG',
        },
    'BCCG_12H':
        {
            'apiKey': 'mcbJTXfp',
            'secret': 'S2WmKGt',
        },

}
# 配置数据库

database_config = {
    'user': '',
    'passwd': '',
    'database': ''  #database 命名为ns_data
}

