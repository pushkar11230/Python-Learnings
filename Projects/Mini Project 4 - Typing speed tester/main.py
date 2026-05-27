import time
import random
import difflib

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A journey of a thousand miles begins with a single step.",
    "If you remember me, then I don't care if everyone else forgets.",
    "You have the power to heal your life, and you need to know that.", 
    "We may encouter many defeats, but we must not be defeated."
]

def typing_test():
    # Picking up a random sentence from sentences list
    test_sentence = random.choice(sentences)

    # Instructions
    print("\nType the following sentence as fast as you can:")
    print(test_sentence)
    input("Press enter when you are ready...")

    # Measureing start time
    start_time = time.time()

    # User type sentence
    user_input = input("\nStart typing:\n")

    # Measuring end time
    end_time = time.time()

    # Total time taken to type the sentence
    time_taken = end_time - start_time

    # Counting the words
    word_count = len(test_sentence.split(" "))

    # Calculate words per minute
    wpm = (word_count / time_taken) * 60

    # # Accuracy measuring:
    # correct_characters = 0

    # # Compare both strings character by character
    # for i in range(min(len(test_sentence), len(user_input))):
    #     if test_sentence[i] == user_input[i]:
    #         correct_characters += 1

    # # Accuracy formula
    # accuracy = (correct_characters / len(test_sentence)) * 100


    # --------Better Accuracy System------------
    accuracy = difflib.SequenceMatcher(
        None,
        test_sentence,
        user_input
    ).ratio() * 100


    print("\nResults:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {word_count} words")
    print(f"Typing speed: {wpm:.2f} WPM")
    print(f"Accuracy: {accuracy:.2f}%")


typing_test()

