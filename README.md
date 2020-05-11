
mri_subset_with_ICAE.ipynb :

loads a subset of 11 MRI records

changed x_train and x_test split to reflect last 'CN' record and last 'AD' record in x_test

brief exploratory analysis

CAE model (CNN without inception) encoder, decoder, autoencoder (refer to Arezoo's notebooks)

ICAE model (CNN with inception) encoder, decoder, autoencoder

classifiers with model plots (refer to plot_models_snippet.ipynb)

* issues with resulting metrics

--

balance_classes_snippet.ipynb :

code snippet to handle class imbalance with automatically determined class weights

--

plot_models_snippet.ipynb :

code snippet to plot each model to an output PNG file