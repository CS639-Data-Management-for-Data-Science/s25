# P1 (8% of grade): SQL Analysis of the Chinook Music Store Dataset

## Clarifications / fixes

-[2/4 2:40pm] Github Classroom join link updated. Students who already created teams, please use the following link: https://classroom.github.com/a/qtUnXczB
- [2/14 12:30pm] Please complete this Github Classroom form (same link from Canvas announcement): https://forms.gle/dSxGuMnGRTd4791L6
- [2/14 12:30pm] Added github repo file hierarchy for project submission

## Parter policy for this assignment

We do accept partner work on this project. If you are in a team (max two people) to finish this assignment, only one of the team members should submit their assignment. **The submitted repo should have a README file that write ALL the team members' names right at the top of the file**.

## Overview

In this project, you'll perform basic and advanced analysis of the Chinook database using SQL queries and functions.

Learning objectives:
* setup a docker container with mysql server
* write basic SQL queries for data retrieval
* perform complex joins across multiple tables
* group and aggregate data using SQL functions
* utilize window functions for advanced analysis

Before starting, please review the [general project directions](../projects.md).

You will be answering 35 questions. **We recommend getting started with the project early.**

## Setting up MySQL using Docker

**WARNING:** **DO NOT** forget to stop and remove the `docker` container which we are using during lecture for "IMDB dataset" analysis. Running both containers simultaneously will make your VM terribly slow. 

For this project, we'll be using the `mysql` image from [dockerhub](https://hub.docker.com/search?q=mysql). You can `pull` the `mysql` image using the below command:

