# hERG_binding_regressor   
## Environment

The most important python packages are:   

python == 3.9.15   
pytorch == 1.12.1   
xgboost == 2.1.4   
rdkit == 2022.09.5   
scikit-learn == 1.2.0   
optuna == 3.1.0   
numpy == 1.23.5   
pyvis == 0.3.2   

To replicate or devleop models more conveniently, the environment file <environmental.yml> is provided to install environment directly. (command： conda env create -f environment.yaml)   


## Main

### Data   
   hERG_13281.csv: hERG dataset with SMILES and pIC50 values;
   
   CECFP.zip: Unzip to get counted_ECFP fingerprint of 13281 chemicals.

   (Note: Counted_ECFP can be obtained from SMILES by the RDKit using the “AllChem.GetHashedMorganFingerprint” commands.)

### XGBoost  
   XGBoost.ipynb: develop XGBoost models based on fingerprints (such as CECFP, which can be obtained by unzipping CECFP.zip in the data file);  
   
   XGB-CECFP.pkl: The optimal model, which can be used to predict the hERG pIC50 values for given SMILES (with calculated CECFP).      

### GNN     
   engine.py, model.py, utils.py: contain GNN models and helper functions;
   
   config.py: hyperparameters and constant variables;
   
   Train_GNN_model.ipynb: develop GNN models;
   
   data: contains train and validation set for developing GNN models.
   
   (Note: The code origninated from previous reference: DOI: 10.1021/acs.jcim.3c00554)
        
        
        
        
        
        
        
           
### ADSAL   
   metAppDomain_ADM.py and pyAppDomain.py: Required files for structure activity landscape-based application domains (ADSAL);   
   
   ADSAL.ipynb: characterize the ADSAL of a model.   
   
   (Note: The code origninated from previous reference: DOI: 0.1021/acs.chemrestox.3c00074)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




