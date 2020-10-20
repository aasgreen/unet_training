# General Notes
Planning on getting this running quickly. 
Phase 1. Get all elements running.
Phase 2. Transfer everything over to a docker file.




# Timeline Notes
## Oct 09

I've got the unet working, and the training is happening.
Features to add-- ability to automatically save state, and load state
Experiment results: training loss vs epoch file. experimental parameters. unet architecture. Hash file name.

Other things I want to do today. Try to get this down to a one pixel mask. Reweight the training classes. Rebalance the unet so 
that the cropping isn't needed. 

Other things. Send follow up email to ISSS and the i9 office. Christoph's thesis. 

## Oct 05 2020
We need to first extract the unet out of ravin's program, and make our own package 
for it.

I am thinking that we will keep the unet isolated from the rest of the code, so it
will be easy to experiment with tweaking the models. This way we can 'snapshot' the
different unet architecture, and experiment a little more qualitatively (storing validation metrics).

So then, the dev package directory will have a few files.
unet.py (current unet architecture)
unet_arxive/ (folder for old unets-- we'll need to label each unet then with a timestamp, or a hash or something.)
data.py (python file to generate, load and muck with all the data)
config.yaml (parameters to run the current experiment, I may split this if I need to.)
ml_pipeline.py (python that lays out the pipeline for the ml experiment-- loading, training, etc)
run_experiment.py (code to actually run everything.)

and the experiment will save the results to two places.

results_big/ containing the masks for all the validation images (this will show the ground truth and enable an image by image
comparison of what is going on.)
results_small/ containing just the main figures of merit (pixel accuracy, number predicted, etc) and a copy of all the code required to run this in a zipped folder. This way we can keep a record of all of our experiments.

We will also log all of our results into a log file, containing the main figures of merit.

