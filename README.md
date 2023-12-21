# Search-the-Longest-Compounded-Words

This Python script finds the longest and second-longest compound words in a given input file using a Trie data structure.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [How to Run](#how-to-run)
- [Example](#example)

## Introduction

This solution employs a Trie data structure to efficiently find the longest and second-longest compound words in a given input file.

## Features

- Trie-based implementation
- Efficient compound word search
- Python 3 compatible

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/Longest-Compound-Words.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Longest-Compound-Words
    ```

3. Install the required dependencies:

    ```bash
    # If using a virtual environment
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

    # Install dependencies
    pip install -r requirements.txt
    ```

## How to Run
Run the `Solution.py` script with the path to the input file as an argument:

```bash
python Solution.py "path/to/your/input/file.txt"
```
Replace "path/to/your/input/file.txt" with the actual path to your input file

## Example

Input:
```
File Name: Input_01.txt
Contents:
bash
Copy code
cat
cats
catsdogcats
catxdogcatsrat
dog
dogcatsdog
hippopotamuses
rat
ratcatdogcat
```
Output:
```
Longest Compound Word: ratcatdogcat
Second Longest Compound Word: catsdogcats
Time taken: 500 milliseconds
```
Note:
Hippopotamuses is the longest word but not a compounded word.

