该项目用来巡我可以蹭哪些课，需提供两个文件：

我的空闲时间段csv文件：`static/my_schedule.csv`，空闲时间段标1即可
* 选课总表文件：`static/complete_classes.xlsx`，从教务网站上直接下载

主程序：`src/run.py`

生成两个文件：

* `result_all.csv`: 包含所有列信息
* `result_part.csv`: 只包含指定列信息

设置选项：

1. 指定列信息设置在 `src/dump_as.py` 的 `simple_ids` 里面
2. 代表课程编号和时间安排的列索引设置在 `src/filter.py` 的 `ID_COL` 和 `TIME_COL` 里面
