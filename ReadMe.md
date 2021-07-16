# Uncertainty Aware Learning
This project demonstrates the use of a neural network classifier parameterized on a source of systematic uncertainty – a nuisance parameter. The classifier learns a conditional decision function such that its dependence on the nuisance paramter can be profiled over for the final estimation of the parameter of interest. 

This project was developed to compare the advantages of this technique in comparison to the machine learning techniques that are currently used in High Energy Physics experiments, resulting in the paper : **Uncertainty Aware Learning for High Energy Physics** [arXiv:2105.08742](https://arxiv.org/abs/2105.08742).

# Notebooks
Two example notebooks illustrate how uncertainty aware learning works. The toy example is reccomended as an instructive self-contained notebook.

The notebook `Toy_Dataset.ipynb` studies a Gaussian toy problem where we have full analytical control. The baseline and uncertainty aware classifiers require no training as their optimal outputs can be calculated analytically. The notebook is generates the data, defines/trains the models and performs the evaluation. It therefore works standalone and is relatively fast to run (with the exception of training the adversarial classifier) unless the dataset size is increased.

The notebook `HiggsML_syst_evaluate.ipynb` demonstrates the comparisons performed on a real physics case with the  [HiggsML Dataset](http://opendata.cern.ch/record/328) after applying Tau Energy Scale shifts using [Victor Estrade's skewing function](https://doi.org/10.5281/zenodo.1887847).  An example of how the networks can be trained is shown in `HiggsML_syst_train.ipynb`. Both these notebooks take a considerable amount of time to run, the training notebook in particular should be treated only as an example and should not be run all in one go.
