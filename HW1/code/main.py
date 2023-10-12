import nltk as nltk
import matplotlib.pyplot as plt
from nltk.book import *

# # Task 1
# print(len(text1))
# print(len(text2))
#
# # Task 2
# print(len(set(text1)))
# print(len(set(text2)))
#
# # Task 3
# print(len(set(text1)) / len(text1))
# print(len(set(text2)) / len(text2))
#
# # Task 4
# spring_count_text1 = text1.count('spring')
# print(f"The word 'spring' appears {spring_count_text1} times in text1.")
# spring_percentage_text1 = 100 * spring_count_text1 / len(text1)
# print(f"The word 'spring' makes up {spring_percentage_text1:.2f}% of the total words in text1.\n")
#
# spring_count_text2 = text2.count('spring')
# print(f"The word 'spring' appears {spring_count_text2} times in text2.")
# spring_percentage_text2 = 100 * spring_count_text2 / len(text2)
# print(f"The word 'spring' makes up {spring_percentage_text2:.2f}% of the total words in text2.\n")
#
# # Task 5
# # Create frequency distributions for text1 and text3
# freq_dist_text1 = nltk.FreqDist(text1)
# freq_dist_text3 = nltk.FreqDist(text3)
#
# # Print the 10 most common words in each text
# print("10 most common words in text1:")
# print(freq_dist_text1.most_common(10))
# print("\n10 most common words in text3:")
# print(freq_dist_text3.most_common(10))
#
# # Generate a cumulative frequency plot for text1
# plt.figure(figsize=(12,6))
# freq_dist_text1.plot(50, cumulative=True)
# plt.show()
#
# # Task 6
# index_of_spring = text2.index("spring")
# start_of_sentence = text2.index("[" or "(" or "CHAPTER" or "VOLUME" or "EPILOGUE" or "CHAPTER")
# end_of_sentence = text2.index("." or "!" or "?" or "]" or ")")
# sentence_containing_spring = text2[start_of_sentence:end_of_sentence+1]
#
# # Task 7
# words_ending_in_ise = [word for word in text2 if word.endswith("ise")]
# words_containing_z = [word for word in text2 if "z" in word]
# words_containing_pt = [word for word in text2 if "pt" in word]
# words_titlecase = [word for word in text2 if word.istitle()]



