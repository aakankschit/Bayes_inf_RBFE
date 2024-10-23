import pandas as pd


class fep_benchmark_dataset:
    """Extract Data from Schindler et. al Repo and Construct CCC performance plots using Cinnabar"""
    
    def __init__(self):
        raw_dt_base_link = "https://raw.githubusercontent.com/MCompChem/fep-benchmark/master/"
        self.list_of_dtsets = ["cdk8", "cmet", "eg5", "hif2a", "pfkfb3", "shp2", "syk", "tnks2"]

        # Constructing dataset containing edge data
        # Constructing dataset containing node data
        all_edge_data = pd.DataFrame(columns = ['Ligand1', 'Ligand2', 'Exp.', 'FEP', 'FEP Error', 'CCC', 'CCC Error',
        'Dataset', 'Sampling Time'])
        all_node_data = pd.DataFrame(columns = ['Ligand', 'Pred. ΔG', 'Pred. Error','Exp. ΔG','Exp. Error','Dataset', 'Sampling Time'])
        for dataset in self.list_of_dtsets:

            # Extract Edge data for 20ns and 5ns sampling datasets

            ## Extract 5ns dataset 
            five_ns_dataset_url = raw_dt_base_link+dataset+"/results_edges_5ns.csv"
            df_fivens_temp = pd.read_csv(five_ns_dataset_url)
            df_fivens_temp = df_fivens_temp.drop(columns=["Solvation","Solvation Error"]) # Drop Solvation
            dataset_col = [dataset]*len(df_fivens_temp) # Creates a column of dataset names associated with dataset
            sampl_time = ["5ns"]*len(df_fivens_temp) # Creates a column of sampling time 
            df_fivens_temp['Dataset']=dataset_col
            df_fivens_temp['Sampling Time'] = sampl_time
            all_edge_data = pd.concat([all_edge_data,df_fivens_temp],ignore_index=True)

            ## Extract 20ns dataset
            twenty_ns_dataset_url = raw_dt_base_link+dataset+"/results_edges_20ns.csv"
            df_twentyns_temp = pd.read_csv(twenty_ns_dataset_url)
            df_twentyns_temp = df_twentyns_temp.drop(columns=["Solvation","Solvation Error"]) # Drop Solvation
            dataset_col = [dataset]*len(df_twentyns_temp) # Creates a column of dataset names associated with dataset
            sampl_time = ["20ns"]*len(df_twentyns_temp) # Creates a column of sampling time 
            df_twentyns_temp['Dataset']=dataset_col
            df_twentyns_temp['Sampling Time'] = sampl_time
            all_edge_data = pd.concat([all_edge_data,df_twentyns_temp],ignore_index=True)

            # Extract Node data for 20ns and 5ns sampling datasets

            ## Extract 5ns dataset 
            five_ns_dataset_nodes_url = raw_dt_base_link+dataset+"/results_5ns.csv"
            df_fivens_temp_nodes = pd.read_csv(five_ns_dataset_nodes_url)
            df_fivens_temp_nodes = df_fivens_temp_nodes.drop(columns=['Affinity unit', ' # ', 'Quality', 'Structure']) # Drop Columns in node dataset
            dataset_col = [dataset]*len(df_fivens_temp_nodes) # Creates a column of dataset names associated with dataset
            sampl_time = ["5ns"]*len(df_fivens_temp_nodes) # Creates a column of sampling time 
            exp_error = [float(0)]*len(df_fivens_temp_nodes)
            df_fivens_temp_nodes['Dataset']=dataset_col
            df_fivens_temp_nodes['Sampling Time'] = sampl_time
            df_fivens_temp_nodes['Exp. Error'] = exp_error
            all_node_data = pd.concat([all_node_data,df_fivens_temp_nodes],ignore_index=True)

            ## Extract 20ns dataset
            twenty_ns_dataset_nodes_url = raw_dt_base_link+dataset+"/results_20ns.csv"
            df_twentyns_temp_nodes = pd.read_csv(twenty_ns_dataset_nodes_url)
            df_twentyns_temp_nodes = df_twentyns_temp_nodes.drop(columns=['Affinity unit', ' # ', 'Quality', 'Structure']) # Drop Columns in node dataset
            dataset_col = [dataset]*len(df_twentyns_temp_nodes) # Creates a column of dataset names associated with dataset
            sampl_time = ["20ns"]*len(df_twentyns_temp_nodes) # Creates a column of sampling time 
            df_twentyns_temp_nodes['Dataset']=dataset_col
            df_twentyns_temp_nodes['Sampling Time'] = sampl_time
            df_twentyns_temp_nodes['Exp. Error'] = exp_error
            all_node_data = pd.concat([all_node_data,df_twentyns_temp_nodes],ignore_index=True)
            
        self.all_edge_data = all_edge_data
        self.all_node_data = all_node_data
    
    def get_dataset(self,dataset,sampling_time):
        data_edges = self.all_edge_data.loc[(self.all_edge_data['Dataset']==dataset) & 
                                            (self.all_edge_data['Sampling Time'] ==sampling_time),:]
        data_nodes = self.all_node_data.loc[(self.all_node_data['Dataset']==dataset) &
                                    (self.all_node_data['Sampling Time']==sampling_time),:]
        data_edges = data_edges.reset_index(drop=True)
        data_nodes = data_nodes.reset_index(drop=True)
        return data_edges,data_nodes
        
        
            