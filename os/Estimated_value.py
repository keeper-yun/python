# -*- coding: utf-8 -*-

import random
import threading

# 全局变量
inside_circle = 0
total_points = 0
lock = threading.Lock()

def generate_random_points(num_points):
    global inside_circle, total_points
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2
        if distance <= 1:
            with lock:
                inside_circle += 1
        with lock:
            total_points += 1

def calculate_pi(num_points):
    num_threads = 4  # 可以根据需要调整线程数
    points_per_thread = num_points // num_threads
    threads = []

    # 创建并启动线程
    for _ in range(num_threads):
        thread = threading.Thread(target=generate_random_points, args=(points_per_thread,))
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 计算π的估计值
    pi_estimate = 4 * inside_circle / total_points
    return pi_estimate

if __name__ == "__main__":
    num_points = 1000000  # 生成的随机点总数
    pi_value = calculate_pi(num_points)
    print(f"我计算的π的值为-->: {pi_value}")
