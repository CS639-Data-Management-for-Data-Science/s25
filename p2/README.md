# P2 (8% of grade): MongoDB

Github Classroom Link: [https://classroom.github.com/a/wDvKEbCR) (group assignment)

## Clarifications/fixes
[2/26 8:48pm] Students should download the two geojson files mentioned in Section 4.

## :telescope: Overview

In this project, you'll perform basic and advanced analysis of the `sample_mflix` database using MongoDB Query Language (MQL).

Learning objectives:
* Set up MongoDB using Docker on your Google VM.
* Explore basic NoSQL database operations operations using MongoDB Query Language (MQL).
* Write and execute MQL queries to extract meaningful insights on `sample_mflix` dataset.

Before starting, please review the [general project directions](../projects.md).

:warning: You will be answering 34 questions. **We recommend getting started early with the project.**

:warning: Please use Piazza to post (public/private) any questions regarding this project, as e-mails will NOT be answered. If you need to include your code to get help, please make a **private** post.

## :hammer_and_wrench: Setting up MongoDB using Docker

- In your VM, pull the official MongoDB Docker image:

```bash
docker pull mongo
```
**Note:** If you are still using `sudo` to run `docker` commands, please follow the steps [here](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user) (don't go beyond the "Manage Docker as a non-root user" section).

- Create and run a MongoDB container using the following command:

```bash
docker run --name <container-name> -d -p 127.0.0.1:27017:27017 mongo
```

- Verify MongoDB is running:

```bash
docker ps
```

## :nut_and_bolt: Setting up `jupyter`, `pymongo`, and other libraries

- If you haven't already installed these packages on your VM, make sure to complete the below installations:

```bash
pip3 install jupyter pandas nbformat nbconvert
```

- Now, install `pymongo` so we can interact with MongoDB via Python.

```bash
pip3 install pymongo
```

- In addition, install `geopandas` and `matplotlib`--we'll ue the two to interact with and visualize GeoJSON data.

```bash
pip3 install geopandas matplotlib
```

- Create a new directory to keep track of your p2 files and `cd` into it:

```bash
mkdir p2
cd p2/
```

- Then, launch `jupyter` using the below command, and make note of the auto-generated URL.

```bash
jupyter notebook
```

- To access the `jupyter` session on your laptop, you must establish an `ssh` tunnel. Open a new terminal or powershell tab, then use either of the below commands to establish your tunnel.

```bash
ssh <USER>@IP -L localhost:8888:localhost:8888
```
or
```bash
gcloud compute ssh <VM_NAME> -- -L localhost:8888:localhost:8888
```

:point_right: Double-check that the second port matches the port in the URL.

:point_right: If port 8888 is occupied on your laptop, you can change the first port (source port) in the above command to a different port number.

- Now, open the jupyter URL in your browser, and create a new notebook file (File > New > Notebook). Make sure to save it as `p2.ipynb`.

## :floppy_disk: Writing code in `p2.ipynb` to set up ```sample_mflix``` database 

1. Inside your notebook, use the appropriate `bash` command to unzip the ```sample_mflixz.zip``` dataset file. **Note:** During the lecture, we covered how to run bash command from inside notebook file. If required, please review lecture demo code.

### Loading ```sample_mflix``` database

1. In a new cell, make sure to type in the necessary `import` statements.
2. Following that, create a new cell to establish connection to your `mongodb` server using `MongoClient` from the `pymongo` module.
3. Then load the content of each `JSON` file into the database.
   * Your database table name must match with each `JSON` file name (including the case).
   * There is an efficient way to load all the `JSON` files without having to type each `JSON` file's name.
      * If you are not familiar with the `os` module `listdir` function, please look it up.
      * You can use a combination of string methods and the `os` module to load all `JSON` files without having to type individual files names. 
   * Please use `bson.json_util.loads()` to load the JSON files (and NOT the `json` module).

## :blue_book: Section 1: Basic MQL operations (20 questions)
:point_right: Each question in this section is worth 0.1 points.

:warning: **Requirements (applies to all subsequent questions)**:
- Each solution cell should be marked using the appropriate question number as a comment. For example, at the beginning of the cell answering question 1, you should have this comment: "#q1".

- Each question's resultant data must be stored into a file called `q<N>.pkl`, where `N` refers to the question number. Save all the files in a folder called `answers/`. For example, store q1's results using the below code:

```
q1 = list(db.movies.find ...)
with open('answers/q1.pkl', 'wb') as f:
   pickle.dump(q1, f)
```

- Please ensure that your output is saved in a `list`, `dict` or `numeric` format (as appropriate); that is, do not save `PyCursor` objects.

- Make sure to go back to the cell containing import statements and include `import pickle` (and other necessary libraries, as needed).

- For each question, unless explicitly stated, you should output all fields of the collection(s) you're working with. For example, if you're asked to find the first movie released in year 2021, you should display all data/fields for that movie in the `movies` collection, and not just the title.

For your personal verification, you can display the output of the your queries.

---

#### Q1: Find the first movie in the `movies` collection.

#### Q2: Find all movies directed by "Christopher Nolan".

#### Q3: Find the first 5 users in the users collection.

#### Q4: Find the first movie with an IMDb rating greater than 9.

#### Q5: Count the number of movies in the movies collection.
- Your output should only be the total count (a numeric value).

#### Q6: Count the number of movies released after the year 2000.
- Your output should only be the total count (a numeric value).
- Please use the `year` field, not `released`.

#### Q7: Count the number of movies in the "Comedy" genre.
- Your output should only be the total count (a numeric value).

#### Q8: Count the number of comments made by the user "Taylor Hill".
- Your output should only be the total count (a numeric value).

#### Q9: Count the number of movies with a runtime greater than 120 minutes.
- Your output should only be the total count (a numeric value).

#### Q10: Find all movies released in year 2015.
- Please use the `year` field, not `released`.
- Your output should only include one field:
   - `title`: movie title
- Sort in ascending order of `title`.

#### Q11: Find the top 5 most recent comments.

#### Q12: Count the number of movies with both "Action" and "Adventure" as genres.

#### Q13: Find all movies with an IMDb rating between 9 and 10.
- The range is inclusive; that is, your output should include movies with ratings exactly 9 or 10 too.
- Your output should only include four fields:
   - `title`: movie title
   - `imdb.rating`: IMDb rating
   - `genres`: genre(s)
   - `year`: release year

#### Q14: Count the number of movies with exactly 3 directors.
- Your output should only be the total count (a numeric value).
- Note: You might have to check that the `directors` field exists.

#### Q15: Count the number of movies with at least 3 directors.
- Your output should only be the total count (a numeric value).
- Note: You might have to check that the `directors` field exists.

#### Q16: Find the total number of comments made on movies released in 2010.
- Your output should only be the total count (a numeric value).
- Please use the `year` field, not `released`.

#### Q17: Find all unique users who have commented on "Action" movies.
- Your output should be a `list` of user names (not `dict`), sorted in ascending order.

#### Q18: Find all comments made on or after August 13th, 2018.
- You will need to import the `datetime` module.

#### Q19: Count the total number of comments made on movies directed by "Steven Spielberg".
- Your output should only be the total count (a numeric value).

#### Q20: Find the 10 most recent movies with an IMDb rating greater than 9.0.
- Please use the `released` field, not `year`.
- Your output should only include three fields:
   - `title`: movie title
   - `released`: date of release
   - `imdb.rating`: IMDb rating
- Sort in decreasing order of `released`. 


## :green_book: Section 2: Medium MQL operations (5 questions)
:point_right: Each question in this section is worth 0.2 points.

#### Q21: Find the total number of movies that have no comments.
- Your output should only be the total count (a numeric value).

#### Q22: Find the total number of movies where the title starts with "The".
- Your output should only be the total count (a numeric value).

#### Q23: Find the average IMDb rating of all "Action" movies.
- Your output should only include one field (a new one created by you):
   - `average_rating`
- Ensure that the `average_rating` is rounded to two decimal places.

#### Q24: Find the top 5 users who have made the most comments.
- Your output should only include two fields:
   - `_id`: user name
   - `total_comments`: number of total comments for given user
- Sort in decreasing order of `total_comments`.
- For tie-breaker, use ascending order of `_id`.

#### Q25: Find the 5 most commented movies in the database.
- Your output should only include two fields:
   - `_id`: movie ID
   - `total_comments`: number of total comments for given movie
- Sort in decreasing order of `total_comments`.
- For tie-breaker, use ascending order of `movie.title`.
- If you're still failing the autograder because of sorting issues, try performing `$group` _before_ `$lookup` in your pipeline.

## :orange_book: Section 3: Hard MQL commands (6 questions)
:point_right: Each question in this section is worth 0.3 points.

#### Q26: Find the average runtime of all movies in the "Sci-Fi" genre.
- Your output should only include one field (a new one created by you):
   - `average_runtime`
- Ensure that the `average_runtime` is rounded to two decimal places.

#### Q27: Find the top 3 directors by the number of movies they directed.
- Your output should only include two fields:
   - `_id`: director name
   - `count`: total number of movies directed by given director
- Sort in decreasing order of `count`.
- For tie-breaker, use ascending order of `_id`.

#### Q28: Find the top 5 most active users (based on the number of comments).
- Your output should only include two fields:
   - `email`: user email
   - `comment_count`: total number of comments by given user
- Sort in descending order of `comment_count`.

#### Q29: Find the average IMDb rating for each genre and list the top 5 genres with the highest average rating.
- Your output should only include two fields:
   -  `_id`: genre name
   - `average_rating`: average IMDb rating for given genre
- Sort in descending order of `average_rating`.
- Ensure that the `average_rating` is rounded to two decimal places.

#### Q30: Find all users who have commented on both "Action" and "Drama" movies.
- Your output should only include one field:
   - `_id`: user name
- Sort in ascending order of `_id`.
- The following operators might be helpful: [`$addToSet`](https://www.mongodb.com/docs/manual/reference/operator/update/addToSet/), [`$cond`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/cond/), and [`in`](https://www.mongodb.com/docs/manual/reference/operator/aggregation/in/).

#### Q31: Find the user who commented on the most distinct movies (i.e., most distinct `movie_ids`).
- Your output should include two fields for the user:
   -  `_id`: user name
   - `unique_movies`: total number of (distinct) movies given user commented on


## :closed_book: Section 4: GeoJSON (3 questions)
:point_right: Each question in this section is worth 0.4 points.

:point_right: The autograder for this section only checks for existence of image file(s). We will manually review the images and assign grades.

:warning: **Requirements (applies to all subsequent questions)**:
- Your output should only be an image/plot.
- Please save the image in the same folder as your notebook, and label it `q<N>.png`, where `N` refers to the question number.
- You can use the below function to create the plots.

```python
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

# Function to plot theaters on a map
def plot_theaters(theaters, map_type, filename):
    assert map_type in ['wi', 'madison']
    assert filename in ['q32', 'q33', 'q34']
    
    # Convert theater coordinates to a GeoDataFrame
    gdf = gpd.GeoDataFrame(theaters, geometry=gpd.points_from_xy(
        [theater['location']['geo']['coordinates'][0] for theater in theaters],
        [theater['location']['geo']['coordinates'][1] for theater in theaters]
    ))

    world = gpd.read_file("wi_limits.geojson")
    if map_type == 'madison':
        world = gpd.read_file("madison_limits.geojson")
    gdf = gdf.set_crs(world.crs)
    
    # Plot
    ax = world.plot(figsize=(10, 6), color='lightgray', edgecolor='black')
    gdf.plot(ax=ax, marker='o', color='red', markersize=5)
    plt.title("Theater Locations")

    plt.grid(True)
    plt.savefig(f'{filename}.png')
    plt.show()
```

- You're provided with two GeoJSON files: [Madison city limits](https://data-cityofmadison.opendata.arcgis.com/datasets/db89adb17d414649a71c0f29ea73e5bf_6/explore?location=43.084327%2C-89.409000%2C11.71) and [WI boundaries](https://data-wisdot.opendata.arcgis.com/datasets/5973013e60d34693b849af053918a5a3_0/explore?location=44.501257%2C-89.836800%2C7.44). Double-check that they're present in your repository.

---

#### Q32: Find all theaters located in Wisconsin (WI) and plot them on a map of WI.

#### Q33: Find the top 2 theaters nearest to the Peninsula State Park and plot them on a map of WI.
- Peninsula State Park coordinates: `(45.15602, -87.22109)` (latitute, longitude).
   - When specifying coordinates for query, list the longitude first and then latitude.

#### Q34: Find theaters within 10 miles of the UW-Madison and plot them on a map of Madison.
- UW-Madison coordinates: `(43.07540, -89.40816)` (latitute, longitude).
   - When specifying coordinates for query, list the longitude first and then latitude.


## :outbox_tray: Submission

- GitHub Classroom will automatically select your last pushed commit _before the deadline_ as your submission.
- **Technical issues within 36 hours of the deadline will not be considered as an excuse for late submission.**
- The structure of the required files for your submissions is as follows:
```
p2-<your_team_name>
|--- README.md (list names and e-mail IDs of team members at the top)
|--- p2.ipynb
|--- answers
     |--- q1.pkl
     .
     .
     .
     |--- q31.pkl
|--- q32.png
|--- q33.png
|--- q34.png
```
- It's OK to have the starter files (e.g. `sample_mflix.zip`, etc.) present too.

## :trophy: Testing
- To test your code, put the `autograder.py' and `conftest.py' in the same folder as your `p2.ipynb' and `answers' folder and run the command
```bash
pytest --no-header -vv autograder.py
```

- Just because the autograder passes doesn't mean you'll get full points—we will still review your code manually.

### Point breakdown
Breakdown of total 6 points is as follows: 
- Q1-20: 0.1 points each
- Q21-25: 0.2 points each
- Q26-31: 0.3 points each
- Q32-34: 0.4 points each
