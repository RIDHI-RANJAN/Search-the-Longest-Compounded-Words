import Trie as T
from collections import deque
import time

class CompoundWordFinder:
    def __init__(self):
        self.trie = T.Trie()
        self.queue = deque()

    def build_trie(self, file_path: str = None):
        try:
            with open(file_path, 'r') as f:
                for line in f:
                    word = line.rstrip('\n')
                    self.queue.extend((word, word[len(prefix):]) for prefix in self.trie.get_prefixes(word))
                    self.trie.insert(word)
        except Exception as e:
            print(f"Error reading the file: {str(e)}")
            exit(0)

    def find_longest_compound_words(self):
        longest, longest_len, second_longest = '', 0, ''
        while self.queue:
            word, suffix = self.queue.popleft()
            if suffix in self.trie and len(word) > longest_len:
                second_longest, longest, longest_len = longest, word, len(word)
            else:
                self.queue.extend((word, suffix[len(prefix):]) for prefix in self.trie.get_prefixes(suffix))

        return longest, second_longest

if __name__ == "__main__":
    finder = CompoundWordFinder()
    start_time = time.time()
    finder.build_trie("C:/Users/shant/OneDrive/Desktop/Impledge/Longest-Compound-Words-main/Longest-Compound-Words-main/Input_02.txt")
    longest_compound, second_longest_compound = finder.find_longest_compound_words()
    end_time = time.time()
    print("Longest Compound Word:", longest_compound)
    print("Second Longest Compound Word:", second_longest_compound)
    print("Time taken: ", str(end_time - start_time), "seconds")
