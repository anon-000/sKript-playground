import psutil
import time

max_bars_count = 10


def show_usage_stats():
    cpu_percentage = psutil.cpu_percent()
    mem_percentage = psutil.virtual_memory().percent

    cpu_usage_fraction = cpu_percentage/100
    mem_usage_fraction = mem_percentage/100

    cpu_bar_string = '▮' * int(cpu_usage_fraction * max_bars_count) + \
        '▯' * (max_bars_count - int(cpu_usage_fraction * max_bars_count))
    memory_bar_string = '▮' * int(mem_usage_fraction * max_bars_count) + \
        '▯' * (max_bars_count - int(mem_usage_fraction * max_bars_count))

    
    print(f"\r CPU Usage:    |{cpu_bar_string}| {cpu_percentage:.2f}%")
    print(f" Memory Usage: |{memory_bar_string}| {mem_percentage:.2f}%")
    # Move the cursor up by 2 lines to overwrite in the next iteration
    print("\033[F\033[F", end="")

    # print(f"\r CPU Usage: |{cpu_bar_string}|{cpu_percentage: .2f}% Memory Usage: |{memory_bar_string}| {mem_percentage: .2f}%", end="\r")
    # print(
    #     f" Memory Usage: |{memory_bar_string}| {mem_percentage: .2f}%", end="\r")


while True:
    show_usage_stats()
    time.sleep(0.5)
