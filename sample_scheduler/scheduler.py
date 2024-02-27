# NOTE: NOT refactored

from .dag import Dag, Node

class Scheduler:
    def __init__(self, core_num: int):
        self._core_num = core_num
        pass

    def schedule_dag(self, dag: Dag) -> list[Node]:
        unscheduled_tasks: list[Node] = [n for n in dag.nodes]
        wait_tasks: list[Node] = []
        scheduling_task_dict: dict[int, Node] = {c: None for c in range(self.core_num)}
        scheduled_tasks: list[Node] = []
        time = 0

        while(len(unscheduled_tasks) != 0 or len(wait_tasks) != 0 or len([v for v in scheduling_task_dict.values() if v is not None]) != 0):
            for core, task in scheduling_task_dict.items():
                if task is not None and time >= task.finish_time:
                    scheduled_tasks.append(task)
                    scheduling_task_dict[core] = None

            ### ===== difference ===== ###

            # if idx set of scheduled task include prev of task, enque wait queue and remove unscheduled list
            # finish: {0, 1, 2}, prev: {0, 1} -> append
            for task in unscheduled_tasks:
                if set([n.idx for n in scheduled_tasks]) >= task.prev:
                    wait_tasks.append(task)
            for task in wait_tasks:
                if task in unscheduled_tasks:
                    unscheduled_tasks.remove(task)

            ### ===== difference ===== ###

            wait_tasks.sort(key=lambda x: x.release_time)

            for core in scheduling_task_dict.keys():
                if scheduling_task_dict[core] is None and len(wait_tasks) > 0:
                    new_scheduling_task = wait_tasks.pop(0)
                    new_scheduling_task.start_time = time
                    new_scheduling_task.finish_time = time + new_scheduling_task.wcet
                    new_scheduling_task.core = core
                    scheduling_task_dict[core] = new_scheduling_task

            # step forward
            time += 1

        return scheduled_tasks

    @property
    def core_num(self) -> int:
        return self._core_num