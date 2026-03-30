# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License


def sparklines(temp_range_day):
    sparklines_graph = "▁▂▃▄▅▆▇█"
    mn, mx = min(temp_range_day), max(temp_range_day)

    if mx - mn == 0:
        return sparklines_graph[0]*len(temp_range_day)
    
    return "".join(sparklines_graph[int((x - mn) / (mx - mn) * (len(sparklines_graph) - 1))] for x in temp_range_day)

temps = [15.2, 14.8, 14.3, 13.9, 14.5, 16.0, 17.2, 18.0]
s=sparklines(temps)

print(s)


