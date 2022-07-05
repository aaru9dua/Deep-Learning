<h1> Problem Statement </h1>
<li> The number and forms of criminal activities are increasing at an alarming rate due to this, security has been given principal significance. </li>
<li>Impossible constant supervision and excessive human work </li>


<h1> Solution </h1>
<li>The project aims to build a model to identify signs of violence from video, which filters out irregularities from normal patterns.</li>
<li>Deep Learning can be a tremendous tool for crime pattern detection. Thus, this effective tool can detect activities which are anomalous or suspicious using Artificial Intelligence.
</li>

<h1>Algorithmic Approach</h1>

<li>The model is trained on untrimmed real-time surveillance videos, to which preprocessing techniques are applied by trimming them into 10-30 seconds clips, resizing and normalizing the frames throughout.</li>
<li>The frames of the videos are then passed in the ConvLSTM2D model.</li>
<li>The main aim of the model is to understand the abnormal patterns and evaluate it to categorize the footage according to the criminal activity.</li>
<li>The model is merged with an Interface to bring more clarity and user-friendly approach to it. By taking in the feed from live surveillance in any form our model can generate alerts and also tell the crime taking place so as to provide the severity according to the user. </li>



<h1> Prototype </h1>


https://user-images.githubusercontent.com/46483403/177372513-a0868cb9-f645-40c2-994d-fa04e85cd9c0.mp4



