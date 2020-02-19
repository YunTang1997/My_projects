from datetime import datetime
from pandas.tseries.offsets import Hour, Minute, Day, MonthEnd
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# dates = [datetime(2011,1, 2), datetime(2011, 1, 5),
#          datetime(2011, 1, 7), datetime(2011, 1, 8),
#          datetime(2011, 1, 10), datetime(2011, 1, 12)]
#
# ts = pd.Series(np.random.randn(6), index=dates)
# print(ts)
# print(ts.index)
# print(ts[::2])  # 将ts中每隔一个的元素选择出
# print(ts + ts[::2])  # 不同索引的时间序列之间的算术运算在日期上自动对齐
# print(ts.index[0])
# resampler = ts.resample('D')  # 将原数据以“日”为单位重新采样

# long_ts = pd.Series(np.random.randn(1000),
#                     index=pd.date_range('1/1/2000', periods=1000))
# print(long_ts)
# print(long_ts['2001'])  # 输出2001年的所有数据
# print(long_ts['2001-05'])   # 输出2001年5月的所有数据
# print(ts[datetime(2011, 1, 7):])  # 使用datetime对象进行切片也可以
# print(ts.truncate(after='1/9/2011'))

# dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
# long_df = pd.DataFrame(np.random.randn(100, 4),
#                        index=dates,
#                        columns=['Colorado', 'Texas',
#                                 'New York', 'Ohio'])
# print(long_df.loc['5-2001'])


# dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
#                           '1/2/2000', '1/3/2000'])
# dup_ts = pd.Series(np.arange(5), index=dates)
# print(dup_ts)
# print(dup_ts.index.is_unique)  # 检查索引是否唯一

# grouped = dup_ts.groupby(level=0)
# print(grouped.first())  # 第一组
# print(grouped.median())  # 中间那组
# print(grouped.last())  # 最后一组
# print(grouped.mean())  # 将有相同时间戳的数据利用均值聚合
# print(grouped.count())  # 统计每个时间戳的数据个数

# index = pd.date_range('2012-04-01', '2012-06-01')
# print('给定起、止时间点： ')
# print(index)
# index = pd.date_range(start='2012-04-01', periods=20)
# print('\n给定起始时间点和范围： ')
# print(index)
# index = pd.date_range(end='2012-06-01', periods=20)
# print('\n给定终止时间点和范围： ')
# print(index)
# index = pd.date_range('2000-01-01', '2000-12-01', freq='BM')
# print('\n每月最后业务日期的时间索引： ')
# print(index)

# four_hour = Hour(4)  # 传递一个整数来定义偏置量的倍数
# print(four_hour)
# index = pd.date_range('2000-01-01', '2000-01-03 2359', freq='4h')  # 以4h小时为频率
# print(index)

# two_half = Hour(2) + Minute(30)  # 多个偏置可以通过加法进行联合
# print(two_half)
# index = pd.date_range('2000-01-01', periods=10, freq='1h30min')  # 以一个半小时为频率
# print(index)


# rng = pd.date_range('2012-01-01', '2012-09-01', freq='WOM-3FRI')  # 每月第三个星期五的日期
# # print(list(rng))

# print('\n---位移（向前和向后）日期---')
# ts = pd.Series(np.random.randn(4),
#                index=pd.date_range('1/1/2000', periods=4, freq='M'))
# print(ts.shift(2))  # 将序列数据向后平移两格，但会引入缺失值
# print(ts.shift(-2))  # 将序列数据前平移两格，但会引入缺失值
# h = ts / ts.shift(1) - 1  # 计算时间序列的百分比变化
# print(h)
# print('\n日期向后平移2个月： ')
# print(ts.shift(2, freq='M'))  # 加入频率指标，不会引入缺失值
# print('\n日期向后平移3天： ')
# print(ts.shift(3, freq='D'))
# print('\n日期向后平移90分钟： ')
# print(ts.shift(1, freq='90T'))

# now = datetime(2011, 11, 17)
# print(now + 3 * Day())
# print(now + MonthEnd())
# print(now + MonthEnd(2))
# offset = MonthEnd()
# print(offset.rollforward(now))  # 按照给定频率向前滚动
# print(offset.rollback(now))  # 按照给定频率向后滚动
# ts = pd.Series(np.random.randn(20),
#                index=pd.date_range('1/15/2000', periods=20, freq='4d'))
# print(ts)
# print(ts.groupby(offset.rollforward).mean())  # ts数据中每个月数据的均值
# print(ts.resample('M').mean())  # 同上

# print('\n---时区处理---')
# rng = pd.date_range('3/9/2012 9:30', periods=6, freq='D')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts.index.tz)  # 查看tz属性，是否是简单时区
# print(ts)
# ts_utc = ts.tz_localize('UTC')  # 简单时区转化为本地化时区
# ts_new = ts_utc.tz_convert('America/New_York')  # 当时间序列被本地化为某个特定的区时，可以转化为另一个时区
# print(ts_new)

# stamp = pd.Timestamp('2011-03-12 04:00')
# stamp_utc = stamp.tz_localize('utc')
# print(stamp_utc.tz_convert('Asia/Shanghai'))

# rng = pd.date_range('3/7/2012 9:30', periods=10, freq='B')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# ts1 = ts[:7].tz_localize('Europe/London')
# ts2 = ts1[2:].tz_convert('Europe/Moscow')
# result = ts1 + ts2
# print(result)
# print(result.index)

