from src.dag_rd_gen import RDG_DAG

# to sample
from sample_scheduler.dag import Dag, Node
from sample_scheduler.scheduler import Scheduler

def simulate(dag: RDG_DAG, **kwargs):
    # implement each method here

    # the following is a sample
    dag_scheduling = Dag(dag.wcets, dag.edges)
    scheduler = Scheduler(5)
    scheduled_nodes: list[Node] = scheduler.schedule_dag(dag_scheduling)

    # for section 6
    # if kwargs['method'] == 'existing':
    #     return 200
    # if kwargs['method'] == 'proposed':
    #     dag_scheduling = Dag(dag.wcets, dag.edges)
    #     scheduler = Scheduler(kwargs['core_num'])
    #     scheduled_nodes: list[Node] = scheduler.schedule_dag(dag_scheduling)

    # return evaluated value
    # in sample, response time of DAG (maximum finish time of all nodes)
    return max([n.finish_time for n in scheduled_nodes])

def simulate_taskset(dags: list[RDG_DAG]):
    loop_len = len(dags)
    results: list = []

    for idx, dag in enumerate(dags):
        results.append(simulate(dag))
        print("\r" + f'{idx+1} / {loop_len} : {100*(idx+1)/loop_len:.0f}%', end="")
    print()

    return results



################
### appendix ###
################



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
            results.append({'idx': idx, 'dag': dag, 'optional': opt})
        print("\r" + f'{idx+1} / {loop_len} : {100*(idx+1)/loop_len:.0f}%', end="")
    print()

    return results

def evaluate_varing_parameter(dags: list[RDG_DAG], arg_dict: dict={}, **kwargs):
    if len(kwargs) == 0:
        loop_len = len(dags)
        results_list: list = []
        for idx, dag in enumerate(dags):
            results_list.append(simulate(dag, **arg_dict))
            print("\r" + f'{idx+1} / {loop_len} : {100*(idx+1)/loop_len:.0f}% - {arg_dict}', end="")
        print()
        return results_list
    else:
        results_dict: dict = {}
        parameter_name, parameter_values = list(kwargs.items())[0]

        kwargs_updated = kwargs.copy()
        kwargs_updated.pop(parameter_name)

        for v in parameter_values:
            arg_dict_updated = arg_dict.copy()
            arg_dict_updated[parameter_name] = v

            results_dict[v] = evaluate_varing_parameter(dags, arg_dict_updated, **kwargs_updated)
        return results_dict
