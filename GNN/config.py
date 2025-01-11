SEED_NO = 14492
DEVICE =  "cuda"
EPOCHS = 300
NUM_GRAPHS_PER_BATCH = 64
NUM_FEATURES=32
NUM_TARGET = 1
EDGE_DIM=11
PATIENCE = 10
N_SPLITS = 10

# Best hyperparameters
params_vertical_gnn = {'num_gin_layers': 2, 'num_graph_trans_layers': 2, 'hidden_size': 128, 'n_heads': 2, 'dropout': 0.1, 'learning_rate': 0.001}

