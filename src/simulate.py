from src.dag_rd_gen import RDG_DAG

# to sample
from sample_scheduler.dag import Dag, Node
from sample_scheduler.scheduler import Scheduler

def simulate(dag: RDG_DAG):
    # implement each method here

    # the following is a sample
    dag_scheduling = Dag(dag.wcets, dag.edges)
    scheduler = Scheduler(5)
    scheduled_nodes: list[Node] = scheduler.schedule_dag(dag_scheduling)

    # return evaluated value
    # in sample, response time of DAG (maximum finish time of all nodes)
    return max([n.finish_time for n in scheduled_nodes])

def prepare_method(dag: RDG_DAG) -> tuple[bool,]:
    # return True when proposed method lose

    # the following is a sample
    dag_scheduling = Dag(dag.wcets, dag.edges)
    scheduler = Scheduler(5)
    scheduled_nodes: list[Node] = scheduler.schedule_dag(dag_scheduling)

    # return True when proposed method lose
    # if you want, another object can return
    wcrt = max([n.finish_time for n in scheduled_nodes])
    return wcrt > 200, wcrt, 200





def simulate_taskset(dags: list[RDG_DAG]):
    loop_len = len(dags)
    results: list = []

    for idx, dag in enumerate(dags):
        results.append(simulate(dag))
        print("\r" + f'{idx+1} / {loop_len} : {100*(idx+1)/loop_len:.0f}%', end="")
    print()

    return results

def prepare_method_taskset(dags: list[RDG_DAG]):
    loop_len = len(dags)
    results: list[dict] = []

    for idx, dag in enumerate(dags):
        result = prepare_method(dag)
        lose = result[0]
        if len(result) > 1:
            opt = result[1:]
        else:
            opt = None

        if lose:
            results.append({'dag': dag, 'optional': opt})
        print("\r" + f'{idx+1} / {loop_len} : {100*(idx+1)/loop_len:.0f}%', end="")
    print()

    return results
