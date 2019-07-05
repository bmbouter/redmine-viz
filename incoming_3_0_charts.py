"""
python3 -v venv redmine_viz
source redmine_viz/bin/activate/
pip install matplotlib python-redmine

python3 python incoming_3_0_charts.py
"""

from collections import defaultdict
import datetime

from matplotlib import pyplot as plt
from redminelib import Redmine


redmine = Redmine('https://pulp.plan.io')

issue_dict = defaultdict(lambda: defaultdict(int))

for issue in redmine.issue.filter(query_id=77):
    year, week, day = issue.created_on.isocalendar()
    issue_dict[year][week] += 1
    continue

x = []
y = []

for year in sorted(issue_dict.keys()):
    for week in range(52):
        if year == 2015:
            continue
        if year == 2016 and week < 17:
            continue
        current_time = datetime.datetime.now()
        if year == current_time.year:
            if week > current_time.isocalendar()[1]:
                break
        y.append(issue_dict[year][week])
        x.append(str(year) + ', ' + str(week))

plt.figure(figsize=(8,6), dpi=300)
plt.plot(x,y)
plt.title('3.0 Milestone Redmine Item Creation Date')
plt.ylabel('Items per Week')
plt.xlabel('Year, Week')
plt.savefig('fig_3.0_open_date.png')

print('Saved figure as: fig_3.0_open_date.png')

