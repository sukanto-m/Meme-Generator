# Meme Generator
In this project, a Python app generates memes via random quotes and images. 

The program scripts can be set up by running the requirements.txt file from the command line in a virtual environment, which installs the required dependencies on 
the computer. It comprises the following components primarily:

### Quote Engine 
This folder uses a number of scripts to parse quotes from the following sets of file formats: .txt, .csv, .pdf and .docx. The associated scripts ie Ingestors for each
file type use a specific library (eg Pandas for CSV) to parse and then the QuoteModel file represents the way the quotes should be read on the memes. The IngestorInterface abstract base class is used for each file except QuoteModel. The QuoteModel file is used to set up certain ingestors to set up the quotes, as well as in the app.py and meme.py scripts.

### MemeGenerator
In this folder the MemeEngine.py script grabs an image using the Pillow library and scales it appropriately for the meme. The file also sets up the variables
and images, including the output, before saving them to an output file.

### App.py & Meme.py
These two scripts wrap the QuoteEngine and MemeGenerator outputs to set up the meme, either on a web server via Flask or on the command line. App.py
randomises the file selection and uses the files in templates to generate a meme. Meme.py enables the user to provide optional arguments in the command line 
for image path, meme body and author to return a path to a generated image.
