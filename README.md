# gender-classifer-for-indonesian-names

Predicting Gender by Name for Indonesian Names.

<b> Training Data </b>   : Indonesian Actors and Actresses from Wikipedia <br>
<b> Text-Processing </b> : <br>
* Remove Punctuations </br>
* Remove Numbers </br>
* Convert to Lowercase </br>

<b> Feature Engineering </b> : CountVectorizer (Character N-Grams) </br>
<b> Target Variable Transformation </b> : Label Encoding (Binary) </br>
<b> Model </b> : Logistic Classifier </br>

This Repo consist of 5 files : 
* Daftar Seniman Indonesia (Wikipedia).xlsx -> Dataset (Excel) </br>
* nubi_genderClassifierByName.py -> Pre-Define Functions (Python Code) </br>
* nubi.stuff -> Saved Model and Feature Engineering (Python Serialized Object) </br>
* Sinubi - GenderClassifierByName (train).ipynb -> Jupyter Notebook for Training a Model </br>
* Sinubi - GenderClassifierByName (predict).ipynb -> Jupyter Notebook for Testing </br>

Please open "Sinubi - GenderClassifierByName (predict).ipynb" first and have fun with it :)

@Sinubi
