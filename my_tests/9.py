
from my_client import client

all_jobs = []
# 根据需要自动获取更多页面。
for job in client.fine_tuning.jobs.list(
    limit=20,
):
    # 在这里对 job 执行某些操作
    all_jobs.append(job)
print(all_jobs)