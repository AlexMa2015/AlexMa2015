import multiprocessing
import time
import math


# 定义计算阶乘的函数
def compute_factorial(n):
    return math.factorial(n)


# 定义任务处理函数
def process_task(numbers):
    results = []
    for num in numbers:
        result = compute_factorial(num)
        results.append(result)
    return results


if __name__ == "__main__":
    # 示例数据：要计算的数字列表
    numbers = [100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000]

    # 获取 CPU 核心数
    num_cores = multiprocessing.cpu_count()
    print(f"CPU 核心数: {num_cores}")

    # 记录串行执行时间
    start_time = time.time()
    process_task(numbers)
    print(f"串行执行时间: {time.time() - start_time:.2f} 秒")

    # 使用 multiprocessing 加速
    start_time = time.time()

    # 创建进程池，指定核心数
    with multiprocessing.Pool(processes=num_cores) as pool:
        # 将任务分成多个子任务，并行处理
        results = pool.map(compute_factorial, numbers)

    print(f"并行执行时间: {time.time() - start_time:.2f} 秒")
