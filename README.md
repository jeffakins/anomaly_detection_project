# Anomaly Detection Project
- By Jeff Akins

![detective](https://us.123rf.com/450wm/belchonock/belchonock2103/belchonock210326388/166366806-male-detective-with-smoking-pipe-looking-through-magnifying-glass-on-beige-background.jpg?ver=6)

## Project Goals:
**Answer 5 of the following questions about Codeup's Online Syllabus Usage:**
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?

## Deliverables:
- An email with a written summary of my findings (see below)
- A single Executive Summary [slide](https://drive.google.com/file/d/1tmoi10CG7lBmjsW0NqTLbjbxsPhlkNyc/view?usp=sharing)
- Link to the final jupyter notebook

### Executive Summary (Response to Five of the Project Goal Questions):
1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?

I included the top three lessons across all programs.

Overall:
- javascript-i
- java-iii
- html-css

Java Full Stack Web Dev is by far the largest course, so it was no surprise that the lessons that they accessed the most matched the overall numbers:
- javascript-i
- java-iii
- html-css

For PHP Full Stack Web Dev it was:
- index.html
- javascript-i
- html-css

For the few Front End Web Dev students it was:
- content/html-css
- content/html-css/gitbook/images/favicon.ico
- content/html-css/introduction.html

For Data Science it was:
- classification/overview
- 1-fundamentals/1.1-intro-to-data-science
- sql/mysql-overview

2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?

This finding stuck out the most and is included on the slide:
- The Marco cohort accessed the "javascript-i/introduction/working-with-data-types-operators-and-variables" lesson more times than the four other cohorts that accessed that page by a path count of 176

- Some additional interesting findings on this topic:
- The Staff accessed the top lessons the most
- Darden cohort accessed the "Stats/compare-means" twice as much as Easley
- Darden cohort accessed the "sql/mysql-overview" more than three time as much as Easley or Florence
- Ceres cohort accessed the "jquery" more than any other cohort

3. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?

Both Web Dev and Data Science groups accessed the other's curriculum from time to time prior to the 2019 shut off. After 2019, the access drops to near zero; however, there are a few cases where students may have reached a page from another group's curriculum. For example:
Web Dev member accessed the following page one time after 2019:
- anomaly-detection/time-series-anomaly-detection-part-2

Data Science member accessed the following pages one time after 2019:
- java-ii/object-oriented-programming
- spring

With additional time I could reformat the data frame to categorize the lessons accessed by 'web dev' or 'data science'. I could then generate the exact counts of cross-curriculum access before and after the 2019 shut off. 

4. What topics are grads continuing to reference after graduation and into their jobs (for each program)?

Here are the top ten lessons accessed by students after they graduate along with the number of times that lesson has been accessed:

By Web Dev Students:
- javascript-i: 5749
- spring: 4913
- html-css: 4195
- java-iii: 4108
- java-ii: 3952
- java-i: 3528
- javascript-ii: 3417
- mysql: 3006
- jquery: 2953
- spring/fundamentals/repositories: 20

By Data Science Students:
- sql/mysql-overview: 275
- classification/overview: 267
- anomaly-detection/overview: 191
- fundamentals/intro-to-data-science: 184
- 1-fundamentals/1.1-intro-to-data-science: 127
- sql/database-design: 87
- 6-regression/1-overview: 86
- classification/prep: 77
- fundamentals/environment-setup: 76
- stats/compare-means: 73

5. Which lessons are least accessed?

These are the 10 least accessed lessons:

- content/examples/php/arithmetic.php
- 5.04.04_LeastAngleRegression
- 1._Fundamentals/index.html
- javascri
- f
- javascript-i/html-css
- bad-charts
- Correlation.md
- extra-exercises/j
- html-css/css-ii/boostrap-grid-system

## Data Acquisition
The data for this project was accessed through the Codeup MySQL server. The data is on the 'curriculum_logs' table.

### How to replicate:
1. You will need an env file with login permissions for Codeup's MySQL server.
2. Clone the files from my repository.
3. Run the jupyter notebook included in the repository

## Data Preparation:
These are the steps that I took to clean the data:
- Created a function to retrieve the data from the server and then write it to a csv file for quicker access later
- Created a function that adds the course names to the data
- Filled the start, end, created, and update null dates with the log entry date
- Combined the date and time columns, then converted to datetime, and made it the index
- Converted all dates and time columns to datetime format
- Created an hour and weekday columns
- Dropped the original date and time columns
- Filled nulls with 0 for numeric columns (made it easy to filter if needed)
- Filled nulls with 'none' for string columns (made it easy to filter if needed)
- Turn the weekday column into an ordered categorical (for order of days in plotting)

### Data Dictionary:
| #  | Column           | Description       | Non-Null Count  | Dtype         |
|--- | ------           | --------------    | --------------  | -----         |
| 0  | path             | URL path          | 900222 non-null | object        |
| 1  | user_id          | User ID           | 900223 non-null | int64         |
| 2  | cohort_id        | Cohort ID         | 900223 non-null | int64         |
| 3  | ip               | IP Address        | 900223 non-null | object        |
| 4  | name             | Cohort Name       | 900223 non-null | object        |
| 5  | slack            | Slack Name        | 900223 non-null | object        |
| 6  | start_date       | Start Date        | 900223 non-null | datetime64[ns]|
| 7  | end_date         | End Date          | 900223 non-null | datetime64[ns]|
| 8  | created_at       | Created Date      | 900223 non-null | datetime64[ns]|
| 9  | updated_at       | Updated Date      | 900223 non-null | datetime64[ns]|
| 10 | program_id       | Program ID        | 900223 non-null | int64         |
| 11 | course_name      | Course Name       | 900223 non-null | object        |
| 12 | course_subdomain | Subdomain         | 900223 non-null | object        |
| 13 | hour             | Hour Timestamp    | 900223 non-null | int64         |
| 14 | weekday          | Weekday Timestamp | 900223 non-null | category      | 

## Explore:
Explore consisted of plotting different aspects of the data to include histograms of curriculum access by weekday and by hour. Not surprising a majority of the access occurred during the workweek and during class time. The remainder of exploration consisted of manipulating the data frame in order to answer the posed questions. This allowed for plotting and counting events using primarily pandas' value counts.

## Conclusions:
Most of the conclusions were stated in the executive summary. There is certainly more to explore with this dataset. There are numerous singular paths that could be explored as well as unusual access times and frequencies by users. Check back for future updates!