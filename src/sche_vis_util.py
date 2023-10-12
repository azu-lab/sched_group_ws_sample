import json


class ScheVisObj:
    def __init__(self, task_idx: int, start_time: int, finish_time: int, core_idx: int=0, job_idx: int=0, release_time: int=0):
        self._task_idx = task_idx
        self._start_time = start_time
        self._finish_time = finish_time
        self._core_idx = core_idx
        self._job_idx = job_idx
        self._release_time = release_time

    @property
    def task_idx(self) -> int:
        return self._task_idx

    @property
    def start_time(self) -> int:
        return self._start_time

    @property
    def finish_time(self) -> int:
        return self._finish_time

    @property
    def core_idx(self) -> int:
        return self._core_idx

    @property
    def job_idx(self) -> int:
        return self._job_idx

    @property
    def release_time(self) -> int:
        return self._release_time


class SchedulingVisualizerUtil:
    @staticmethod
    def save(objs: list[ScheVisObj], scheduling_length: int | None=None, filename: str='output') -> str:
        json_dict = {
            'makespan': scheduling_length or max([obj.finish_time for obj in objs]),
            'taskSet':[]
        }

        for obj in objs:
            json_dict['taskSet'].append({
                'coreID': obj.core_idx,
                'taskID': obj.task_idx,
                'jobID': obj.job_idx,
                'releaseTime': obj.release_time,
                'startTime': obj.start_time,
                'finishTime': obj.finish_time
            })

        filepath: str = './output/'+filename+'.json'
        file = open(filepath, 'w+')
        json.dump(json_dict, file)
        file.close()

        return filepath

    @staticmethod
    def save_from_array(task_idxs: list[int], start_times: list[int], finish_times: list[int], core_idxs: list[int] | None=None, job_idxs: list[int] | None=None, release_times: list[int] | None=None,
                        scheduling_length: int | None=None, filename: str='output') -> str:
        if core_idxs is None:
            core_idxs = [0 for _ in range(len(task_idxs))]
        if job_idxs is None:
            job_idxs = [0 for _ in range(len(task_idxs))]
        if release_times is None:
            release_times = [0 for _ in range(len(task_idxs))]

        json_dict = {
            'makespan': scheduling_length or max([f for f in finish_times]),
            'taskSet':[]
        }

        for task_idx, start_time, finish_time, core_idx, job_idx, release_time in zip(task_idxs, start_times, finish_times, core_idxs, job_idxs, release_times):
            json_dict['taskSet'].append({
                'coreID': core_idx,
                'taskID': task_idx,
                'jobID': job_idx,
                'releaseTime': release_time,
                'startTime': start_time,
                'finishTime': finish_time
            })

        filepath: str = './output/'+filename+'.json'
        file = open(filepath, 'w+')
        json.dump(json_dict, file)
        file.close()

        return filepath
