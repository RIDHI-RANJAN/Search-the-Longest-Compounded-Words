# Longest Compound Words Finder

This Python script finds the longest and second-longest compound words in a given input file using a Trie data structure.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [Design and Approach](#design-and-approach)
- [Eample](#example)

## Introduction

This Python script uses a Trie data structure to efficiently find the longest and second-longest compound words in a given input file. It is designed to handle both small word lists and larger datasets with over 100,000 items.


## Features

- Trie-based implementation
- Efficient compound word search
- Python 3 compatible

## Requirements

- Python 3.x
  
## How To Run

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yourusername/Longest-Compound-Words.git
    cd Longest-Compound-Words
    ```

2. **Install Dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the Script:**
    ```bash
    python Solution.py "path/to/your/input/file.txt"
    ```

    Replace `"path/to/your/input/file.txt"` with the actual path to your input file.

## Design and Approach

- **Trie Data Structure:** The program utilizes a Trie to efficiently store and search for words. This allows for quick retrieval of prefixes and checking if a word is a valid compound word.

- **Queue for Compound Word Exploration:** A deque (double-ended queue) is used to explore compound words. The program iterates through the queue, continually checking and updating the longest and second-longest compound words.

- **Efficient Word Processing:** The script processes words line by line from the input file, efficiently storing them in the Trie. It then explores compound words using the Trie's structure.

- **Time Complexity:** The time complexity of finding the longest and second-longest compound words is O(N * M), where N is the total number of characters in the input file and M is the length of the longest compound word. The Trie structure provides efficient prefix matching, making the algorithm faster compared to brute-force methods.

- **Best Solution:** The Trie-based approach is considered the best solution for compound word search due to its efficient prefix matching and traversal capabilities. It minimizes redundant comparisons and provides a systematic way to explore compound words. The use of a deque further optimizes the exploration process.

- **Clear Output:** The script provides clear output, indicating the longest and second-longest compound words along with the time taken for the process. It notes if the longest word is not a compounded word.

Feel free to adjust the input file path and explore different datasets to find compound words efficiently.

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

