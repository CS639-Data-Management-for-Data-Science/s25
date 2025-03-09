import json
import os
import pytest
import nbformat
from pathlib import Path

SOLUTIONS_DIR = os.path.join(os.getcwd(), "answers") 
NOTEBOOK_NAME = 'p3.ipynb'

# q1: 0.5, q2-q15: 0.6, q16-q20: 0.5

weights = [0.5, 0.6, 0.6, 0.6, 0.6, 
          0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6,0.6,0.6,0.6,
          0.5, 0.5, 0.5, 0.5, 0.5]

# Track total score
test_scores = {}
max_score = sum(weights)

def get_code_cells(notebook):
    """Extract all code cells from the Jupyter notebook."""
    return [cell['source'] for cell in notebook.cells if cell['cell_type'] == 'code']


@pytest.fixture
def load_notebook():
    """Load the Jupyter notebook and return the code cells."""
    with open(NOTEBOOK_NAME, 'r', encoding='utf-8') as f:
        notebook = nbformat.read(f, as_version=4)
    return get_code_cells(notebook)


def test_wget_unzip_usage(load_notebook):
    """Check that wget and unzip were used to download and extract the sample_mflix dataset."""
    notebook_code = "\n".join(load_notebook)
    #assert "!wget" in notebook_code, "wget command to download datasets not found."
    #assert "!unzip" in notebook_code, "unzip command to extract the dataset not found."


def test_imports(load_notebook):
    """Check that the required modules are imported."""
    notebook_code = "\n".join(load_notebook)
    required_imports = [ 
        "os",
        "json", 
        "elasticsearch",
    ]
    for imp in required_imports:
        assert imp in notebook_code, f"Required import '{imp}' not found."


def load_json(filename):
    file_path = os.path.join(SOLUTIONS_DIR, filename)  
    if not os.path.exists(file_path):  
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r', encoding="utf-8") as f: 
        return json.load(f)