```bash
docker pull mysql
```
**Note:** if you are still using `sudo` to run `docker` commands, please follow the steps here:
https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user
(don't go beyond the "Manage Docker as a non-root user" section).

Then, launch a docker container running MySQL server using this command:

```bash
docker run --name <container-name> -d -p 127.0.0.1:3306:3306 -e MYSQL_DATABASE=Chinook -e MYSQL_ROOT_PASSWORD=123456 mysql
```

Now start a new program (`bash`) in the existing docker container using the below docker command:

```bash
docker exec -it <container-name> bash
```
You can use this session for your experimentation of the database.

## Setting up `jupyter` on your VM

In a new terminal / powershell window, open another ssh session to your VM. Create a new directory (*in your home directory*) to keep track of your p1 files (of course don't forget to `cd` into it). Feel free to accept [github classroom invite](https://classroom.github.com/a/qtUnXczB), clone your repository and directory used that directory instead.

If you haven't already installed these packages on your VM, make sure to complete the below installations:
```bash
sudo apt-get update
sudo apt-get install python3-pip wget unzip
```
```bash
sudo pip3 install jupyter
pip3 install SQLAlchemy mysql-connector-python pandas nbformat nbconvert
```

Then, launch `jupyter` using the below command

```bash
jupyter notebook
```

To access the `jupyter` session on your laptop, you must establish an `ssh` tunnel. Open a new terminal or powershell tab, then use the below command to establish your tunnel:

```bash
ssh <USER>@IP -L localhost:8888:localhost:8888
```
If port 8888 is occupied on your laptop, you can change the first port (source port) in the above command to a different port number.

Then, create a new Notebook file (File > New > Notebook) and make sure to save it as `p1.ipynb`.

## Writing code in `p1.ipynb` to set up ```Chinook``` database 

1. Inside your notebook, use the appropriate `bash` command to remove `Chinook.zip` file.
   - **Note:** During the lecture, we covered how to run bash command from inside notebook file. If required, please review lecture demo code.
   - When you run this cell for the first time, it'll show an error "No such file or directory".
   - But this will come in handy when you have to do "Restart Kernel and Run All Cells...". 
2. Inside your notebook, use the appropriate `bash` command to remove all files that end with `.csv`.
3. Inside your notebook, use the appropriate `bash` command to download zip file ```Chinook``` dataset. For the URL part, you should be using the raw URL from github: `https://github.com/CS639-Data-Management-for-Data-Science/s25/raw/main/p1/Chinook.zip`.
4. Inside your notebook, use the appropriate `bash` command to unzip the zip file.
6. **IMPORTANT NOTE**: Do not manually download and unzip the dataset and do not ignore the steps 1 and 2 (you'll end up with multiple copies of the dataset, thereby wasting your disk space!)

### Loading ```Chinook``` database

1. In a new cell, make sure to type in the necessary `import` statements.
2. Following that, create a new cell to establish connection to your `mysql-server` using `create_engine` function from `sqlalchemy` module.
3. Then use load the content of each `csv` file into the database.
   * **IMPORTANT NOTE**: Your database table name must match with each csv file name (including the case).
   * There is an efficient way to load all the csv files without having to type each csv file's name.
   * If you are not familiar with the `os` module `listdir` function, please look it up.
   * You can use a combination of string methods and the `os` module to load all csv files without having to type individual files names.
  
## Running the Autograder
Download `autograder.py` and `answers.zip`, in the same dir as your solution notebook. 

Then run:
> python3 autograder.py

If your notebook is not named p1.ipynb, you can run:
> python3 autograder.py -nb `<YOUR-NOTEBOOK-NAME>`

## Section 1: Basic SQL commands (14 questions)

You are a data analyst in the Chinook company who has just been asked to conduct a full analysis of sales data of the artist named "Queen" in your database. The company needs to understand how well a specific artist is performing by reviewing the tracks sold, the total revenue generated, and customer information related to purchases. Your final goal is to present a summary of sales and customer details for that artist.

**Requirement:** Use subquery to answer the questions in section 1. We'll have an entire section dedicated to joins.

### Part 1: Analysis of the artist "Queen"

We would recommend you to explore all the tables by using appropriate SQL queries to display the corresponding table rows. Also, to make your notebook readable, we recommend copy/pasting the questions into mark down cells above your solution cell. You can use `####` mark down syntax to highlight each question.

**Requirement**: Each solution cell should be marked using the appropriate question number as a comment. For example, at the beginning of the cell answering question 1, you should have this comment: "#q1".

#### Q1: Retrieve all information about the artist "Queen" from the Artist table.

Each question's resultant `pandas DataFrame` must be stored into a file called `q\<N\>.pkl`, where `N` refers to the question number. For example, store q1's results using the below code:

```
q1_df = pd.read_sql(...)
q1_df.to_pickle("q1.pkl")
```
Make sure to go back to the cell containing import statements and include `import pickle`.

For your personal verification, you can display the output of the `pandas DataFrame` as well.

#### Q2: What are all the albums released by the artist "Queen"?

Your SQL query answering this question should be self-sufficient - that is, you should not be hardcoding the `ArtistId` that you determined from the previous question. **Harcoding will make you lose points during manual TA review**.

**Requirement:** Use subquery to answer this question and other questions in section 1. We'll have an entire section dedicated to joins.

#### Q3: What are all the tracks released by the artist "Queen"? 

Again, we expect your SQL query to be self-sufficient. **Do not hardcode** any of the identifiers. If you hardcoded the `ArtistID` for the previous question, now would be the time for you to go back and fix it. **Harcoding will make you lose points during manual TA review**.

**Requirement:** Use subquery to answer this question and other questions in section 1. We'll have an entire section dedicated to joins.

#### Q4: How many tracks released by "Queen" were composed or co-composed by "Queen"?

**Requirement:** Your result should have count column named as `TotalQueenTracks`

#### Q5: Who are all the composers of tracks by the artist "Queen"?

**Requirement:** Your result should only include unique composer names.

#### Q6: Which are the top 5 longest tracks by the artist "Queen"?

#### Q7: What are all the tracks by the artist "Queen" that are sized smaller than 6MB?

1000000 bytes = 1 MB

Wasn't it a pain to read the relevant results from the last two queries? How about we make this data more human readable for the next question?

#### Q8: Generate human-readable details about all tracks released by "Queen".

**Requirement:** Other than track names, your result should have two columns named `DurationMinutes` and `FileSize` in MB.

### Part 2: Customer and employee analysis

Let's now explore the customers to see if there is some trend.

#### Q9: Who are all the customers from USA?

**Requirement:** Your result should include `CustomerId`, `FirstName`, `LastName`, and `State` information for the customers. The rows should be ordered using ascending order of the `State` names.

#### Q10: Which invoices correspond to transactions costing greater than $20?

#### Q11: Which invoices were issued in the year 2021?

#### Q12: What was the total expenditure of "Eduardo Martins"?

**Requirement:** It is acceptable to hardcode first and the last name here. But it is not acceptable to hardcode customer id.

#### Q13: Which customers from the USA do not have any specified company information?

#### Q14: Who are all the Canadian employess?

## Section 2: In-depth analysis of Queen data with `JOIN` clauses (10 questions)

Now that you have the basic information and understanding of the database, you should begin some real analysis that can uncover interesting information across tables. In SQL, we link tables using the `JOIN` command.

#### Q15: Retrieve the names of all customers along with their corresponding invoice totals.

**Requirements:** 
* You must use `JOIN` to solve this question and the other questions in this section.
* Your results should be ordered by `LastName` (A through Z).
* Your results should also be ordered based on increasing order of the `Total` column.

#### Q16: Which customers purchased the tracks by "Queen"?

**Requirements:** 
* Your result should include `CustomerId`, `FirstName`, and `LastName` of customers who have purchased tracks by Queen.
* Your results should only include unique `CustomerID`.
* Your results should be ordered by `CustomerID`.
* You may use subquery for the Queen's tracks retrieval part given that you wrote that for Q3, but you must use `JOIN` for answering the rest of the question.

#### Q17: Retrieve Invoice Details for the tracks by "Queen".

**Requirements:** 
* Your results must include the `InvoiceId`, `InvoiceDate`, `BillingCountry`, and `Total` columns for invoices that include at least one track by Queen.
* Your results should only include unique `InvoiceId`.
* Your results should be ordered by `InvoiceId`.

#### Q18: Retrieve tracks details by "Queen" along with the corresponding album titles and media types.

**Requirements:** 
* Your results must include `TrackId`, track's name `TrackName`, album's title `AlbumTitle`, and media type's name `MediaTypeName` for all tracks by Queen.
* Your results should be ordered by `TrackId`.

#### Q19: Find genres of tracks by "Queen".

**Requirements:** 
* Your results must include `TrackId`, track's name `TrackName`, and genre's name `GenreName` for all tracks by Queen.
* Your results should be ordered by `TrackId`.

#### Q20: Retrieve invoice details for customers from the USA who purchased tracks by "Queen".

**Requirements:** 
* Your results must include the `InvoiceId`, `InvoiceDate`, `BillingCity`, `BillingState`, and `CustomerId` for the invoices of customers from the USA who have purchased tracks by Queen.
* Your results should only include unique `InvoiceId`.
* Your results should be ordered by `InvoiceId`.

#### Q21: Find all playlists that contain tracks by "Queen".

**Requirements:** 
* Your results must include the playlist name `PlaylistName`.
* Your results should also be ordered based on ascending order of `PlaylistName`.

#### Q22: List all the employees (sales agents) who supported customers that purchased tracks by "Queen." 

**Requirements:** 
* Your results must include the `EmployeeId`, `FirstName`, and `LastName`, of the employess (salees agents) who supported customers that purchased tracks by Queen.
* Your results should only include unique `EmployeeId`.
* Your results should be ordered by `EmployeeId`.

#### Q23: Retrieve a list of all albums along with the names of their artists, including albums that don't have any artist information.

**Requirements:** 
* **IMPORTANT NOTE:** You may **NOT** use a regular join to answer this question. Instead, you **MUST** use `LEFT JOIN`.
* Your result should include album title `AlbumTitle`, and artist name `ArtistName`.
* Your results should be ordered by ascending order of `AlbumTitle` and ascending order of `ArtistName`.
* Please run the below two queries **before** your solution query.

```python
conn.execute(text("""
    ALTER TABLE Album MODIFY Title VARCHAR(255) COLLATE utf8mb4_general_ci;
"""))

conn.execute(text("""
    SET collation_connection = 'utf8mb4_general_ci';
"""))
```

#### Q24: Retrieve a list of all artists and their corresponding albums, including artists who have not released any albums.

**Requirements:** 
* **IMPORTANT NOTE**: You may **NOT** use a regular join to answer this question. Instead, you **MUST** use `RIGHT JOIN`.
* Your result should include album title `AlbumTitle`, and artist name `ArtistName`.
* Your results should be ordered by ascending order of `AlbumTitle` and ascending order of `ArtistName`.

## Section 3: Grouping and windowing (11 questions)

In this section, you will employ SQL **grouping** clause and **windowing** functions to perform more complex data analysis. These queries will help you uncover the trends, summarize data, and obtain insights into the database. 

### Part 1: Basic grouping

#### Q25: How many tracks are there in each genre?

**Requirements:** 
* Your results must include the `GenreId`, and track count `TrackCount` for each genre.
* Your results should be ordered by descending order of track count.
* Your results should also be ordered by ascending order of `GenreId`.

#### Q26: What is the total duration (in hours) of tracks for top 5 longest albums?

**Requirements:** 
* Your results must include the `AlbumId`, album title `AlbumTitle` and total duration in hours `TotalDurationHours` for each album.
* Your results should be ordered by descending order of total duration in hours.

#### Q27: Retrieve all albums that contain tracks from more than one genre.

**Requirements:** 
* Your results must include the album title `AlbumTitle`, and corresponding unique genre count `GenreCount`.
* Your results should be ordered by descending order of genre count `GenreCount`.
* Your results should also be ordered by ascending order of `AlbumTitle`.

#### Q28: Calculate the total revenue for all artists.

**Requirements:** 
* Your results must include the artist name `ArtistName`, and corresponding total revenue `TotalRevenue`.
* Total revenue calculation: `UnitPrice * Quantity`
* Your results should be ordered by descending order of total revenue.
* Your results should also be ordered by ascending order of `ArtistName`.

#### Q29: Which genres have greater than 20 minute average track duration?

**Requirements:** 
* Your results must include the genre name `GenreName`, and corresponding average duration `AverageDurationMinutes` for tracks that have average duration that exceeds 20 minutes.
* Your results should be ordered by descending order of average duration in minutes.

#### Q30: What is the total expenditure incurred by customers who purchased tracks by "Queen"?

**Requirements:** 
* Your results must include the `CustomerId`, `FirstName`, `LastName`, and corresponding total expenditure `TotalExpenditure` then put the descending rank of total expenditure as `ExpenditureRank`.
* Total expenditure calculation: `UnitPrice * Quantity`
* Your results should be ordered by descending order of total expenditure.
* Your results should also be ordered by ascending order of `CustomerId`.

### Part 2: Windowing queries

Window functions allow you to perform calculations across a set of rows related to the current row, enabling advanced analysis without collapsing data.

#### Q31: Find each track's duration and rank all tracks by their duration.

**Requirements:** 
* Your results must include the `TrackId`, track name `TrackName`, duration in minutes `DurationMinutes`, and corresponding duration rank `DurationRank`.
* Ranking should be based on descending order of duration.
* Your results should be ordered by ascending order of ascending order of duration rank. If two tracks have the same rank, then they should be ordered based on descending order of duration in minutes.
* Your results should also be ordered by ascending order of `TrackId`.

#### Q32: Rank customers who purchased tracks by "Queen" based on their total expenditure.

**Hint:** You solved majority of this question already in Q30. Reuse that solution to answer this question

**Requirements:** 
* Your results must include the `CustomerId`, `FirstName`, `LastName`, corresponding total expenditure `TotalExpenditure`, and corresponding expenditure rank `ExpenditureRank`.
* Total expenditure calculation: `UnitPrice * Quantity`
* Ranking should be based on descending order of total expenditure.
* Your results should be ordered by descending order of total expenditure.
* Your results should also be ordered by ascending order of `CustomerId`.

### Q33: Calculate the total number of invoices for each customer and assign a sequential rank to each customer based on their total invoices.

**Requirements:**
* Your results must include the `CustomerId`, `FirstName`, `LastName`, corresponding invoices count `InvoicesCount`, and corresponding invoice rank `InvoiceRank`.
* Ranking:
  * Ranks assigned to customers must be unique and based on descending order of invoices count. That is customer with highest invoices count should receive rank 1.
  * If there are ties in invoices count, you must break ties by using ascending order of `LastName`. 

#### Q34: Find the top 3 invoices per country.

**Hints:** 
* This is a challenging question.
* Break it down into individual steps:
  1. Determine invoice rank `InvoiceRank` using descending order of `Total`. Make sure order the results both using ascending order of `BillingCountry` and `Total`.
  2. Then, write another query which uses the query you wrote in step 1 as sub query to filter invoices with top 3 ranks.

**Requirements:** 
* Your results must include the `BillingCountry`, `InvoiceId`, `Total`, and corresponding invoice rank `InvoiceRank`.
* Ranking should be based on descending order of `Total`.
* Your results should be ordered by the ascending order of `BillingCountry`, descending order of `Total`, and ascending order of `InvoiceId` in the exact sequence mentioned above. 

#### Q35: Calculate the moving average of monthly sales.

**Hints:** 
* This is a challenging question.
* Break it down into individual steps:
  1. Determine how to extract just the month information from `InvoiceDate` by exploring `DATE_FORMAT`.
  2. Then, calculate total sales per month and order the results by month.
  3. Finally, calculate moving average using `PRECEDING` and `CURRENT`.

**Requirements:** 
* Your results must include the month `Month`, corresponding month's total sales `MonthlySales`, and corresponding month's moving average sales `MovingAverageSales`.
* Your results should be ordered by ascending order of the months.


## Submission
**Github Classroom Invitation Link: https://classroom.github.com/a/qtUnXczB**

- The structure of the required files for your submissions is as follows:
```
project-1--<your_team_name>
|--- README.md (list names of team members at the top)
|--- p1.ipynb
|--- q1.pkl
|--- q2.pkl
|--- ...
|--- q35.pkl
```
These are the files that is absolutely needed for grading, however if you have additional files such as *.csv, you won't get marks off. 
