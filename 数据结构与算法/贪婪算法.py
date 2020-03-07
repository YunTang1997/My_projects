"""
假设你办了个广播节目，要让全美50个州的听众都收听得到，为此，
你需要决定在哪些广播台播出，出于预算，你要力图在尽可能少的
广播台播出，现在广播台名单和其覆盖位置如下：
{'KONE': ID,NV,UT}{'KTWO': WA,ID,MT},{KTHREE : OR,NV,CA}
{KFOUR : NV,UT},{KFIVE : CA, AZ}
"""

# 需要覆盖的州
states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

# 广播台清单
stations = dict()
stations['KONE'] = set(['id', 'nv', 'ut'])
stations['KTWO'] = set(['wa', 'id', 'mt'])
stations['KTHREE'] = set(['or', 'nv', 'ca'])
stations['KFOUR'] = set(['nv', 'ut'])
stations['KFIVE'] = set(['ca', 'az'])

# 最终使用的广播台
final_station = set()

while states_needed:  # 当还有需要覆盖的州未被覆盖的时候循环
    best_station = None  # 覆盖了最多未覆盖的州的广播台
    states_covered = set()  # 已经覆盖了的州的集合
    for station, states in stations.items():
        # 计算需要覆盖的州和每个广播台覆盖的州的交集
        covered = states_needed & states
        # 如果交集的州数量比已经覆盖的州数量多
        if len(covered) > len(states_covered):
            best_station = station  # 最佳广播台更新为这个广播台
            states_covered = covered  # 已覆盖的州更新为交集
    states_needed = states_needed - states_covered  # 更新为覆盖的州
    final_station.add(best_station)  # 更新最终结果


print(final_station)
