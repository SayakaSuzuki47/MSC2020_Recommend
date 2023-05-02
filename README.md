# MSC_Recommend
This is a script that recommends MSC2020 from abstracts and other texts.  

## Quick start
This repository includes a Jupyter Notebook file in the 'recom_MSC.ipynb' ; which can be executed on Google Colaboratory.

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
The error “Max retries exceeded with url” may occur; restarting with a new instance of Google Colaboratry may fix it.

## Acknowledgements/Licenses
This project uses the following open-source code or libraries:  
[[yanekyuk/bert-uncased-keyword-extractor](https://huggingface.co/yanekyuk/bert-uncased-keyword-extractor)] (apache-2.0)-[The model was used to generate predictions based on the input data].

In addition, the following code or library has been modified and used in this project:  
・[Mathematics Subject Classification 2020] (a Creative Commons [CC-BY-NC-SA license](https://creativecommons.org/licenses/by-nc-sa/4.0/))- [We have created a table of labels and their corresponding descriptions.]
Documentation and terms of use available at [Mathematics Subject Classification 2020](https://mathscinet.ams.org/msnhtml/msc2020.pdf).
The labels can be found in [MSC2020 table](MSC/MSC2020.tsv). If you notice any errors or omissions, please let us know. Thank you!

This project uses the following APIs:  
・[zbMATH Open API] ([CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/))- [We are crawling keywords and counting the number of classification labels in MSC2020]. Documentation and terms of use available at [[API URL](https://zboai.formulasearchengine.com/)]
