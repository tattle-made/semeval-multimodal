# Multimodal Machine Learning Pipeline

This is a description of the experimental multimodal pipeline we built for the multilabel classification subtask given in SemEval 2021 task 6 Subtask 3. The subtask is described in the [SemEval README](README.md). [This pipeline](SemEval-subtask3.ipynb) can be adapted for other use cases where we want to predict multiple labels for a set of memes  / images overlaid with text. 

#### Requirements

A dataset of memes with multiple non-exclusive binary labels. The text from the memes should be extracted via OCR, labelled and stored in the same folder as the images. See [the SemEval training data](training_set_task3/) for reference. The code in the [notebook](SemEval-subtask3.ipynb) requires the data to be present in this format; if the format is different, the `read_data()` function in the notebook will need to be modified accordingly. The output of `df.head()` in the notebook shows what type of data and format is expected. 

#### Improving the pipeline

This pipeline shows how to fuse a language model (Huggingface's BERT) with a vision model (ResNet18) to learn and predict labels for multimodal content. Results can be improved by methods such as using different models, tuning model hyperparameters, oversampling imbalanced labels, etc. 