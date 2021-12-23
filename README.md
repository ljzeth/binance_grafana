# binance_grafana

## 更新

12月9日 21.00更新.

1. 更新了账户资金面板(出入金的记录已实现,收益率不受影响)
2. python代码2.0(在config中需要填写initial_cash的参数)

截图:

使用新的账户资金面板，需要部署2.0的代码，其他面板不受影响。

所有盈亏已经计算了充值和提现。

![%E8%B4%A6%E6%88%B7%E5%87%BA%E5%85%A5%E9%87%91.jpeg](https://bbs.quantclass.cn/api/storage/attachments/43639?t=cfee0c98vGxCe5ltXUye2vE220211209205108 "43639")

---

12月2日 23.00更新，上传了总体资金面板

该面板有两个图表需要手工配置(总体未实现盈亏和总体资金曲线)

![%E7%BC%96%E8%BE%91%E6%9D%BF.jpeg](https://bbs.quantclass.cn/storage/attachments/2021/12/02/cQALCF2ZoDgZP16v9W0l1qqcK35NJXc3zkrZ8all_thumb.jpeg "42551")

点击 `Edit`进入编辑页面

![sql%E8%AF%AD%E5%8F%A5%E9%A1%B5%E9%9D%A2.jpeg](https://bbs.quantclass.cn/storage/attachments/2021/12/02/JBfoMbZsVZNbsCTK02pGeCLls8hv4yoEsKiEWsY9_thumb.jpeg "42552")

`From`那里改成自己表的名字，有多少个账户就加多少个query,分别填写自己的表的名字。

例子：xxx_position

总体资金曲线也是一致

表的名字例子: xxx_equity

---

11月29 16.00更新 ：重新上传了代码。(忘记删除微信配置了，通知已经爆了)

## 简述

适用于币安u本位的监控，功能设计是按照中性策略的监控需求出发。granfa从今年年初开始用的，里面的花活基本玩明白了。最近从头到尾升级了一次。

## 主要功能

我是从个人最主要的三个需求出发。

- 验证实盘曲线与回测的一致性。因为中性每小时交易一次，资金账户的记录是在每小时的3分钟，保证单子全部成交(资金量大的老板可以推后这个时间)。这样理论上就可以回测曲线完全一致。
- 实时查看盈亏。因此仓位的更新是每60s一次，随时随地可以知道账户的情况。
- 实盘运维。保证代码不会挂掉，在下单分析的面板中，可以查看最近一小时的下单情况和明细，不仅可以确保程序一直运行，也可以观察到下单是否有异常情况。

## 部分截图

![%E8%B5%84%E9%87%91%E8%B4%A6%E6%88%B7%E9%9D%A2%E6%9D%BF.jpeg](https://bbs.quantclass.cn/storage/attachments/2021/11/29/fHxT9QjuV8xhjwek9oP679wipD5OTdR9ZlWkRFfa_thumb.jpeg "42153")

---

![%E5%AE%9E%E6%97%B6%E6%8C%81%E4%BB%93%E9%9D%A2%E6%9D%BF.jpeg](https://bbs.quantclass.cn/storage/attachments/2021/11/29/BcoZcizxcetWofCeuqx2bAFcCBwSYL33INdY8VCL_thumb.jpeg "42154")

---

![%E4%B8%8B%E5%8D%95%E5%88%86%E6%9E%90%E9%9D%A2%E6%9D%BF.jpeg](https://bbs.quantclass.cn/storage/attachments/2021/11/29/ajzgyr11C4kcKYozpF1nbrhuCgZa7XENAv808QFx_thumb.jpeg "42155")

---

![%E5%8E%86%E5%8F%B2%E6%95%B0%E6%8D%AE%E9%9D%A2%E6%9D%BF.jpeg](https://bbs.quantclass.cn/storage/attachments/2021/11/29/OFyjB22nVjmY4xrBaRTIruWY7LDTCiQO5XdEkQPn_thumb.jpeg "42156")

---

## 部署建议

- 长期使用Grafana的老板，可以导入面板后，自行根据自己的数据库的字段进行图表的采用或者修改。
- 对Grafana了解不多的老板，可在现有数据下创建新的数据库，运行python文件，导入面板后即可使用。

## 具体步骤

1. 在服务器安装grafana(v8.0.5)和mysql(5.7)((数据库需自行创建,建议数据库名字`ns_data`)的过程我就不再赘述,具体版本影响不大。
2. 把`config.py`中配置好账户API((建议单独申请只读的api))以及数据库，并运行`supervsior.py`文件，其中有2个与交易所交互的库需要安装。

- `pip install unicorn-binance-websocket-api --upgrade`
- `pip install python-binance`

3. 把json文件导入Grafana即可。有一个图表使用了第三方插件，需要安装后重启。

- `grafana-cli plugins install grafana-piechart-panel`

## 具体使用

1. 使用前需要在Grafana正确配置数据库。可参考论坛帖子。
2. 每个页面基于一个账户，需要切换时在左上角切换。
3. 不用修改任何面板的query，会自动识别表的名字

## 注意事项

1. 下单面板，要在程序运行，第一次下单后，order表才会被创建并写入数据。
