import csv
from split_word import split_word 
from sentimental_embedding import embedding_word, embedding_word_array, embedding_sentence, embedding_sentence_per_word
import numpy as np
from sentence_transformers import SentenceTransformer, util 
import torch
from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, 'r') as csvfile:
            # Create a CSV reader object
            csv_reader = csv.reader(csvfile)
            
            # Read the header
            header = next(csv_reader)
            

            # Read the data
            for row in csv_reader:
                data.append(row)

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return data


def array_to_latex_table(array):
    # Ensure the array is not empty
    # if not array:
    #     print("Error: Array is empty.")
    #     return

    # Determine the number of columns based on the length of the first row
    num_columns = len(array[0])

    # Begin the LaTeX table
    latex_table = "\\begin{array}{" + "c" * num_columns + "}"

    # Iterate through the array and format each row
    for row in array:
        # Join elements in the row, separated by "&", and add a newline
        latex_table += " & ".join(map(str, row)) + " \\\\"

    # End the LaTeX table
    latex_table += "\n\\end{array}"

    return latex_table




# Example usage
file_path = 'data/Text_Similarity_Dataset.csv'  # Replace with your CSV file path
data = read_csv_file(file_path)
data = data[0:29]
print(len(data))
next = 1 
counter = 0
# results_head = np.array([['Index'],['PyTorch Similarity'], ['Square Similarity']])
results_head = ['Index', 'PyTorch Similarity', 'Square Similarity']
results = []
for index in range(0, len(data)-2):
    embedding_1= model.encode(data[index], convert_to_tensor=True)
    embedding_2 = model.encode(data[index + next], convert_to_tensor=True)
    score_torch = util.pytorch_cos_sim(embedding_1, embedding_2)
    # print(data[index])
    # print("\n")
    # print(f"The pytorch score is {score_torch} \n")
    # do combined sentences and do individual and calculate shortest distance 
    comb_sentence = data[index] + data[index + next]
    score_embed_comb = embedding_sentence(comb_sentence)
    torch_similarity = score_torch[0][0].numpy()
    # print(torch_similarity)
    sentimental_similarity = float(score_embed_comb[2])
    # print(sentimental_similarity)
    counter += 1
    arr = [counter, torch_similarity, sentimental_similarity]
    results.append(arr)
results = np.array(results)
results = [results_head, results]
result_array = np.vstack(results)
print(result_array)
    
print(array_to_latex_table(result_array))

    
    
    # score_sentence_1 = embedding_sentence(data[index], len(data[index]))
    # score_sentence_2 = embedding_sentence(data[index + next], len(data[index + next]))
    # print(f"The combined sentence score is {score_embed_comb} \n")
    # print(f"The individual sentence 1 score is {score_sentence_1} \n")
    # print(f"The individual sentence 2 score is {score_sentence_2} \n")
    
    # analysis array 
    
    

    
    
    
    

    


# for word in words:
#     arr = sentiment(word)
#     arr = np.insert(arr, 0, ind)
#     ind = ind + 1
#     arr_list.append(arr)


# array = np.vstack(arr_list)
# print(array)
