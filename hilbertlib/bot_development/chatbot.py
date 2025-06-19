import pickle
from rapidfuzz import fuzz
import os

class ChatBot:
    def __init__(self):
        self.data = []  # list of (trigger, response, threshold)

    def is_similar(self, text1, text2, threshold_percent):
        similarity = fuzz.token_sort_ratio(text1, text2)
        return similarity >= threshold_percent

    def add(self, trigger, response, threshold_percent=100):
        self.data.append((trigger, response, threshold_percent))

    def remove(self, trigger):
        # remove all items with exact trigger match
        self.data = [item for item in self.data if item[0] != trigger]

    def get_response(self, prompt):
        for trigger, response, threshold in self.data:
            if self.is_similar(prompt, trigger, threshold):
                return response
        return "Sorry, I don't understand."

    def save(self, filename):
        if not filename.endswith(".hlibcb"):
            filename += ".hlibcb"
        with open(filename, "wb") as f:
            pickle.dump(self.data, f)

    def load(self, filename):
        if not filename.endswith(".hlibcb"):
            filename += ".hlibcb"
        if os.path.exists(filename):
            with open(filename, "rb") as f:
                self.data = pickle.load(f)
        else:
            print(f"File '{filename}' not found.")