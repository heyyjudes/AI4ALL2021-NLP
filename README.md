# Tweet Classification for Disaster Relief

This is the homepage for the [AI4ALL 2018](http://ai4all.stanford.edu/) NLP research project. 
Here you can find links to all class materials used for the research project.

Instructors: [Rob Voigt](https://nlp.stanford.edu/robvoigt/) (robvoigt@stanford.edu), [Bingbin Liu](https://www.linkedin.com/in/bingbinliu/) (bingbin@stanford.edu)

## Slides
* [Week 1 - Fri / Lesson 0: Introduction to NLP](https://docs.google.com/presentation/d/1t4fAHT-oCHGCkLXqqHSLu0kzJzADQD7G8JiaQdxPOdA/edit?usp=sharing)
* [Week 2 - Tue / Lesson 1: Rule-based classifiers](https://docs.google.com/presentation/d/1WG662N7UeeVViv-8UxWuwPHluyh2ZNL1DJmM55cydRs/edit?usp=sharing)
* [Week 2 - Wed / Lesson 2: Evaluation metrics](https://docs.google.com/presentation/d/1J0wa9ZLNve1Ndd-GniI8B2T1K6NsId5Y__REYndH9Ew/edit?usp=sharing) (Exercise sheet [here](https://docs.google.com/document/d/1IyynNr2hVJY8LOzFEBKRXNJ71usqfPQuR81lrFjEcPc/edit?usp=sharing))
* [Week 2 - Thu / Lesson 3: Probability theory and Bayes rule](https://drive.google.com/open?id=117pmZws2XxXOu68vnezh7y4LKCYNHrar6gk_Svap_rc) 
(Exercise sheet [here](https://docs.google.com/document/d/1u8pY6YicTEa3xZI6QxcPfrZ8A9mIJYxjA4iL6hpSB9c/edit?usp=sharing))
* [Week 2 - Fri / Lesson 4: Naive Bayes classifier](https://docs.google.com/presentation/d/1nVvoMwcDtgLSxXEdbRpLX0EbK7Yg_BFTC1WjTu7mSrk/edit?usp=sharing)
* [Week 3 - Mon / Lesson 5: More NLP](https://drive.google.com/open?id=1cBbLRibJG0drd8qnxQtt0yh08DGq0x5IosomjnDj2mc)
* [Week 3 - Tue / Lesson 6: Naive Bayes classifier for Twitter project](https://drive.google.com/open?id=1H2ty14VzCNaNC8GX1kYyveuqoRsAyfOAlSJHz3nFW8Q)
* [Week 3 - Wed / Lesson 7: Neural Networks](https://docs.google.com/presentation/d/1X45IZGTbvPyn41mZP9yA2y8y1NarhzDXWZbiATSRYuc/edit?usp=sharing)

### Presentation
* [5 minutes talk](https://docs.google.com/document/d/1pqF7j7oJR5bHGdmdFZ3CHWuaNYVX-Ev39Qjh2gWo5zA/edit?usp=sharing) at the banquet


## Other materials
* [Lesson 0: Data exploration spreadsheet](https://docs.google.com/spreadsheets/d/1EC83i5jhi5TjQTT4XN0v4CScZcie9WloASPGSEdJ2mY/edit?usp=sharing)
* [Python cheat sheet](https://docs.google.com/presentation/d/1ToMvqhFXC9XJgsqqSDhzhaIaSqWxnYAdp5sDYrfmj-I/edit?usp=sharing): feel free put comments / things you'd like to know about in the slides!
* [Naive Bayes cheat sheet](https://docs.google.com/document/d/1Z6WnbCQYtOsaoFAZc4VdXtCc9edGIlPBX9CulSwBVgo/edit)
* [Latex](http://latex2png.com/) to make our slides / poster pretty
* [Next Steps: Resources for after AI4ALL](https://docs.google.com/document/d/1_byDijN6Mc0Gk7phL5e5dmVuhyMkkZDNoEsXXvnfzPw/edit?usp=sharing)


## Instructions for running the notebooks
We will go through this together on July 3rd, but feel free to start on your own! :) 
1. Install Anaconda.
    
    Anaconda is a python distribution that makes it really easy to install additional python packages and manage different Python versions. You can download Anaconda from https://www.anaconda.com/download/. Make sure to download the Python 3.6 version! This should also automatically install Jupyter notebook, which you'll need to run the notebooks.

2. Install numpy and nltk:
    
    Open a Terminal window and type 
    
    ```
    conda install nltk numpy pandas
    ```

3. Copy ("clone") the GitHub repository to your computer:

    Open a Terminal window and type 
    
    ```
    git clone https://github.com/ClaraBing/AI4ALL2018
    ```
    
    This will copy all the notebooks to your computer.

4. Change into the directory:

   In the same Terminal window, type

   ```
   cd AI4ALL2018
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

The directory `filled` contains versions of the iPython notebooks with the solutions filled in, which will be released at the end of each day. If you would like to run these, you need to copy them to the main directory (i.e. `AI4ALL2018`), overwriting the blank versions of the notebooks that are currently there. Then run `jupyter notebook` and you should be able to access the completed versions of the notebooks.
