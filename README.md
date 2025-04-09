## hERG_binding_regressor   
### Folder

1. Data Folder   
   hERG_13281.csv: hERG pIC50 dataset;   
   MACCS.csv: MACCS Fingerprints of 13281 chemicals.

2. XGBoost Folder   
   XBoost.ipynb: develop XGBoost models based on fingerprints (such as MACCS).

3. GNN Folder (The code origninated from previous reference: 10.1021/acs.jcim.3c00554)   
   engine.py, model.py, utils.py: contain GNN models and helper functions;   
   config.py: hyperparameters and constant variables;   
   Train_GNN_model.ipynb: develop GNN models.



### Environment

To replicate or devleop models more conveniently, the environment file <environment.txt> is provided to install environment directly.
