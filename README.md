## hERG_binding_regressor   
### Folder

1. Data Folder   
   hERG_13281.csv: hERG pIC50 dataset;   
   MACCS.csv: MACCS Fingerprints of 13281 chemicals;   
   CECFP_Example.csv: Part of counted fingerprint of 13281 chemicals. (Note: Unable to provide the full CECFP fingerprint file due to file size limitations. It can be obtained from SMILES (hERG_13281.csv) by the RDKit using the “AllChem.GetHashedMorganFingerprint” commands.)

3. XGBoost Folder   
   XBoost.ipynb: develop XGBoost models based on fingerprints (such as MACCS).

4. GNN Folder      
   engine.py, model.py, utils.py: contain GNN models and helper functions;   
   config.py: hyperparameters and constant variables;   
   Train_GNN_model.ipynb: develop GNN models;   
   data: Contains train and validation set for developing GNN models.   
   (Note: The code origninated from previous reference: 10.1021/acs.jcim.3c00554)



### Environment

To replicate or devleop models more conveniently, the environment file <environment.txt> is provided to install environment directly.
