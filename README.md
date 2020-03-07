# Webay-Backend Documentation

## To Do

- [x] Add *Add Listing* option.
- [x] Add *Edit Listing* option.
- [x] Add *Delete Listing* option.
- [x] Add *Search Titles* option.
- [ ] Add *Price Sorting* option.
- [x] Add *Print Listings* option.
- [ ] Finish project proposal.
    - [x] Upload screenshots of program in action to 
    [shared Google Doc](https://docs.google.com/document/d/1ihBZfIJOcxj6T_4s6dOSwVBvJf_e2HV0FrDpJ-MLg0s/edit?usp=sharing).
    - [ ] Proofread answers, expand where possible.
    - [ ] Submit Google Form with following answers.

![General Program Structure](assets/images/program_structure_chart.png)

# Webay

## 1. Introduction

Webay is an open-source webstore backend. Currently, developers can access
functions for adding/modifying/deleting listings, sorting listings based on price, 
as well as searching through listing titles for specific items. 

### Project description

We will be creating a mock version of the [Ebay webstore](https://ebay.com).
This mock store will have price sorting capabilities, 
a general search ability, and the ability to create/edit/delete listings. 
Our mock listings will be generated using a list of preselected objects and associated adjectives.

### Objective/Purpose

The purpose of creating this mock store is to learn how to implement 
search algorithms in an actual use-case situation. 
This is also a stepping stone towards our final project of creating 
a complete webstore application.

## 2. Background/Related studies

Our programming backgrounds cover many languages
such as Java, Javascript, Python, and Arduino. 
We will use previously learned concepts along with
newly learned concepts to complete a functional webstore backend. 

### Background knowledge that you are inspired.

One of the members of our group was keen on building a functional webstore.
We decided to use this project's deadline as motivation 
to both start and finish this project in a timely manner.

### Summaries and notes from your sources (research papers). 

<!-- Fill in notes. -->

## 3. Methods

### How you actually implemented your project (e.g. referring textbook examples or using open-source libraries such as TensorFlow or algorithms that you've found from research articles)

Our project was implemented using open-source libraries included
in the Python Standard Library. 
Of those included, we used Argparse, JSON, Operator, 
Random, and Time.
We also referenced online articles about sort algorithms
and best practices.

### What other sources were available (e.g. Github, StackOverflow, etc)

We used StackOverflow for quickly resolving many library specific errors.
Most of these errors occurred due to improper use of a library's
methods.

## 4. Implementation

### How you implemented your project

We have created an API for a webstore backend. This API is 
accessible via the command line within the project folder.
The API is also accessible via function calls by importing 
our defined classes and functions. 


### Program use cases (with screenshots). If you want to use screenshots, upload your screenshots to your One Drive or Google Drive and share it with me. 

<!-- Link to GD with images. -->
[Program In Action](https://docs.google.com/document/d/1ihBZfIJOcxj6T_4s6dOSwVBvJf_e2HV0FrDpJ-MLg0s/edit?usp=sharing)


## 5. Discussion

### Challenges that you have faced

We faced many small issues that were related to an improper use
of an imported library. Examples include writing to a read-only file, passing incompatible parameters, and misspelling function names.
We also faced larger challenges when storing data, reading data,
and sorting data. We had accidentally overwritten our listing data
file with an empty file, multiple times. 
Luckily we were not handling live data. 

### How to overcome those challenges

Passing incompatible parameters to a function was generally resolved
by carefully reading the generated error messages, looking for the
correct parameter type, and fixing the function call. 
Misspellings were resolved by carefully rereading each library's 
documentation, looking for the function name we thought we were calling. These issues were easy to resolve. 

The issues that required more thought were those relating to
our storage and access of file data. 
To manage this, we developed helper functions to safely read and
write data whenever necessary.

### Stories that you want to share with the class


## 6. Conclusion

### Lessons that you learned from this project

In developing this project, we have learned that figuring out
the best way to organize large amounts of data can be difficult. 
We also discovered the value of a Version Control System, such as git, 
when working collaboratively within a group. 

### How to use this project experience as leverage to get to the next level

In this project, we learned how to access data that is stored on a file.
We implemented a sorting algorithm, title search, and a listing editor into 
a callable API. 
We can now use this API as a general framework for fitting several use-cases.


## 7. Reference

### your resources, at least five academic articles (book or research paper). 

[Python Documentation: JSON](https://docs.python.org/3.7/tutorial/inputoutput.html#reading-and-writing-files)

[Python Documentation: Argparse](https://docs.python.org/3/library/argparse.html)

Learn Python the Hard Way 3rd ed., Zed Shaw
