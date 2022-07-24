# 並列処理用関数
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Generator, Callable

from tqdm import tqdm


def parallel_processor(
    total_file_num: int, n_jobs: int,
    files: Generator, process_function: Callable,
    max_file_num_per_process: int, process_result: Callable,
    *args, **kwargs,
):
    """paralell processor for big data.

    Args:
        total_file_num (int): total num of the files for process.
        n_jobs (int): num of the cpu you want to use.
        files (Generator): file generator you want to process. like List, pathlib.glob, etc.
        process_function (Callable): function for process for your one file.
        max_file_num_per_process (int): the limit for the files to process at once.
        process_result (Callable): function for process the results of your job.
    """
    pbar = tqdm(total=total_file_num)
    with ProcessPoolExecutor(n_jobs) as executor:
        jobs = {}
        while total_file_num:
            for _file in files:
                job = executor.submit(
                    process_function,
                    _file,
                    *args, **kwargs,
                )
                jobs[job] = _file
                if len(jobs) > max_file_num_per_process:
                    break

            for job in as_completed(jobs):
                total_file_num -= 1
                process_result(job)
                del jobs[job]
                pbar.update(1)
                break
