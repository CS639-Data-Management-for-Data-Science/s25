import nbformat
from nbconvert import PythonExporter
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
import pickle
import argparse
import os
import subprocess
from pandas.testing import assert_frame_equal, assert_index_equal

def unzip_and_store(zip_path, temp_dir):
  if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)
  subprocess.run(["unzip", "-o", zip_path, "-d", temp_dir])
  

def parse_pickle(path_to_pickle):
  with open(path_to_pickle, 'rb') as f:
    return pickle.load(f)
  

def assert_frame_equal_extended_diff(df1, df2, out, question_tag, question_number):
  try:
    assert_frame_equal(df1, df2,  
                       check_freq=False, 
                       check_index_type=False, 
                       check_column_type=False,
                       check_like=True, 
                       check_dtype=False)
    out.write(f"Question {question_number}: 2.5/2.5 points\n")
    return 2.5
  except AssertionError as e:
    # if this was a shape or index/col error, then re-raise
    if (df1.astype(str)).equals(df2.astype(str)):
      out.write(f"Question {question_number}: 2.5/2.5 points\n")
      return 2.5
      
    try:
        pd.testing.assert_index_equal(df1.index, df2.index)
        pd.testing.assert_index_equal(df1.columns, df2.columns)
    except AssertionError:
        out.write(f"\nShape or index/column error for {question_tag}:\n")
        out.write(e)
        out.write("\n")
      
    # if not, we have a value error 
    diff = df1 != df2
    diffcols = diff.any(axis=0)
    diffrows = diff.any(axis=1)
    cmp = pd.concat(
            {'left': df1.loc[diffrows, diffcols], 'right': df2.loc[diffrows, diffcols]},
            names=['dataframe'],
            axis=1)
    out.write(f'\nValue error for {question_tag}:\n\nDifferences:\n{cmp}\n')
    return 0
    

def grade_notebook(notebook_path):
    with open(notebook_path, 'r') as f:
        notebook = nbformat.read(f, as_version=4)

    with open('test_output.txt', 'w') as out:
      total_score = 0 
      question_tags_seen = []

      for cell in notebook.cells:

        if cell.cell_type == 'code':
          # print(cell.source)
          if "create_engine" in cell.source and ".connect()" in cell.source: 
            out.write("Connection to database established: 2.5 points\n")
            total_score += 2.5

          elif "pd.read_sql" in cell.source:
            # Find the comment #qXX in the cell.source
            if cell.source[0] == "#": 
              # print(cell.source)
              question_tag = cell.source.split("#")[1].split("\n")[0]
              # print(f"Found question tag: {question_tag}")
            else:
              out.write(f"[!] Missing question number comment identifier on first line of the cell containing SQL query: {cell.source} \n\n")
              continue

            if question_tag in question_tags_seen: # Make sure no duplicate questions are graded 
              continue
            else:
              question_tags_seen.append(question_tag)
              question_number = int(question_tag[1:])
            
            # Grading
            if 'outputs' in cell: # Check whether the notebook has been executed
              try:
                with open(question_tag + ".pkl", 'rb') as ao:
                  actual_output = pickle.load(ao)
              except FileNotFoundError:
                out.write(f"[!] Missing/Incorrect pickle file name for question {question_number}\n")
                print(f"Found #q{question_number} tag but couldn't open student's pkl. Continuing...")
                continue
              
              try:
                with open(f"answers/answers/pkls/p{str(question_number)}.pkl", 'rb') as eo:
                  expected_output = pickle.load(eo)
              except FileNotFoundError:
                out.write(f"[!!] Could not open answers/q{question_number}.pkl")
                print(f"[!] Could not open answers/q{question_number}.pkl. Continuing")
                continue
            
              score_val = assert_frame_equal_extended_diff(actual_output, 
                                                              expected_output,
                                                              out, 
                                                              question_tag, 
                                                              question_number)
            
              if int(question_number) == 23 and score_val == 0: ## Q23 autograder fix
                  try:
                    with open(f"answers/answers/pkls/p23-s2.pkl", 'rb') as eo:
                      expected_output_2 = pickle.load(eo)
                    total_score += assert_frame_equal_extended_diff(actual_output, 
                                                              expected_output_2,
                                                              out, 
                                                              question_tag, 
                                                              question_number)
                  except FileNotFoundError:
                    out.write(f"[!!] Could not open answers/q{question_number}.pkl")
                    print(f"[!] Could not open answers/q{question_number}.pkl. Continuing")
                    continue
              
              total_score += score_val


            else:
              out.write(f"Question {question_number}: 0 points (NB did not have an output)\n")
            print("Processed", question_tag)
      out.write(f"---------------------------------------------------------------\n Total Score: {total_score}/{2.5 * (35 + 1)}\n---------------------------------------------------------------\n")
      print("-----------------------------")
      print(f"Total Score: {total_score}/{2.5 * (35 + 1)}\n-----------------------------\nRun `cat test_output.txt` for individual question-wise results :)")

if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("-nb", "--notebook_path", type=str, default="p1.ipynb")
    args = args.parse_args()

    unzip_and_store("answers.zip", "answers")
    score = grade_notebook(args.notebook_path)
