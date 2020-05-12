
import glob
import pandas as pd
import pickle
import ants # !pip install antspyx
import matplotlib.pyplot as plt
import numpy as np
import os
#ad_path = '/Users/daniel/Downloads/AD_MRI'
#paths = glob.glob('./**/*.nii*',recursive=True)
#scan_IDz=pd.read_csv(ad_path+"/scan_IDs20.csv",header=None)
#scan_IDs=[i[0] for i in scan_IDz.values]
import pickle
with open('AD_MRI_Master','rb') as f:
    AD_MRI_Master = pickle.load(f)

######



# make QA sheet
mnipath = 'MNI152_T1_1mm.nii.gz'
mni=ants.image_read(mnipath).numpy()#

data_paths = glob.glob('PROCESSED/*')
AD_MRI_QA = pd.DataFrame.from_dict(AD_MRI_Master,orient='index')

AD_MRI_QA['has_T1'] = np.nan
AD_MRI_QA['QA'] = np.nan



for sub in ('OAS30020',
'OAS30022',
'OAS30032',
'OAS30038'):
    
    
    if any(sub in i for i in data_paths):
        AD_MRI_QA.loc[sub,'has_T1']= 'good'
    else:
        AD_MRI_QA.loc[sub,'has_T1']= 'missing'
    
    
    with open('PROCESSED/'+sub+'_data','rb') as f:
        data = pickle.load(f)

    print("loading...")
    img= data['image']
    mni=ants.image_read(mnipath).resample_image((120,160,120),use_voxels=True).numpy()


    
    fig, axs = plt.subplots(3,4)
    
    
    axs[0,0].imshow(mni[:,:,60],cmap='gray')
    axs[0,0].imshow(img[:,:,60],alpha=0.4)
    
    axs[0,1].imshow(mni[:,:,45],cmap='gray')
    axs[0,1].imshow(img[:,:,45],alpha=0.4)
    
    axs[0,2].imshow(mni[:,:,75],cmap='gray')
    axs[0,2].imshow(img[:,:,75],alpha=0.4)

    
    axs[1,0].imshow(np.rot90(mni[:,80,:]),cmap='gray')
    axs[1,0].imshow(np.rot90(img[:,80,:]),alpha=0.4)
    
    axs[1,1].imshow(np.rot90(mni[:,100,:]),cmap='gray')
    axs[1,1].imshow(np.rot90(img[:,100,:]),alpha=0.4)
    
    axs[1,2].imshow(np.rot90(mni[:,100,:]),cmap='gray')
    axs[1,2].imshow(np.rot90(img[:,100,:]),alpha=0.4)
    

    axs[2,0].imshow(np.rot90(mni[60,:,:]),cmap='gray')
    axs[2,0].imshow(np.rot90(img[60,:,:]),alpha=0.4)
    
    axs[2,1].imshow(np.rot90(mni[45,:,:]),cmap='gray')
    axs[2,1].imshow(np.rot90(img[45,:,:]),alpha=0.4)
    
    axs[2,2].imshow(np.rot90(mni[75,:,:]),cmap='gray')
    axs[2,2].imshow(np.rot90(img[75,:,:]),alpha=0.4)
    
    axs[2,3].imshow(np.rot90(img[60,:,:]))
    axs[1,3].imshow(np.rot90(img[:,80,:]))
    axs[0,3].imshow(img[:,:,60])
    
    
    fig.suptitle(sub)
    plt.show(block = False)
    #QA=input("how does it look?")
    
    
    QA = input("How's it look? type g for good, b for bad:  ")
    if str(QA) == 'g':
        AD_MRI_QA.loc[sub,'QA']= 'good'
    elif str(QA) == 'b':
        AD_MRI_QA.loc[sub,'QA']= 'bad'
    else:
        print("something went wrong! you entered"+str(QA))
    
    plt.close(fig)

    #QA=input("how does it look?")
    
    

AD_MRI_QA.to_csv("AD_MRI_QA_Spreadsheet_update.csv")