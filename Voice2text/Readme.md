This is a tool which convert your voice to electronic handwriting using combination of CNN and RNN
https://ieeexplore.ieee.org/document/9544925

<h1>Steps</h1>
The project is carried in two major step :
<ol>
  <li><b>Voice to text:</b> This step is achieved through Google Speech-to-text API</li>
  
  ![image](https://user-images.githubusercontent.com/46483403/123950227-13db8080-d9c1-11eb-89e8-336b506b8ee3.png)
 <br>
  *This is the text I am getting using Speech API

  <li><b>Text to Handwritten using Handwritting recognition using CNN and BILSTM technique</b></li>
    

![Capture](https://user-images.githubusercontent.com/46483403/123950565-746abd80-d9c1-11eb-9029-4cfc766e62d2.PNG)
<br>Build a model for handwrittten recognition (Used IAM and english character Dataset)
  </ol>
 <li> Atlast with the help of customized function, i passed my text file and then tokenize the word and replace letter with the handwritting accordingly</li>
  
  ![image](https://user-images.githubusercontent.com/46483403/123950999-ecd17e80-d9c1-11eb-8466-db4ba56a00fe.png)
<h1>Dataset</h1>
The IAM Handwriting dataset I have used contains 115,320 isolated and labeled images of words by 657 seperate writers.

IAM words dataset can be downloaded from <a href="https://fki.tic.heia-fr.ch/databases/iam-handwriting-database">here</a>. 
