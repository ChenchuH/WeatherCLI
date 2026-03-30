# Copyright (c) 2026 Chenchu Hemanth Yakasiri Saravanan
# Licensed under the MIT License

def sparklines(temp_range_day):
    sparklines_graph = "▁▂▃▄▅▆▇█"
    mn, mx = min(temp_range_day), max(temp_range_day)

    if mx - mn == 0:
        return sparklines_graph[0]*len(temp_range_day)
    
    return "".join(sparklines_graph[int((x - mn) / (mx - mn) * (len(sparklines_graph) - 1))] for x in temp_range_day)