@pytest.mark.parametrize("question", [1])
def test_client_info(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    check_keys = ["cluster_name", "status", "timed_out", "number_of_nodes", "number_of_data_nodes"]

    assert student_answer is not None, f"Question {question}: No solution found."
    
    for key in check_keys:
        assert key in student_answer, f"Question {question}: '{key}' key not found."

    test_scores[question] = weights[question - 1]




@pytest.mark.parametrize("question", [2, 3])
def test_mappings(question):
    try:
       student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"
    
    assert student_answer is not None, f"Question {question}: No solution found."
    assert "madmap" in student_answer, f"Question {question}: 'madmap' key not found."
    assert "mappings" in student_answer["madmap"], f"Question {question}: 'mappings' key not found in student_answer['madmap']"
    assert "properties" in student_answer["madmap"]["mappings"], f"Question {question}: 'properties' key not found in student_answer['madmap']['mappings']"

    if question == 2:
        entries_to_match = ["arrests", "attended", "publishedAt"]
    elif question == 3:
        entries_to_match = ["arrests", "attended", "publishedAt", "wiki"]

    for entry in entries_to_match:
        assert entry in student_answer["madmap"]["mappings"]["properties"], f"Question {question}: '{entry}' key not found in student_answer['madmap']['mappings']['properties']"

    test_scores[question] = weights[question - 1]



@pytest.mark.parametrize("question", [4])
def test_q4(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "hits" in student_answer and "max_score" in student_answer["hits"], f"Question {question}: Missing 'hits' or 'max_score' key."
    assert "hits" in student_answer["hits"], f"Question {question}: 'hits' list not found."

    assert student_answer["hits"]["total"]["value"] >= 20, f"Question {question}: Less than 20 results found."
    assert student_answer["hits"]["max_score"] >= 2.5, f"Question {question}: Max score achieved is less than 2.5."

    for entry in student_answer["hits"]["hits"]:
        assert "formattedAddress" in entry["_source"], f"Question {question}: 'formattedAddress' key missing."
        assert "University" in entry["_source"]["formattedAddress"], f"Question {question}: 'University' not found in formattedAddress."

    test_scores[question] = weights[question - 1]




@pytest.mark.parametrize("question", [5])
def test_q5(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "hits" in student_answer, f"Question {question}: 'hits' key not found."
    assert "hits" in student_answer["hits"], f"Question {question}: 'hits' list not found."

    expected_titles = [
        "Wisconsin Badgers host Alabama, anticipation builds in Madison",
        "Alabama vs. Wisconsin Odds, Best Bets: Crimson Tide Favored in Madison",
        "News: FOX\u2019s Big Noon Kickoff to visit Madison, Wisconsin on Saturday",
        "ESPN\u2019s College GameDay will not visit Madison for Wisconsin vs. Alabama",
        "Purdue football vs. Wisconsin grades: Boilers' downward spiral continues in Madison meltdown",
        "Wisconsin top-10 class of 2026 running back target to visit Madison this weekend",
    ]

    retrieved_titles = [entry["_source"]["title"] for entry in student_answer["hits"]["hits"] if "_source" in entry and "title" in entry["_source"]]

    assert len(retrieved_titles) >= 10, f"Question {question}: Expected at least 10 titles, but found {len(retrieved_titles)}."
    assert any(title in expected_titles for title in retrieved_titles), f"Question {question}: No expected titles found in results."

    test_scores[question] = weights[question - 1]




@pytest.mark.parametrize("question", [6])
def test_q6(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "hits" in student_answer and "hits" in student_answer["hits"], f"Question {question}: Missing 'hits' key."
    
    total_hits = student_answer["hits"]["total"]["value"]
    assert total_hits >= 25, f"Question {question}: Expected at least 30 results, but found {total_hits}."
    
    for entry in student_answer["hits"]["hits"]:
        assert "_source" in entry, f"Question {question}: '_source' key missing in one of the hits."
        source_data = entry["_source"]

        found_phrase = any("Wisconsin Badgers" in source_data[field] for field in ["title", "description", "content"] if field in source_data)
        assert found_phrase, f"Question {question}: Expected phrase 'Wisconsin Badgers' not found in any relevant field."

    test_scores[question] = weights[question - 1]



@pytest.mark.parametrize("question", [7])
def test_q7(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "hits" in student_answer and "hits" in student_answer["hits"], f"Question {question}: Missing 'hits' key."
    
    total_hits = student_answer["hits"]["total"]["value"]
    assert total_hits > 0, f"Question {question}: Expected results, but found {total_hits}."

    for entry in student_answer["hits"]["hits"]:
        assert "_source" in entry, f"Question {question}: '_source' key missing in one of the hits."
        source_data = entry["_source"]

        assert "formattedAddress" in source_data, f"Question {question}: Missing 'formattedAddress' key."
        assert "name" in source_data, f"Question {question}: Missing 'name' key."

        assert "Madison" not in source_data["formattedAddress"], (
            f"Question {question}: Found 'Madison' in address {source_data['formattedAddress']}."
        )

    test_scores[question] = weights[question - 1]


@pytest.mark.parametrize("question", [8])
def test_q8(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "hits" in student_answer, f"Question {question}: 'hits' key not found."
    assert "hits" in student_answer["hits"], f"Question {question}: 'hits' list not found in 'hits'."
    
    assert any(hit["_score"] > 6 for hit in student_answer["hits"]["hits"]), \
        f"Question {question}: No document found with _score higher than 6."



@pytest.mark.parametrize("question", [9])
def test_q9(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "wiki" in student_answer, f"Question {question}: 'wiki' key not found."
    
    assert isinstance(student_answer["wiki"], list), f"Question {question}: 'wiki' should be a list."
    assert all(isinstance(item, str) for item in student_answer["wiki"]), f"Question {question}: Each item in 'wiki' should be a string."

    assert any("<em>rivalry</em>" in item for item in student_answer["wiki"]), \
        f"Question {question}: No highlighted '<em>rivalry</em>' found in wiki highlights."


@pytest.mark.parametrize("question", [10])
def test_q10(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert student_answer is not None, f"Question {question}: No solution found."
    assert "hits" in student_answer, f"Question {question}: 'hits' key not found."
    assert "hits" in student_answer["hits"], f"Question {question}: 'hits' inside 'hits' key not found."

    hits = student_answer["hits"]["hits"]
    assert isinstance(hits, list), f"Question {question}: 'hits' should be a list."
    
    required_fields = ["source", "title", "publishedAt"]
    for hit in hits:
        assert "_source" in hit, f"Question {question}: '_source' key missing in one of the hits."
        source = hit["_source"]

        for field in required_fields:
            assert field in source, f"Question {question}: '{field}' missing in '_source'."

        assert source["source"]["name"] == "NASA", f"Question {question}: 'source.name' must be 'NASA', but found {source['source']['name']}."
        
 



@pytest.mark.parametrize("question", [12])
def test_q12(question):
    try:
        student_answer = load_json(f"{SOLUTIONS_DIR}/q{question}.json")
    except Exception:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert isinstance(student_answer, list), f"Question {question}: Expected a list, but got {type(student_answer)}."

    expected_top_sources = [
        {"key": "Milwaukee Journal Sentinel", "doc_count": 22},
        {"key": "Yahoo Entertainment", "doc_count": 19},
        {"key": "Fox Sports", "doc_count": 18},
        {"key": "USA Today", "doc_count": 18},
        {"key": "Forbes", "doc_count": 15},
        {"key": "CBS Sports", "doc_count": 9},
        {"key": "Newsweek", "doc_count": 8},
        {"key": "ESPN", "doc_count": 6},
        {"key": "Scientific American", "doc_count": 6},
        {"key": "Tuscaloosa News", "doc_count": 6}
    ]
    
    assert len(student_answer) == 10, f"Question {question}: Expected 10 sources, but got {len(student_answer)}."

    for expected, actual in zip(expected_top_sources, student_answer):
        assert actual["key"] == expected["key"], f"Question {question}: Source mismatch. Expected '{expected['key']}', but got '{actual['key']}'."
        assert actual["doc_count"] == expected["doc_count"], f"Question {question}: Doc count mismatch for '{expected['key']}'. Expected {expected['doc_count']}, but got {actual['doc_count']}."

        
        

@pytest.mark.parametrize("question, expected_value", [(11, 1671.0), (13, 307), (14, 64), (15, 47736.84210526316)])
def test_numeric_values(question, expected_value):
    try:
        student_answer = load_json(f"{SOLUTIONS_DIR}/q{question}.json")
    except Exception:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    assert isinstance(student_answer, (int, float)), f"Question {question}: Expected a number, but got {type(student_answer)}."

    assert student_answer == expected_value, f"Question {question}: Expected {expected_value}, but got {student_answer}."



@pytest.mark.parametrize("question", [19])
def test_q19(question):
    try:
        student_answer = load_json(f"q{question}.json")
    except Exception as e:
        assert False, f"Question {question} json not found at {SOLUTIONS_DIR}/q{question}.json"

    required_keys = [
        "coordinates", "formattedAddress", "name", "place_id",
        "place_type", "priceLevel", "_id", "_index", "_score"
    ]

    assert student_answer is not None, f"Question {question}: No solution found."

    for key in required_keys:
        assert key in student_answer, f"Question {question}: '{key}' key not found."

    assert student_answer["priceLevel"] == ["PRICE_LEVEL_VERY_EXPENSIVE"], (
        f"Question {question}: 'priceLevel' should be 'PRICE_LEVEL_VERY_EXPENSIVE', but got {student_answer['priceLevel']}."
    )

    assert student_answer["_index"] == "places_madison", (
        f"Question {question}: '_index' should be 'places_madison', but got {student_answer['_index']}."
    )



@pytest.mark.parametrize("question",  [16,17,18,20])
def test_imgs_exist(question):
    if os.path.exists(f"{SOLUTIONS_DIR}/q{question}.png"):
        assert True, f"Question {question}: Image found."
        test_scores[question] = weights[question - 1]
    else:
        assert False, f"Question {question}: Image not found."