# print('\n---时间区间和区间算术---')
# p = pd.Period(2007, freq='A-DEC')
# print(p)
# print(p + 5)
# print(p - 2)
# print('\n注意rng与rng2输出的区别: ')
# rng = pd.period_range('2000-01-01', '2000-06-30', freq='M')
# print('rng: ')
# print(rng)
# rng2 = pd.date_range('2000-01-01', '2000-06-30', freq='M')
# print('rng2: ')
# print(rng2)

# values = ['2001Q3', '2002Q2', '2003Q1']  # 将字符串数组转化为PeriodIndex类
# # index = pd.PeriodIndex(values, freq='Q-DEC')
# # print(index)

# print(p.asfreq('M', how='start'))
# print(p.asfreq('M', how='end'))
#
# p1 = pd.Period('2007', freq='A-Jun')
# print(p1.asfreq('M', how='start'))
# print(p1.asfreq('M', how='end'))

# rng = pd.period_range('2006', '2009', freq='A-DEC')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts)
# ts1 = ts.asfreq('M', how='start')  # 年度区间将被替换为对应于每个年度区间的第一个月的月度区间
# print(ts1)
# ts2 = ts.asfreq('M', how='end')  # 年度区间将被替换为对应于每个年度区间的最后一个月的月度区间
# print(ts2)
# ts3 = ts.asfreq('B', how='end')  # 年度区间将被替换为对应于每年最后一个工作日
# print(ts3)

# p = pd.Period('2012Q4', freq='Q-JAN')
# print(p)
# print(p.asfreq('D', how='start'))
# print(p.asfreq('D', how='end'))
# p1 = pd.Period('2012Q3', freq='Q-JAN')
# print(p1.asfreq('D', how='start'))
# print(p1.asfreq('D', how='end'))
# p4pm = (p.asfreq('B', how='end') - 1).asfreq('T', how='start') + 16 * 60  # 获取在季度倒数第二个工作日下午4点的时间戳
# print(p4pm)

# rng = pd.period_range('2011Q3', '2012Q4', freq='Q-JAN')
# ts = pd.Series(np.arange(len(rng)), index=rng)
# print(ts)
#
# new_rng = (rng.asfreq('B', how='end')).asfreq('T', how='start') + 16 * 60
# ts.index = new_rng.to_timestamp()
# print(ts)

# rng = pd.date_range('2000-01-01', periods=3, freq='M')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# pts = ts.to_period()  # 将Series或DataFrame时间戳转化为区间
# print(pts)

# rng = pd.date_range('1/29/2000', periods=6, freq='D')
# ts2 = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts2.to_period('M'))
# print((ts2.to_period()).to_timestamp(how='end'))

# print('\n---重新采样与频率转换---')
# rng = pd.date_range('2000-01-01', periods=100, freq='D')
# ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print(ts.resample('M').mean())  # 对每月求平均
# print(ts.resample('M', kind='period').mean())

# rng = pd.date_range('2000-01-01', periods=12, freq='T')
# ts = pd.Series(np.arange(12), index=rng)
# print(ts)
# print(ts.resample('5min', closed='left').sum())  # 默认情况下左箱体是包含的
# print(ts.resample('5min', label='right').sum())  # 使用label='right'可以使用右箱体边界标记时间序列
# print(ts.resample('5min', label='right', loffset='-1s').sum())

# ts_new = ts.resample('5min', label='right').sum()
# print(ts_new.shift(-1, freq='S'))  # 与上一行代码效果相同
# print(ts.resample('5min').ohlc())  # 得到开端、峰值、谷值与结束值
# print(ts.resample('5min', closed='right').sum())

# frame = pd.DataFrame(np.random.randn(2, 4),
#                      index=pd.date_range('1/1/2000', periods=2, freq='W-WED'),
#                      columns=['Colorado', 'Texas', 'New York', 'Ohio'])
# print(frame)
# df_daily = frame.resample('D').asfreq()
# print('\n')
# print(df_daily)
# print('\n')
# print(frame.resample('D').ffill())
# print('\n')
# print(frame.resample('D').ffill(limit=2))
# print('\n')
# print(frame.resample('W-THU').ffill())

# print(os.getcwd())  # 得到当前工作环境目录

print('\n---移动窗口函数---')
close_px_all = pd.read_csv('../基础练习/stock_px_2.csv',
                           parse_dates=True, index_col=0)
# print(close_px_all)
close_px = close_px_all[['AAPL', 'MSFT', 'XOM']]  # 读取文档对应的几列

close_px1 = close_px_all.loc[:, ['AAPL', 'MSFT', 'XOM']]
# print(close_px1)

close_px = close_px.resample('B').ffill()
# print(close_px)
# close_px.AAPL.plot()
# close_px.AAPL.rolling(250).mean().plot(figsize=(15, 8))

appl_std250 = close_px.AAPL.rolling(250, min_periods=10).std()
# print(appl_std250[5:12])
# appl_std250.plot()
# expanding_mean = close_px.AAPL.expanding().mean())
# close_px.rolling(60).mean().plot(logy=True)

# aapl_px = close_px.AAPL['2006':'2007']
# ma60 = aapl_px.rolling(window=30, min_periods=20).mean()
#
# ewma60 = aapl_px.ewm(span=30).mean()
# ma60.plot(style='k--', label='Simple MA')
# ewma60.plot(style='r-', label='EW MA')  # 指数加权函数
# plt.legend()  # 显示图例

spx_px = close_px_all['SPX']
spx_rets = spx_px.pct_change()
returns = close_px.pct_change()
# corr = returns.AAPL.rolling(window=125, min_periods=100).corr(spx_rets)  # 相关系数图
# corr.plot()
corr = returns.rolling(window=125, min_periods=100).corr(spx_rets)
corr.plot()

plt.show()  # 图像才能显示出来