import numpy as np
import pandas as pd
from .FEP_dataset import fep_benchmark_dataset

class dataset:
	
	def __init__(self, dataset_nodes=None, dataset_edges=None, **kwargs):
		if dataset_nodes is None or dataset_edges is None:
			self.dataset_edges, self.dataset_nodes = fep_benchmark_dataset().get_dataset(kwargs["dataset_name"],
																						 kwargs["sampling_time"])
		else:
			self.dataset_nodes = dataset_nodes
			self.dataset_edges = dataset_edges
		self.cycle_data, self.node2idx, self.idx2node = self.get_graph_data(self.dataset_edges)
		self.estimators = [] # Whenever data from an estimator is added, it updates this list
	def get_graph_data(self, dataset_edges):
		"""
		
		@param dataset_edges:
		@return:
		"""

		start = []  # Source node
		end = []  # Destination node
		y = []  # FEP values
		ccc_dt = []  # CCC data schindler datasets TODO: Modify this
		idx = 0
		node2idx = dict()
		idx2node = dict()
		
		for row_idx, row in dataset_edges.iterrows():
			if row["Ligand1"] not in node2idx:
				node2idx[row["Ligand1"]] = idx
				idx2node[idx] = row["Ligand1"]
				idx += 1
			
			if row["Ligand2"] not in node2idx:
				node2idx[row["Ligand2"]] = idx
				idx2node[idx] = row["Ligand2"]
				idx += 1
			
			start.append(node2idx[row['Ligand1']] + 1)
			end.append(node2idx[row['Ligand2']] + 1)
			y.append(float(row["FEP"]))
			ccc_dt.append(float(row["CCC"]))
		
		# Export Data as dictionary
		cycle_dat = {
			'N': len(node2idx),
			'M': len(y),
			'src': start,
			'dst': end,
			'y': y,
			'ccc': ccc_dt}
		
		return cycle_dat, node2idx, idx2node