import schedule
import time
import scrawl
import os

def job():
  global job_count
  job_start_time = time.time()
  print('Running daily job %d' % job_count);
  scrawl.start_scrawling(firstTime=True) if job_count == 0 else scrawl.start_scrawling()
  job_end_time = time.time();
  print('Job %d finishes in %d' % (job_count, job_end_time-job_start_time))
  job_count += 1

if __name__ == "__main__":
  print('Starting...');
  job_count = 0
  schedule.every().day.do(job);