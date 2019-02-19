import schedule
import time
import scrawl
import os

def job():
  global job_count
  job_start_time = time.time()
  print('Running daily job %d' % job_count);
  scrawl.start_scrawling(firstTime=True) if job_count == 0 else scrawl.start_scrawling(sell=True)
  job_end_time = time.time();
  print('Job %d finishes in %d' % (job_count, job_end_time-job_start_time))
  job_count += 1

def job_rent():
  job_start_time = time.time()
  print('Running rent fetching job')
  scrawl.start_scrawling(rent=True)
  job_end_time = time.time();
  print('Job rent finishes in %d' % (job_end_time-job_start_time))

def job_house():
  job_start_time = time.time()
  print('Running house fetching job')
  scrawl.start_scrawling(house=True)
  job_end_time = time.time()
  print('Job house info finishes in %d' (job_end_time-job_start_time))

def job_sell():
  job_start_time = time.time()
  print('Running sell info fetching job')
  scrawl.start_scrawling(sell=True)
  job_end_time = time.time()
  print('Job sell info finishes in %d' (job_end_time-job_start_time))

if __name__ == "__main__":
  print('Starting...');
  schedule.every().day.do(job_sell).run();
  schedule.every().day.do(job_rent).run();
  schedule.every().day.do(job_house).run();
  while(True):
    schedule.run_pending();
    time.sleep(600);
