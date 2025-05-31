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

To replicate or devleop models more conveniently, the environment file <environmental.yml> is provided to install environment directly.    


```
conda env create -f environment.yaml
```   


## Main

### Data   
   hERG_R_13818.csv: hERG dataset with 13818 SMILES and pIC50 values, which is used to develop XGBoost-CECFP model;  
   
   hERG_R_13890.csv: hERG dataset with 13890 SMILES, pIC50 values, and two source informantion, which is used to develop XGBoost-CECFP-S model;   

   hERG_R_6952.csv: hERG dataset with 6952 SMILES and pIC50 values from ChEMBL, which is used to develop XGBoost-CECFP-C model;
   
   CECFP.zip: Unzip to get counted_ECFP fingerprints of chemicals in above 3 csv files.

   (Note: Counted_ECFP can be obtained from SMILES by the RDKit using the ```AllChem.GetHashedMorganFingerprint``` commands.)

### XGBoost  
   ```XGBoost.ipynb```: develop XGBoost models based on fingerprints (such as CECFP, which can be obtained conveniently by unzipping CECFP.zip in the data file);  
   
   ```XGBoost-CECFP.pkl```: The optimal model, which can be used to predict the hERG pIC50 values for given SMILES (with calculated CECFP).    

   ```XGBoost-CECFP-S.pkl```: The model developed based on CECFP and Source features (hERG_R_13890).    

   ```XGBoost-CECFP-C.pkl```: The model developed based on ChEMBL dataset (hERG_R_6952). 

### GNN     
   ```engine.py, model.py, utils.py```  : contain GNN models and helper functions;
   
   ```config.py``` : hyperparameters and constant variables;
   
   ``` Train_GNN_model.ipynb ``` : develop GNN models;
   
   data: contains train and validation set for developing GNN models.
   
   (Acknowledgments: The code origninated from previous reference: DOI: 10.1021/acs.jcim.3c00554)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
### ADSAL   
   ```pyAppDomain.py and metAppDomain_ADM.py```: Required files for structure activity landscape-based application domains (ADSAL);   
   
   ```ADSAL.ipynb```: characterize the ADSAL of a model; Users can set different application domain stringency levels according to the instructions in the codes and their own needs, in order to achieve the function of improving the prediction of the model.   

   Training_set.csv and VS.csv: Training and validation sets used in the current study for developing the optimal XGBoost-CECFP model; here, the validation set data gives the prediction results for the convenience of the application domain characterization.
   
   (Acknowledgments: The code origninated from previous reference: DOI: 10.1021/acs.chemrestox.3c00074)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        




