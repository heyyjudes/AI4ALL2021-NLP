# Tweet Classification for Disaster Relief

This is the homepage for the [AI4ALL 2019](http://ai4all.stanford.edu/) NLP research project. 
Here you can find links to all class materials used for the research project.

2018 Instructors: [Rob Voigt](https://nlp.stanford.edu/robvoigt/) (robvoigt@stanford.edu), [Bingbin Liu](https://www.linkedin.com/in/bingbinliu/) (bingbin@stanford.edu)

2019 Instructors: Lucy Li (lucy3@stanford.edu) & Christina Yuan (cjyuan@stanford.edu)

## Slides
* [Week 1 - Thurs / Lesson 0: Introduction to NLP](https://docs.google.com/presentation/d/1S4bf1l4-g4BKkWFPutNyqi2YKJMoieTJHRfTTvB3edk/edit?usp=sharing)
* [Week 1 - Fri / Lesson 1: Rule-based classifiers](https://docs.google.com/presentation/d/1j1WkNvZBv5ularvSoY8r5doCL53Y4hdcIW8Y82afajE/edit?usp=sharing) ([Python cheat sheet](https://docs.google.com/presentation/d/1ToMvqhFXC9XJgsqqSDhzhaIaSqWxnYAdp5sDYrfmj-I/edit?usp=sharing))
* [Week 2 - Tues / Lesson 2: Evaluation metrics](https://docs.google.com/presentation/d/16a3Lf7Mp-_3UjEB_cmFlofRBbE2ONFm1BJkuzOgeRx0/edit?usp=sharing) (Exercise sheet [here](https://docs.google.com/document/d/1IyynNr2hVJY8LOzFEBKRXNJ71usqfPQuR81lrFjEcPc/edit?usp=sharing))
* [Week 2 - Wed / Lesson 3: Probability theory and Bayes rule](https://docs.google.com/presentation/d/18h0QDt5jQGx74L0OMbqjL24sIt_ooMCeVI9pfaDan1Q/edit?usp=sharing) 
(Exercise sheet [here](https://docs.google.com/document/d/1u8pY6YicTEa3xZI6QxcPfrZ8A9mIJYxjA4iL6hpSB9c/edit?usp=sharing))
* [Week 2 - Thurs / Lesson 4: Naive Bayes classifier](https://docs.google.com/presentation/d/10ucgKKkkEdG2OLIsDuRnQBGkeDIJTIayvxGl06E_mFg/edit?usp=sharing)
* [Week 2 - Fri / Lesson 5: More NLP](https://docs.google.com/presentation/d/1fWRKDyyQIqH5s98iB0_HrN90TlMbE-W1PHLGfHOUMYM/edit?usp=sharing)
* [Week 3 - Mon / Lesson 6: Naive Bayes classifier for Twitter project](https://docs.google.com/presentation/d/1q3KTSEHeq4btUdQ7d3rYVBeqgCb8KWKRvQrNebnNHws/edit?usp=sharing)
* [Week 3 - Tues / Lesson 7: Neural Networks](https://docs.google.com/presentation/d/1IalgO0s9w3-hwvMcm9ii9Vv9kJ3v5UHOUL95ZqG8O2c/edit?usp=sharing)

### Presentation
* 5 minutes talk at the banquet (we will add your outline here) 


## Other materials
* [Lesson 0: Data exploration spreadsheet](https://docs.google.com/spreadsheets/d/1EC83i5jhi5TjQTT4XN0v4CScZcie9WloASPGSEdJ2mY/edit?usp=sharing)
* [Lecture on text processing](https://web.stanford.edu/class/cs124/lec/textprocessingboth.pdf) (e.g. regular expression, tokenization, lemmatization/stemming) from [Stanford CS 124](http://web.stanford.edu/class/cs124/#schedule) by Professor [Dan Jurafsky](https://web.stanford.edu/~jurafsky/)
* [Python cheat sheet](https://docs.google.com/presentation/d/1ToMvqhFXC9XJgsqqSDhzhaIaSqWxnYAdp5sDYrfmj-I/edit?usp=sharing): feel free put comments / things you'd like to know about in the slides!
* [Naive Bayes cheat sheet](https://docs.google.com/document/d/1Z6WnbCQYtOsaoFAZc4VdXtCc9edGIlPBX9CulSwBVgo/edit)
* [Latex](http://latex2png.com/) to make our slides / poster pretty
* [Next Steps: Resources for after AI4ALL](https://docs.google.com/document/d/1_byDijN6Mc0Gk7phL5e5dmVuhyMkkZDNoEsXXvnfzPw/edit?usp=sharing)


## Instructions for running the notebooks
We will go through this together on June 27, but feel free to start on your own! :) 
1. Check if Anaconda is installed, or install Anaconda.

    ```
    conda
    ```
    
    If you get ```-bash: conda: command not found```, you don't have Anaconda yet!
    
    Anaconda is a python distribution that makes it really easy to install additional python packages and manage different Python versions. You can download Anaconda from https://www.anaconda.com/download/. Make sure to download the Python 3.6 version! This should also automatically install Jupyter notebook, which you'll need to run the notebooks.

2. Install numpy and nltk:
    
    Open a Terminal window and type 
    
    ```
    conda install nltk numpy pandas
    ```

3. Copy ("clone") the GitHub repository to your computer:

    Open a Terminal window and type 
    
    ```
    git clone https://github.com/lucy3/AI4ALL2019
    ```
    
    This will copy all the notebooks to your computer.

4. Change into the directory:

   In the same Terminal window, type

   ```
   cd AI4ALL2019
   ```

5. Download the tokenizer models:

    Start a Python console by typing `python` in the Terminal window. Then run the following commands:

    ```
    import nltk
    nltk.download("punkt")
    exit()
    ```

6. Run the jupyter notebook:

    ```
    jupyter notebook
    ```

## Accessing the completed versions of the notebooks

The directory `filled` contains versions of the iPython notebooks with the solutions filled in, which will be released at the end of each day. If you would like to run these, you need to copy them to the main directory (i.e. `AI4ALL2019`), overwriting the blank versions of the notebooks that are currently there. Then run `jupyter notebook` and you should be able to access the completed versions of the notebooks.
