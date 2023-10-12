from __future__ import annotations

import yaml
from networkx import DiGraph, all_simple_paths
from PIL import Image
from glob import glob

class RDG_DAG:
    def __init__(self, wcets: list[int], edges: list[set[int]], rdgen_obj: dict, filepath: str, img: Image.Image):
        self._wcets = wcets
        self._edges = edges
        self._rdgen_obj = rdgen_obj
        self._filepath = filepath
        self._img = img

        self._graph = DiGraph()
        self._graph.add_nodes_from(range(len(wcets)))
        self._graph.add_edges_from(edges)

    def pred(self, idx: int) -> list[int]:
        return [_ for _ in self.graph.predecessors(idx)]

    def succ(self, idx: int) -> list[int]:
        return [_ for _ in self.graph.successors(idx)]

    @property
    def paths(self) -> list[list[int]]:
        _paths: list[list[int]] = []
        for sr in self.src:
            for sn in self.snk:
                _paths.extend(all_simple_paths(self._graph, sr, sn))
        # for path in paths:
        return _paths

    @property
    def src(self) -> list[int]:
        return [i for i in range(len(self.wcets)) if len(self.pred(i)) == 0]

    @property
    def snk(self) -> list[int]:
        return [i for i in range(len(self.wcets)) if len(self.succ(i)) == 0]

    @property
    def wcets(self) -> list[int]:
        return self._wcets

    @property
    def edges(self) -> list[set[int]]:
        return self._edges

    @property
    def rdgen_obj(self) -> dict:
        """
        row data of yaml file of RD-Gen
        """
        return self._rdgen_obj

    @property
    def filepath(self) -> str:
        return self._filepath

    @property
    def img(self) -> Image.Image:
        return self._img

    @property
    def graph(self) -> DiGraph:
        return self._graph

    @classmethod
    def load_from_rd_gen(cls, filepath: str, graphpath: str | None=None) -> RDG_DAG:
        try:
            file = open(filepath, 'r')
            rdg_obj = yaml.safe_load(file)
        except:
            print(f'RD-Gen: {filepath} not exists')
            exit()

        if graphpath:
            img = Image.open(graphpath)
        else:
            img = Image.open(filepath.replace('.yaml', '.png'))

        # define node
        wcets = [n['execution_time'] for n in sorted(rdg_obj['nodes'], key=lambda x: x['id'])]
        edges = [(e['source'], e['target']) for e in rdg_obj['links']]

        return RDG_DAG(wcets, edges, rdg_obj, filepath, img)

    @classmethod
    def load_from_rd_gen_dir(cls, dirpath: str, regex: str='*'):
        dags: list[RDG_DAG] = []
        for filepath in glob(f'{dirpath}/{regex}.yaml'):
            dags.append(cls.load_from_rd_gen(filepath))

        return dags
