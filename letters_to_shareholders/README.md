
# Infusing ChatGPT with legendary Warren Buffet's letters to shareholders

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Running the App](#running-the-app)
5. [Sample output](#sample-output)

## Introduction

This micro project aims to infuse GPT models with the legendary wisdom coming from the Warren Buffett's letters to shareholders.

![Buffett's picture](https://github.com/lsirse/Data-Science-Portfolio/blob/master/letters_to_shareholders/data/buffett_smaller.png)

## ToDo

This micro project is just a demonstration of the capabilities of Langchain library & Large Language models and is far from being production-ready. Possible areas of improvement are:

- UI: Develop better, more intuitive user interface
- Methodology optimization: Refine the approach through testing.
- Multi-turn conversation: Enable dynamic, coherent dialogues.
- Complete Buffett letters: Include all letters dating from 1965


## Requirements

Before you can install the required Python libraries, please ensure that you have the following software installed:

* Python 3.9 or later
* A Python package manager, such as Anaconda or pip

You can download the Anaconda distribution, which includes both Python and the conda package manager, from https://www.anaconda.com/products/individual.

## Installation

1. Change to the project directory:

   ```
   cd letters_to_shareholders
   ```

2. Create a virtual environment (optional, but recommended):

   ```
   conda create --name letters_to_shareholders python=3.9
   ```

3. Activate the virtual environment (optional, but recommended):
   ```
   conda activate letters_to_shareholders
   ```

4. Install the required Python libraries:

   ```
   pip install -r requirements.txt
   ```

   This command will install all the necessary dependencies specified in the `requirements.txt` file.

## Running the App

1. Make sure you're in the `letters_to_shareholders` directory and your virtual environment is activated.

2. Fill in your OpenAI API key into `config.py` file.

3. Run the app using the following command:

   ```
   python app.py
   ```

   This will start the letters_to_shareholders app, and you should see the app's output.
   

## Sample output

```
(letters_to_shareholders) user@user:~/$ python app.py 
Loading letters to shareholders...
100%|████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  1.10it/s]
100%|████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00,  2.47it/s]
Splitting data into chunks...
Generating embeddings...
Using embedded DuckDB without persistence: data will be transient
Emeddings successfully generated...
─────────███─────────
─────────█$█─────────
─────█████$██████────
───███████$████████──
──████████$████████──
─█████████$████████──
─███████─█$█──████───
─███████─█$█─────────
─█████████$█─────────
─█████████$█████─────
──████████$███████───
────██████$█████████─
───────███$█████████─
─────────█$█─████████
─────────█$█──███████
──████───█$█──███████
─█████████$█████████─
██████████$█████████─
─█████████$████████──
───███████$██████────
─────────█$█─────────
─────────███─────────
Please enter (another) question to answer from the content of Warren Buffett's letters to shareholders (years 1978 - 2022) or type 'exit' to quit: How does Warren Buffett handle risk?
You entered: How does Warren Buffett handle risk?
Generating the answer, it may take some time...
Here's the answer generated:
{'output_text': '\n\nWarren Buffett handles risk by assuming it on a large scale, which interests virtually no other company. He is willing to write business as Berkshire\'s net worth and earnings grow, making these moves in recognition of Berkshire\'s financial strength and tolerance for wide swings in earnings. As he stated in a speech given in March 1980, "Risk is not only an inherent part of investing, but it is also a necessary part of the process of achieving satisfactory long-term returns." He is also careful to ensure that the risks taken are proportional to the resources available to Berkshire, and he takes steps to ensure that the risks taken are appropriate in relation to the resources available to Berkshire. In the first ten years in control of Berkshire, Buffett saw one business (textiles) move close to death and two new businesses come in, for a net gain of one. Buffett was aiming to create a system that would allow Berkshire to take on risks that were proportional to its resources, while also ensuring that the risks taken were appropriate in relation to the resources available and that they would not expose Berkshire to losses beyond what they could comfortably handle. He would manage almost all security investments, with these normally residing in Berkshire’s casualty insurers. Additionally, Buffett has a long-term view of risk,'}
Please enter (another) question to answer from the content of Warren Buffett's letters to shareholders (years 1978 - 2022) or type 'exit' to quit: How does Warren Buffett handle CEOs of the companies he acquires?             You entered: How does Warren Buffett handle CEOs of the companies he acquires?
Generating the answer, it may take some time...
Here's the answer generated:
{'output_text': '\n\nWarren Buffett is known for taking a hands-off approach to the CEOs of the companies he acquires. He typically chooses CEOs who are trustworthy, skilled, energetic, and have a love for the business and its circumstances. He then allows them to continue running the company as they did before, without raising their revenues or cutting their costs, while providing guidance and support when needed. Buffett also takes into account whether the company has the right CEO, if they are overreaching in terms of compensation, and if proposed acquisitions are more likely to create or destroy per-share value. At Berkshire, Buffett is a one-man compensation committee who determines the salaries and incentives for the CEOs of around 40 significant operating businesses. Buffett also takes the time to develop relationships with the CEOs of the companies he acquires, so that counterparties are both familiar with and feel comfortable with him. This approach has been in place since Buffett took over as Chairman of the Board in February 1981, and has been successful in creating a net gain of one business for Berkshire in the first ten years of control. Buffett also invests in businesses that he controls, usually buying 100% of each. He directs capital allocation at these subsidiaries and selects the CEOs who make day-by-day operating decisions. Charlie and I'}
Please enter (another) question to answer from the content of Warren Buffett's letters to shareholders (years 1978 - 2022) or type 'exit' to quit: exit
Goodbye!
```

## License considerations

The Warren Buffett's letters to shareholders dataset provided in this project is intended for academic and research purposes only. These letters contain valuable insights into the investment strategies and philosophies of one of the world's most renowned investors. It is important to note that these letters should not be used for commercial purposes or any other unauthorized uses. 