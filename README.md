# MSC2020_Recommend
This is a script that recommends MSC2020 from abstracts and other texts.  

## Quick start
This repository includes a Jupyter notebook file in the 'recom_MSC2020.ipynb' format, which can be executed on Google Colaboratory.

To run the notebook on Google Colaboratory, please follow these instructions:

1. Open Google Colaboratory in your web browser.
2. Click on "File" in the top left corner of the screen, and then click on "Upload notebook".
3. Select the 'recom_MSC2020.ipynb' file from your local machine and upload it to Google Colaboratory.
4. Once the file has been uploaded, you can open it by double-clicking on the file name in the file browser on the left-hand side of the screen.
5. In the notebook, navigate to the cell where you are prompted to enter the text you want to classify.
6. Enter the text you want to classify in the text area provided.
7. You can choose the number of MSC2020 labels you want to display by changing the numerical value in the corresponding cell.
8. Once you have entered the text and selected the desired number of labels, run the notebook to see the classification results.

Please note that you will need a Google account to use Google Colaboratory.

## Acknowledgements/Licenses
This project uses the following open-source code or libraries:
This project uses the pre-trained machine learning model provided by [yanekyuk/bert-uncased-keyword-extractor](https://huggingface.co/yanekyuk/bert-uncased-keyword-extractor) from Hugging Face. The model was used to generate predictions based on the input data. The license for the model is apache-2.0, and we have confirmed that we are in compliance with the terms of that license.

In addition, the following code or library has been modified and used in this project:
The MSC2020 labels have been modified for ease of use and can be accessed from the following URL:
[Mathematics Subject Classification 2020](https://mathscinet.ams.org/msnhtml/msc2020.pdf)

The labels can be found in [MSC2020 table](MSC/MSC2020.tsv). If you notice any errors or omissions, please let me know. Thank you!
