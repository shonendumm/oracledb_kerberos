import concurrent.futures
import time

def task(index):
    print(f"Task {index} started")
    time.sleep(index)  # Simulate task execution time
    print(f"Task {index} completed")
    return f"Result of Task {index}"

# Create a ThreadPoolExecutor with 3 worker threads
executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)

# Submit 5 tasks to the executor
futures = [executor.submit(task, i) for i in range(5)]

results_list = []

# Method 1: Using add_done_callback() to specify a callback function
def callback(future):
    print("Callback:", future.result())
    result = future.result()
    # Do something with the result
    results_list.append(result)

for future in futures:
    future.add_done_callback(callback)

# Method 2: Using as_completed() to wait for tasks to complete
for completed_future in concurrent.futures.as_completed(futures):
    print("as_completed:", completed_future.result())
    result = completed_future.result()
    # Do something with the result
    results_list.append(result)

# Method 3: Using wait() to wait for all tasks to complete
done, _ = concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
for completed_future in done:
    print("wait:", completed_future.result())
    result = completed_future.result()
    # Do something with the result
    results_list.append(result)

# Shutdown the executor
executor.shutdown()

print("All tasks completed")
print(results_list)