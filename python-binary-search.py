{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "fda8aa8d",
   "metadata": {},
   "source": [
    "# Introduction to Binary Search and Complexity Analysis with Python\n",
    "\n",
    "### Part 1 of \"Data Structures and Algorithms in Python\"\n",
    "\n",
    "[Data Structures and Algorithms in Python](https://pythondsa.com) is beginner-friendly introduction to common data structures (linked lists, stacks, queues, graphs) and algorithms (search, sorting, recursion, dynamic programming) in Python, designed to help you prepare for coding interviews and assessments. Check out the full series here:\n",
    "\n",
    "1. [Binary Search and Complexity Analysis](https://jovian.ai/aakashns/python-binary-search)\n",
    "2. [Python Classes and Linked Lists](https://jovian.ai/aakashns/python-classes-and-linked-lists)\n",
    "3. Arrays, Stacks, Queues and Strings (coming soon)\n",
    "4. Binary Search Trees and Hash Tables (coming soon)\n",
    "5. Insertion Sort, Merge Sort and Divide-and-Conquer (coming soon)\n",
    "6. Quicksort, Partitions and Average-case Complexity (coming soon)\n",
    "7. Recursion, Backtracking and Dynamic Programming (coming soon)\n",
    "8. Knapsack, Subsequence and Matrix Problems (coming soon)\n",
    "9. Graphs, Breadth-First Search and Depth-First Search (coming soon)\n",
    "10. Shortest Paths, Spanning Trees & Topological Sorting (coming soon)\n",
    "11. Disjoint Sets and the Union Find Algorithm (coming soon)\n",
    "12. Interview Questions, Tips & Practical Advice (coming soon)\n",
    "\n",
    "\n",
    "Earn a verified certificate of accomplishment for this course by signing up here: http://pythondsa.com .\n",
    "\n",
    "Ask questions, get help & participate in discussions on the community forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/78"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b071fcc6",
   "metadata": {},
   "source": [
    "### Prerequisites\n",
    "\n",
    "This course assumes very little background in programming and mathematics, and you can learn the required concepts here:\n",
    "\n",
    "- Basic programming with Python ([variables](https://jovian.ai/aakashns/first-steps-with-python), [data types](https://jovian.ai/aakashns/python-variables-and-data-types), [loops](https://jovian.ai/aakashns/python-branching-and-loops), [functions](https://jovian.ai/aakashns/python-functions-and-scope) etc.)\n",
    "- Some high school mathematics ([polynomials](https://www.youtube.com/watch?v=Vm7H0VTlIco), [vectors, matrices](https://www.youtube.com/watch?v=0oGJTQCy4cQ&list=PLSQl0a2vh4HCs4zPpOEdF2GuydqS90Yb6) and [probability](https://www.youtube.com/watch?v=uzkc-qNVoOk))\n",
    "- No prior knowledge of data structures or algorithms is required\n",
    "\n",
    "We'll cover any additional mathematical and theoretical concepts we need as we go along.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29ea46d5",
   "metadata": {},
   "source": [
    "## How to Run the Code\n",
    "\n",
    "The best way to learn the material is to execute the code and experiment with it yourself. This tutorial is an executable [Jupyter notebook](https://jupyter.org). You can _run_ this tutorial and experiment with the code examples in a couple of ways: *using free online resources* (recommended) or *on your computer*.\n",
    "\n",
    "#### Option 1: Running using free online resources (1-click, recommended)\n",
    "\n",
    "The easiest way to start executing the code is to click the **Run** button at the top of this page and select **Run on Binder**. You can also select \"Run on Colab\" or \"Run on Kaggle\", but you'll need to create an account on [Google Colab](https://colab.research.google.com) or [Kaggle](https://kaggle.com) to use these platforms.\n",
    "\n",
    "\n",
    "#### Option 2: Running on your computer locally\n",
    "\n",
    "To run the code on your computer locally, you'll need to set up [Python](https://www.python.org), download the notebook and install the required libraries. We recommend using the [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/) distribution of Python. Click the **Run** button at the top of this page, select the **Run Locally** option, and follow the instructions.\n",
    "\n",
    ">  **Jupyter Notebooks**: This notebook is made of _cells_. Each cell can contain code written in Python or explanations in plain English. You can execute code cells and view the results instantly within the notebook. Jupyter is a powerful platform for experimentation and analysis. Don't be afraid to mess around with the code & break things - you'll learn a lot by encountering and fixing errors. You can use the \"Kernel > Restart & Clear Output\" menu option to clear all outputs and start again from the top.\n",
    "\n",
    "Try executing the cells below:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "56724fa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import a library module\n",
    "import math"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "050ca7fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7.0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Use a function from the library\n",
    "math.sqrt(49)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "33d760fc",
   "metadata": {},
   "source": [
    "## Problem \n",
    "\n",
    "This course takes a coding-focused approach towards learning. In each notebook, we'll focus on solving one problem, and learn the techniques, algorithms, and data structures to devise an *efficient* solution. We will then generalize the technique and apply it to other problems.\n",
    "\n",
    "\n",
    "\n",
    "In this notebook, we focus on solving the following problem:\n",
    "\n",
    "> **QUESTION 1:** Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.\n",
    "\n",
    "<img src=\"https://i.imgur.com/mazym6s.png\" width=\"480\">\n",
    "\n",
    "This may seem like a simple problem, especially if you're familiar with the concept of _binary search_, but the strategy and technique we learning here will be widely applicable, and we'll soon use it to solve harder problems."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "edda2f63",
   "metadata": {},
   "source": [
    "## Why You Should Learn Data Structures and Algorithms\n",
    "\n",
    "Whether you're pursuing a career in software development or data science, it's almost certain that you'll be asked to solve programming problems like *reversing a linked list* or *balancing a binary tree* in a technical interview or coding assessment.\n",
    "\n",
    "It's well known, however, that you will almost never face these problems in your job as a software developer. So it's reasonable to wonder why such problems are asked in interviews and coding assessments. Solving programming problems demonstrates the following traits:\n",
    "\n",
    "1. You can **think about a problem systematically** and solve it systematically step-by-step.\n",
    "2. You can **envision different inputs, outputs, and edge cases** for programs you write.\n",
    "3. You can **communicate your ideas clearly** to co-workers and incorporate their suggestions.\n",
    "4. Most importantly, you can **convert your thoughts and ideas into working code** that's also readable.\n",
    "\n",
    "It's not your knowledge of specific data structures or algorithms that's tested in an interview, but your approach towards the problem. You may fail to solve the problem and still clear the interview or vice versa. In this course, you will learn the skills to both solve problems and clear interviews successfully.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "369ae622",
   "metadata": {},
   "source": [
    "## The Method\n",
    "\n",
    "Upon reading the problem, you may get some ideas on how to solve it and your first instinct might be to start writing code. This is not the optimal strategy and you may end up spending a longer time trying to solve the problem due to coding errors, or may not be able to solve it at all.\n",
    "\n",
    "Here's a systematic strategy we'll apply for solving problems:\n",
    "\n",
    "1. State the problem clearly. Identify the input & output formats.\n",
    "2. Come up with some example inputs & outputs. Try to cover all edge cases.\n",
    "3. Come up with a correct solution for the problem. State it in plain English.\n",
    "4. Implement the solution and test it using example inputs. Fix bugs, if any.\n",
    "5. Analyze the algorithm's complexity and identify inefficiencies, if any.\n",
    "6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.\n",
    "\n",
    "_\"Applying the right technique\"_ is where the knowledge of common data structures and algorithms comes in handy. \n",
    "\n",
    "Use this template for solving problems by applying this method: https://jovian.ai/aakashns/python-problem-solving-template"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9c11a7df",
   "metadata": {},
   "source": [
    "## Solution\n",
    "\n",
    "\n",
    "### 1. State the problem clearly. Identify the input & output formats.\n",
    "\n",
    "You will often encounter detailed word problems in coding challenges and interviews. The first step is to state the problem clearly and precisely in abstract terms. \n",
    "\n",
    "<img src=\"https://i.imgur.com/mazym6s.png\" width=\"480\">\n",
    "\n",
    "In this case, for instance, we can represent the sequence of cards as a list of numbers. Turning over a specific card is equivalent to accessing the value of the number at the corresponding position the list. \n",
    "\n",
    "<img src=\"https://i.imgur.com/G9fBarb.png\" width=\"600\">\n",
    "\n",
    "The problem can now be stated as follows:\n",
    "\n",
    "#### Problem\n",
    "\n",
    "> We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.\n",
    "\n",
    "#### Input\n",
    "\n",
    "1. `cards`: A list of numbers sorted in decreasing order. E.g. `[13, 11, 10, 7, 4, 3, 1, 0]`\n",
    "2. `query`: A number, whose position in the array is to be determined. E.g. `7`\n",
    "\n",
    "#### Output\n",
    "\n",
    "3. `position`: The position of `query` in the list `cards`. E.g. `3` in the above case (counting from `0`)\n",
    "\n",
    "\n",
    "\n",
    "Based on the above, we can now create the signature of our function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "fdd5f851",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card(cards, query):\n",
    "    pass"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5d70d69a",
   "metadata": {},
   "source": [
    "**Tips**:\n",
    "\n",
    "* Name your function appropriately and think carefully about the signature\n",
    "* Discuss the problem with the interviewer if you are unsure how to frame it in abstract terms\n",
    "* Use descriptive variable names, otherwise you may forget what a variable represents\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "89a41ab7",
   "metadata": {},
   "source": [
    "### 2. Come up with some example inputs & outputs. Try to cover all edge cases.\n",
    "\n",
    "Before we start implementing our function, it would be useful to come up with some example inputs and outputs which we can use later to test out problem. We'll refer to them as *test cases*.\n",
    "\n",
    "Here's the test case described in the example above."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "93163560",
   "metadata": {},
   "outputs": [],
   "source": [
    "cards = [13, 11, 10, 7, 4, 3, 1, 0]\n",
    "query = 7\n",
    "output = 3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c54aa454",
   "metadata": {},
   "source": [
    "We can test our function by passing the inputs into function and comparing the result with the expected output."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "abaa4af2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "None\n"
     ]
    }
   ],
   "source": [
    "result = locate_card(cards, query)\n",
    "print(result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "c838bb55",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result == output"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3724ac9",
   "metadata": {},
   "source": [
    "Obviously, the two result does not match the output as we have not yet implemented the function.\n",
    "\n",
    "We'll represent our test cases as dictionaries to make it easier to test them once we write implement our function. For example, the above test case can be represented as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "eeca48b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "test = {\n",
    "    'input': { \n",
    "        'cards': [13, 11, 10, 7, 4, 3, 1, 0], \n",
    "        'query': 7\n",
    "    },\n",
    "    'output': 3\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "43596eb5",
   "metadata": {},
   "source": [
    "The function can now be tested as follows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "67dbe005",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "locate_card(**test['input']) == test['output']"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fbde700",
   "metadata": {},
   "source": [
    "Our function should be able to handle any set of valid inputs we pass into it. Here's a list of some possible variations we might encounter:\n",
    "\n",
    "1. The number `query` occurs somewhere in the middle of the list `cards`.\n",
    "2. `query` is the first element in `cards`.\n",
    "3. `query` is the last element in `cards`.\n",
    "4. The list `cards` contains just one element, which is `query`.\n",
    "5. The list `cards` does not contain number `query`.\n",
    "6. The list `cards` is empty.\n",
    "7. The list `cards` contains repeating numbers.\n",
    "8. The number `query` occurs at more than one position in `cards`.\n",
    "9. (can you think of any more variations?)\n",
    "\n",
    "> **Edge Cases**: It's likely that you didn't think of all of the above cases when you read the problem for the first time. Some of these (like the empty array or `query` not occurring in `cards`) are called *edge cases*, as they represent rare or extreme examples. \n",
    "\n",
    "While edge cases may not occur frequently, your programs should be able to handle all edge cases, otherwise they may fail in unexpected ways. Let's create some more test cases for the variations listed above. We'll store all our test cases in an list for easier testing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2d6e3f66",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "b16a6172",
   "metadata": {},
   "outputs": [],
   "source": [
    "tests = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0cc13fc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query occurs in the middle\n",
    "tests.append(test)\n",
    "\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [13, 11, 10, 7, 4, 3, 1, 0],\n",
    "        'query': 1\n",
    "    },\n",
    "    'output': 6\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "faba8d6d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query is the first element\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [4, 2, 1, -1],\n",
    "        'query': 4\n",
    "    },\n",
    "    'output': 0\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "b93855fe",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query is the last element\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [3, -1, -9, -127],\n",
    "        'query': -127\n",
    "    },\n",
    "    'output': 3\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "56a18127",
   "metadata": {},
   "outputs": [],
   "source": [
    "# cards contains just one element, query\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [6],\n",
    "        'query': 6\n",
    "    },\n",
    "    'output': 0 \n",
    "})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2446f62",
   "metadata": {},
   "source": [
    "The problem statement does not specify what to do if the list `cards` does not contain the number `query`. \n",
    "\n",
    "1. Read the problem statement again, carefully.\n",
    "2. Look through the examples provided with the problem.\n",
    "3. Ask the interviewer/platform for a clarification.\n",
    "4. Make a reasonable assumption, state it and move forward.\n",
    "\n",
    "We will assume that our function will return `-1` in case `cards` does not contain `query`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "0dc648fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# cards does not contain query \n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [9, 7, 5, 2, -9],\n",
    "        'query': 4\n",
    "    },\n",
    "    'output': -1\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "cc8db169",
   "metadata": {},
   "outputs": [],
   "source": [
    "# cards is empty\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [],\n",
    "        'query': 7\n",
    "    },\n",
    "    'output': -1\n",
    "})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "b8b2ae96",
   "metadata": {},
   "outputs": [],
   "source": [
    "# numbers can repeat in cards\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],\n",
    "        'query': 3\n",
    "    },\n",
    "    'output': 7\n",
    "})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "13bba342",
   "metadata": {},
   "source": [
    "In the case where `query` occurs multiple times in `cards`, we'll expect our function to return the first occurrence of `query`. \n",
    "\n",
    "While it may also be acceptable for the function to return any position where `query` occurs within the list, it would be slightly more difficult to test the function, as the output is non-deterministic."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9d1258cc",
   "metadata": {},
   "outputs": [],
   "source": [
    "# query occurs multiple times\n",
    "tests.append({\n",
    "    'input': {\n",
    "        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],\n",
    "        'query': 6\n",
    "    },\n",
    "    'output': 2\n",
    "})"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "001e4a69",
   "metadata": {},
   "source": [
    "Let's look at the full set of test cases we have created so far."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "56d29397",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},\n",
       " {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},\n",
       " {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},\n",
       " {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},\n",
       " {'input': {'cards': [6], 'query': 6}, 'output': 0},\n",
       " {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},\n",
       " {'input': {'cards': [], 'query': 7}, 'output': -1},\n",
       " {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3},\n",
       "  'output': 7},\n",
       " {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],\n",
       "   'query': 6},\n",
       "  'output': 2}]"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tests"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8ec7056",
   "metadata": {},
   "source": [
    "Great, now we have a fairly exhaustive set of test cases to evaluate our function. \n",
    "\n",
    "Creating test cases beforehand allows you to identify different variations and edge cases in advance so that can make sure to handle them while writing code. Sometimes, you may start out confused, but the solution will reveal itself as you try to come up with interesting test cases.\n",
    "\n",
    "\n",
    "**Tip:** Don't stress it if you can't come up with an exhaustive list of test cases though. You can come back to this section and add more test cases as you discover them. Coming up with good test cases is a skill that takes practice.\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd65b5b3",
   "metadata": {},
   "source": [
    "### 3. Come up with a correct solution for the problem. State it in plain English.\n",
    "\n",
    "Our first goal should always be to come up with a _correct_ solution to the problem, which may necessarily be the most _efficient_ solution. The simplest or most obvious solution to a problem, which generally involves checking all possible answers is called the _brute force_ solution.\n",
    "\n",
    "In this problem, coming up with a correct solution is quite easy: Bob can simply turn over cards in order one by one, till he find a card with the given number on it. Here's how we might implement it:\n",
    "\n",
    "1. Create a variable `position` with the value 0.\n",
    "3. Check whether the number at index `position` in `card` equals `query`.\n",
    "4. If it does, `position` is the answer and can be returned from the function\n",
    "5. If not, increment the value of `position` by 1, and repeat steps 2 to 5 till we reach the last position.\n",
    "6. If the number was not found, return `-1`.\n",
    "\n",
    "> **Linear Search Algorithm**: Congratulations, we've just written our first _algorithm_! An algorithm is simply a list of statements which can be converted into code and executed by a computer on different sets of inputs. This particular algorithm is called linear search, since it involves searching through a list in a linear fashion i.e. element after element.\n",
    "\n",
    "\n",
    "**Tip:** Always try to express (speak or write) the algorithm in your own words before you start coding. It can be as brief or detailed as you require it to be. Writing is a great tool for thinking clearly. It's likely that you will find some parts of the solution difficult to express, which suggests that you are probably unable to think about it clearly. The more clearly you are able to express your thoughts, the easier it will be for you to turn into code."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7e3c9fcb",
   "metadata": {},
   "source": [
    "### 4. Implement the solution and test it using example inputs. Fix bugs, if any.\n",
    "\n",
    "Phew! We are finally ready to implement our solution. All the work we've done so far will definitely come in handy, as we now exactly what we want our function to do, and we have an easy way of testing it on a variety of inputs.\n",
    "\n",
    "Here's a first attempt at implementing the function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "9b9025f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card(cards, query):\n",
    "    # Create a variable position with the value 0\n",
    "    position = 0\n",
    "    \n",
    "    # Set up a loop for repetition\n",
    "    while True:\n",
    "        \n",
    "        # Check if element at the current position matche the query\n",
    "        if cards[position] == query:\n",
    "            \n",
    "            # Answer found! Return and exit..\n",
    "            return position\n",
    "        \n",
    "        # Increment the position\n",
    "        position += 1\n",
    "        \n",
    "        # Check if we have reached the end of the array\n",
    "        if position == len(cards):\n",
    "            \n",
    "            # Number not found, return -1\n",
    "            return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1597136d",
   "metadata": {},
   "source": [
    "Let's test out the function with the first test case"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "c022d71f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3}"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "cc82aa18",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result = locate_card(test['input']['cards'], test['input']['query'])\n",
    "result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "757165fd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "7d5cb56b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "result == output"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b39a980",
   "metadata": {},
   "source": [
    "Yay! The result matches the output. \n",
    "\n",
    "To help you test your functions easily the `jovian` Python library provides a helper function `evalute_test_case`. Apart from checking whether the function produces the expected result, it also displays the input, expected output, actual output from the function, and the execution time of the function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "7f7f05a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install jovian --upgrade --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f275b249",
   "metadata": {},
   "outputs": [],
   "source": [
    "from jovian.pythondsa import evaluate_test_case"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2f36a5f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.008 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(3, True, 0.008)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_case(locate_card, test)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1b6cbb41",
   "metadata": {},
   "source": [
    "While it may seem like we have a working solution based on the above test, we can't be sure about it until we test the function with all the test cases. \n",
    "\n",
    "We can use the `evaluate_test_cases` (plural) function from the `jovian` library to test our function on all the test cases with a single line of code."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "51447bd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from jovian.pythondsa import evaluate_test_cases"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "25611080",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[1mTEST CASE #0\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.004 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #1\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}\n",
      "\n",
      "Expected Output:\n",
      "6\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "6\n",
      "\n",
      "Execution Time:\n",
      "0.003 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #2\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [4, 2, 1, -1], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.002 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #3\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [3, -1, -9, -127], 'query': -127}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.003 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #4\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [6], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.002 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #5\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [9, 7, 5, 2, -9], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.003 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #6\u001b[0m\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-38-2111dddaa84c>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mevaluate_test_cases\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlocate_card\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtests\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m/opt/conda/lib/python3.9/site-packages/jovian/pythondsa/__init__.py\u001b[0m in \u001b[0;36mevaluate_test_cases\u001b[0;34m(function, test_cases, error_only, summary_only)\u001b[0m\n\u001b[1;32m     85\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0merror_only\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     86\u001b[0m             \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"\\n\\033[1mTEST CASE #{}\\033[0m\"\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 87\u001b[0;31m         \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mevaluate_test_case\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfunction\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mtest_case\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mdisplay\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mFalse\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     88\u001b[0m         \u001b[0mresults\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mappend\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mresult\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     89\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0merror_only\u001b[0m \u001b[0;32mand\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mresult\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/opt/conda/lib/python3.9/site-packages/jovian/pythondsa/__init__.py\u001b[0m in \u001b[0;36mevaluate_test_case\u001b[0;34m(function, test_case, display)\u001b[0m\n\u001b[1;32m     63\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     64\u001b[0m     \u001b[0mstart\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtimer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 65\u001b[0;31m     \u001b[0mactual_output\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfunction\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m**\u001b[0m\u001b[0minputs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     66\u001b[0m     \u001b[0mend\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtimer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     67\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-29-9ed30c367c36>\u001b[0m in \u001b[0;36mlocate_card\u001b[0;34m(cards, query)\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m         \u001b[0;31m# Check if element at the current position matche the query\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 9\u001b[0;31m         \u001b[0;32mif\u001b[0m \u001b[0mcards\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mposition\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mquery\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     10\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     11\u001b[0m             \u001b[0;31m# Answer found! Return and exit..\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "evaluate_test_cases(locate_card, tests)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6ab899b8",
   "metadata": {},
   "source": [
    "Oh no! Looks like our function encountered an error in the sixth test case. The error message suggests that we're trying to access an index outside the range of valid indices in the list. Looks like the list `cards` is empty in this case, and may be the root of the problem. \n",
    "\n",
    "Let's add some `print` statements within our function to print the inputs and the value of the `position` variable in each loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "9b1bbf6c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card(cards, query):\n",
    "    position = 0\n",
    "    \n",
    "    print('cards:', cards)\n",
    "    print('query:', query)\n",
    "    \n",
    "    while True:\n",
    "        print('position:', position)\n",
    "        \n",
    "        if cards[position] == query:\n",
    "            return position\n",
    "        \n",
    "        position += 1\n",
    "        if position == len(cards):\n",
    "            return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "292eb990",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cards: []\n",
      "query: 7\n",
      "position: 0\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-40-5f727cb3c2c3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mquery6\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mtests\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;36m6\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'input'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'query'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m \u001b[0mlocate_card\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcards6\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mquery6\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;32m<ipython-input-39-aabbbc74d5cf>\u001b[0m in \u001b[0;36mlocate_card\u001b[0;34m(cards, query)\u001b[0m\n\u001b[1;32m      8\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'position:'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mposition\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 10\u001b[0;31m         \u001b[0;32mif\u001b[0m \u001b[0mcards\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mposition\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mquery\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     11\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mposition\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     12\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "cards6 = tests[6]['input']['cards']\n",
    "query6 = tests[6]['input']['query']\n",
    "\n",
    "locate_card(cards6, query6)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9dd051ea",
   "metadata": {},
   "source": [
    "Clearly, since `cards` is empty, it's not possible to access the element at index 0. To fix this, we can check whether we've reached the end of the array before trying to access an element from it. In fact, this can be terminating condition for the `while` loop itself."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "290b9e1a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card(cards, query):\n",
    "    position = 0\n",
    "    while position < len(cards):\n",
    "        if cards[position] == query:\n",
    "            return position\n",
    "        position += 1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bbf633ff",
   "metadata": {},
   "source": [
    "Let's test the failing case again."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "7768a43a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'input': {'cards': [], 'query': 7}, 'output': -1}"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tests[6]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "0c1296cf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "locate_card(cards6, query6)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c56f18f",
   "metadata": {},
   "source": [
    "The result now matches the expected output. Do you now see the benefit of listing test cases beforehand? Without a good set of test cases, we may never have discovered this error in our function.\n",
    "\n",
    "Let's verify that all the other test cases pass too."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "d959ce58",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[1mTEST CASE #0\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.005 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #1\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}\n",
      "\n",
      "Expected Output:\n",
      "6\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "6\n",
      "\n",
      "Execution Time:\n",
      "0.005 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #2\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [4, 2, 1, -1], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.003 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #3\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [3, -1, -9, -127], 'query': -127}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.003 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #4\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [6], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.002 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #5\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [9, 7, 5, 2, -9], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.004 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #6\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.002 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #7\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}\n",
      "\n",
      "Expected Output:\n",
      "7\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "7\n",
      "\n",
      "Execution Time:\n",
      "0.004 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #8\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "2\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "2\n",
      "\n",
      "Execution Time:\n",
      "0.006 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mSUMMARY\u001b[0m\n",
      "\n",
      "TOTAL: 9, \u001b[92mPASSED\u001b[0m: 9, \u001b[91mFAILED\u001b[0m: 0\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[(3, True, 0.005),\n",
       " (6, True, 0.005),\n",
       " (0, True, 0.003),\n",
       " (3, True, 0.003),\n",
       " (0, True, 0.002),\n",
       " (-1, True, 0.004),\n",
       " (-1, True, 0.002),\n",
       " (7, True, 0.004),\n",
       " (2, True, 0.006)]"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_cases(locate_card, tests)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "074fb1b9",
   "metadata": {},
   "source": [
    "Our code passes all the test cases. Of course, there might be some other edge cases we haven't thought of which may cause the function to fail. Can you think of any?\n",
    "\n",
    "**Tip**: In a real interview or coding assessment, you can skip the step of implementing and testing the brute force solution in the interest of time. It's generally quite easy to figure out the complexity of the brute for solution from the plain English description."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0357bd79",
   "metadata": {},
   "source": [
    "### 5. Analyze the algorithm's complexity and identify inefficiencies, if any.\n",
    "\n",
    "Recall this statement from  original question: _\"Alice challenges Bob to pick out the card containing a given number by **turning over as few cards as possible**.\"_ We restated this requirement as: _\"Minimize the number of times we access elements from the list `cards`\"_\n",
    "\n",
    "<img src=\"https://i.imgur.com/mazym6s.png\" width=\"480\">\n",
    "\n",
    "Before we can minimize the number, we need a way to measure it. Since we access a list element once in every iteration, for a list of size `N` we access the elements from the list up to `N` times. Thus, Bob may need to overturn up to `N` cards in the worst case, to find the required card. \n",
    "\n",
    "Suppose he is only allowed to overturn 1 card per minute, it may take him 30 minutes to find the required card if 30 cards are laid out on the table. Is this the best he can do? Is a way for Bob to arrive at the answer by turning over just 5 cards, instead of 30?\n",
    "\n",
    "The field of study concerned with finding the amount of time, space or other resources required to complete the execution of computer programs is called _the analysis of algorithms_. And the process of figuring out the best algorithm to solve a given problem is called _algorithm design and optimization_.\n",
    "\n",
    "\n",
    "### Complexity and Big O Notation\n",
    "\n",
    "> **Complexity** of an algorithm is a measure of the amount of time and/or space required by an algorithm for an input of a given size e.g. `N`. Unless otherwise stated, the term _complexity_ always refers to the worst-case complexity (i.e. the highest possible time/space taken by the program/algorithm to process an input).\n",
    "\n",
    "In the case of linear search:\n",
    "\n",
    "1. The _time complexity_ of the algorithm is `cN` for some fixed constant `c` that depends on the number of operations we perform in each iteration and the time taken to execute a statement. Time complexity is sometimes also called the _running time_ of the algorithm.\n",
    "\n",
    "2. The _space complexity_ is some constant `c'` (independent of `N`), since we just need a single variable `position` to iterate through the array, and it occupies a constant space in the computer's memory (RAM).\n",
    "\n",
    "\n",
    "> **Big O Notation**: Worst-case complexity is often expressed using the Big O notation. In the Big O, we drop fixed constants and lower powers of variables to capture the trend of relationship between the size of the input and the complexity of the algorithm i.e. if the complexity of the algorithm is `cN^3 + dN^2 + eN + f`, in the Big O notation it is expressed as **O(N^3)**\n",
    "\n",
    "Thus, the time complexity of linear search is **O(N)** and its space complexity is **O(1)**.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0560848e",
   "metadata": {},
   "source": [
    "### Save and upload your work to Jovian\n",
    "\n",
    "Whether you're running this Jupyter notebook online or on your computer, it's essential to save your work from time to time. You can continue working on a saved notebook later or share it with friends and colleagues to let them execute your code. [Jovian](https://jovian.ai/platform-features) offers an easy way of saving and sharing your Jupyter notebooks online."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "8f4e1db5",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install jovian --upgrade --quiet"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "952025d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import jovian"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b3922637",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "window.require && require([\"base/js/namespace\"],function(Jupyter){Jupyter.notebook.save_checkpoint()})"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[jovian] Updating notebook \"lisashen-iii/python-binary-search\" on https://jovian.ai\u001b[0m\n",
      "[jovian] Committed successfully! https://jovian.ai/lisashen-iii/python-binary-search\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'https://jovian.ai/lisashen-iii/python-binary-search'"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jovian.commit(project='python-binary-search', environment=None)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "037fe0f6",
   "metadata": {},
   "source": [
    "### 6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.\n",
    "\n",
    "At the moment, we're simply going over cards one by one, and not even utilizing the face that they're sorted. This is called a *brute force* approach.\n",
    "\n",
    "It would be great if Bob could somehow guess the card at the first attempt, but with all the cards turned over it's simply impossible to guess the right card. \n",
    "\n",
    "\n",
    "<img src=\"https://i.imgur.com/mazym6s.png\" width=\"480\">\n",
    "\n",
    "The next best idea would be to pick a random card, and use the fact that the list is sorted, to determine whether the target card lies to the left or right of it. In fact, if we pick the middle card, we can reduce the number of additional cards to be tested to half the size of the list. Then, we can simply repeat the process with each half. This technique is called binary search. Here's a visual explanation of the technique:\n",
    "\n",
    "\n",
    "\n",
    "<img src=\"https://miro.medium.com/max/494/1*3eOrsoF9idyOp-0Ll9I9PA.png\" width=\"480\">\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ad33f4a2",
   "metadata": {},
   "source": [
    "### 7. Come up with a correct solution for the problem. State it in plain English.\n",
    "\n",
    "Here's how binary search can be applied to our problem:\n",
    "\n",
    "1. Find the middle element of the list.\n",
    "2. If it matches queried number, return the middle position as the answer.\n",
    "3. If it is less than the queried number, then search the first half of the list\n",
    "3. If it is greater than the queried number, then search the second half of the list\n",
    "4. If no more elements remain, return -1.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "4756c5be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "window.require && require([\"base/js/namespace\"],function(Jupyter){Jupyter.notebook.save_checkpoint()})"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[jovian] Updating notebook \"lisashen-iii/python-binary-search\" on https://jovian.ai\u001b[0m\n",
      "[jovian] Committed successfully! https://jovian.ai/lisashen-iii/python-binary-search\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'https://jovian.ai/lisashen-iii/python-binary-search'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jovian.commit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32cf140e",
   "metadata": {},
   "source": [
    "### 8. Implement the solution and test it using example inputs. Fix bugs, if any."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c80d6d15",
   "metadata": {},
   "source": [
    "Here's an implementation of binary search for solving our problem. We also print the relevant variables in each iteration of the `while` loop."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "dfb38479",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card(cards, query):\n",
    "    lo, hi = 0, len(cards) - 1\n",
    "    \n",
    "    while lo <= hi:\n",
    "        mid = (lo + hi) // 2\n",
    "        mid_number = cards[mid]\n",
    "        \n",
    "        print(\"lo:\", lo, \", hi:\", hi, \", mid:\", mid, \", mid_number:\", mid_number)\n",
    "        \n",
    "        if mid_number == query:\n",
    "            return mid\n",
    "        elif mid_number < query:\n",
    "            hi = mid - 1  \n",
    "        elif mid_number > query:\n",
    "            lo = mid + 1\n",
    "    \n",
    "    return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "24f0d8e5",
   "metadata": {},
   "source": [
    "Let's test it out using the test cases."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "af219d3b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[1mTEST CASE #0\u001b[0m\n",
      "lo: 0 , hi: 7 , mid: 3 , mid_number: 7\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.227 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #1\u001b[0m\n",
      "lo: 0 , hi: 7 , mid: 3 , mid_number: 7\n",
      "lo: 4 , hi: 7 , mid: 5 , mid_number: 3\n",
      "lo: 6 , hi: 7 , mid: 6 , mid_number: 1\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}\n",
      "\n",
      "Expected Output:\n",
      "6\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "6\n",
      "\n",
      "Execution Time:\n",
      "0.715 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #2\u001b[0m\n",
      "lo: 0 , hi: 3 , mid: 1 , mid_number: 2\n",
      "lo: 0 , hi: 0 , mid: 0 , mid_number: 4\n",
      "\n",
      "Input:\n",
      "{'cards': [4, 2, 1, -1], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.387 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #3\u001b[0m\n",
      "lo: 0 , hi: 3 , mid: 1 , mid_number: -1\n",
      "lo: 2 , hi: 3 , mid: 2 , mid_number: -9\n",
      "lo: 3 , hi: 3 , mid: 3 , mid_number: -127\n",
      "\n",
      "Input:\n",
      "{'cards': [3, -1, -9, -127], 'query': -127}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "4.742 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #4\u001b[0m\n",
      "lo: 0 , hi: 0 , mid: 0 , mid_number: 6\n",
      "\n",
      "Input:\n",
      "{'cards': [6], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.77 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #5\u001b[0m\n",
      "lo: 0 , hi: 4 , mid: 2 , mid_number: 5\n",
      "lo: 3 , hi: 4 , mid: 3 , mid_number: 2\n",
      "\n",
      "Input:\n",
      "{'cards': [9, 7, 5, 2, -9], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.354 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #6\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.002 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #7\u001b[0m\n",
      "lo: 0 , hi: 13 , mid: 6 , mid_number: 6\n",
      "lo: 7 , hi: 13 , mid: 10 , mid_number: 2\n",
      "lo: 7 , hi: 9 , mid: 8 , mid_number: 2\n",
      "lo: 7 , hi: 7 , mid: 7 , mid_number: 3\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}\n",
      "\n",
      "Expected Output:\n",
      "7\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "7\n",
      "\n",
      "Execution Time:\n",
      "1.74 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #8\u001b[0m\n",
      "lo: 0 , hi: 14 , mid: 7 , mid_number: 6\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "2\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "7\n",
      "\n",
      "Execution Time:\n",
      "3.525 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[91mFAILED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mSUMMARY\u001b[0m\n",
      "\n",
      "TOTAL: 9, \u001b[92mPASSED\u001b[0m: 8, \u001b[91mFAILED\u001b[0m: 1\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[(3, True, 0.227),\n",
       " (6, True, 0.715),\n",
       " (0, True, 0.387),\n",
       " (3, True, 4.742),\n",
       " (0, True, 0.77),\n",
       " (-1, True, 0.354),\n",
       " (-1, True, 0.002),\n",
       " (7, True, 1.74),\n",
       " (7, False, 3.525)]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_cases(locate_card, tests)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6e0a40cc",
   "metadata": {},
   "source": [
    "Looks like it passed 8 out of 9 tests! Let's look at the failed test."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "59c446dc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "2\n",
      "\n",
      "lo: 0 , hi: 14 , mid: 7 , mid_number: 6\n",
      "\n",
      "Actual Output:\n",
      "7\n",
      "\n",
      "Execution Time:\n",
      "0.93 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[91mFAILED\u001b[0m\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(7, False, 0.93)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_case(locate_card, tests[8])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "93b9e9a8",
   "metadata": {},
   "source": [
    "Seems like our function returned the position `7`. Let's check what lies at this position in the input list."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "fbb05e5e",
   "metadata": {},
   "outputs": [],
   "source": [
    "cards8 = tests[8]['input']['cards']\n",
    "query8 = tests[8]['input']['cards']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "d9b3099e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "6"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "query8[7]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bb5f45a0",
   "metadata": {},
   "source": [
    "Seems like we did locate a 6 in the array, it's just that it wasn't the first 6. As you can guess, this is because in binary search, we don't go over indices in a linear order.\n",
    "\n",
    "So how do we fix it?\n",
    "\n",
    "When we find that `cards[mid]` is equal to `query`, we need to check whether it is the first occurrence of `query` in the list i.e the number that comes before it.\n",
    "\n",
    "`[8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0]`\n",
    "\n",
    "To make it easier, we'll define a helper function called `test_location`, which will take the list `cards`, the `query` and `mid` as inputs.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "41ea54db",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_location(cards, query, mid):\n",
    "    mid_number = cards[mid]\n",
    "    print(\"mid:\", mid, \", mid_number:\", mid_number)\n",
    "    if mid_number == query:\n",
    "        if mid-1 >= 0 and cards[mid-1] == query:\n",
    "            return 'left'\n",
    "        else:\n",
    "            return 'found'\n",
    "    elif mid_number < query:\n",
    "        return 'left'\n",
    "    else:\n",
    "        return 'right'\n",
    "\n",
    "def locate_card(cards, query):\n",
    "    lo, hi = 0, len(cards) - 1\n",
    "    \n",
    "    while lo <= hi:\n",
    "        print(\"lo:\", lo, \", hi:\", hi)\n",
    "        mid = (lo + hi) // 2\n",
    "        result = test_location(cards, query, mid)\n",
    "        \n",
    "        if result == 'found':\n",
    "            return mid\n",
    "        elif result == 'left':\n",
    "            hi = mid - 1\n",
    "        elif result == 'right':\n",
    "            lo = mid + 1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "83d2f057",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "2\n",
      "\n",
      "lo: 0 , hi: 14\n",
      "mid: 7 , mid_number: 6\n",
      "lo: 0 , hi: 6\n",
      "mid: 3 , mid_number: 6\n",
      "lo: 0 , hi: 2\n",
      "mid: 1 , mid_number: 8\n",
      "lo: 2 , hi: 2\n",
      "mid: 2 , mid_number: 6\n",
      "\n",
      "Actual Output:\n",
      "2\n",
      "\n",
      "Execution Time:\n",
      "1.742 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(2, True, 1.742)"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_case(locate_card, tests[8])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "949ac52a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[1mTEST CASE #0\u001b[0m\n",
      "lo: 0 , hi: 7\n",
      "mid: 3 , mid_number: 7\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.089 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #1\u001b[0m\n",
      "lo: 0 , hi: 7\n",
      "mid: 3 , mid_number: 7\n",
      "lo: 4 , hi: 7\n",
      "mid: 5 , mid_number: 3\n",
      "lo: 6 , hi: 7\n",
      "mid: 6 , mid_number: 1\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}\n",
      "\n",
      "Expected Output:\n",
      "6\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "6\n",
      "\n",
      "Execution Time:\n",
      "0.249 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #2\u001b[0m\n",
      "lo: 0 , hi: 3\n",
      "mid: 1 , mid_number: 2\n",
      "lo: 0 , hi: 0\n",
      "mid: 0 , mid_number: 4\n",
      "\n",
      "Input:\n",
      "{'cards': [4, 2, 1, -1], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.186 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #3\u001b[0m\n",
      "lo: 0 , hi: 3\n",
      "mid: 1 , mid_number: -1\n",
      "lo: 2 , hi: 3\n",
      "mid: 2 , mid_number: -9\n",
      "lo: 3 , hi: 3\n",
      "mid: 3 , mid_number: -127\n",
      "\n",
      "Input:\n",
      "{'cards': [3, -1, -9, -127], 'query': -127}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.368 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #4\u001b[0m\n",
      "lo: 0 , hi: 0\n",
      "mid: 0 , mid_number: 6\n",
      "\n",
      "Input:\n",
      "{'cards': [6], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.085 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #5\u001b[0m\n",
      "lo: 0 , hi: 4\n",
      "mid: 2 , mid_number: 5\n",
      "lo: 3 , hi: 4\n",
      "mid: 3 , mid_number: 2\n",
      "\n",
      "Input:\n",
      "{'cards': [9, 7, 5, 2, -9], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.179 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #6\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.002 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #7\u001b[0m\n",
      "lo: 0 , hi: 13\n",
      "mid: 6 , mid_number: 6\n",
      "lo: 7 , hi: 13\n",
      "mid: 10 , mid_number: 2\n",
      "lo: 7 , hi: 9\n",
      "mid: 8 , mid_number: 2\n",
      "lo: 7 , hi: 7\n",
      "mid: 7 , mid_number: 3\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}\n",
      "\n",
      "Expected Output:\n",
      "7\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "7\n",
      "\n",
      "Execution Time:\n",
      "0.319 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #8\u001b[0m\n",
      "lo: 0 , hi: 14\n",
      "mid: 7 , mid_number: 6\n",
      "lo: 0 , hi: 6\n",
      "mid: 3 , mid_number: 6\n",
      "lo: 0 , hi: 2\n",
      "mid: 1 , mid_number: 8\n",
      "lo: 2 , hi: 2\n",
      "mid: 2 , mid_number: 6\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "2\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "2\n",
      "\n",
      "Execution Time:\n",
      "0.335 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mSUMMARY\u001b[0m\n",
      "\n",
      "TOTAL: 9, \u001b[92mPASSED\u001b[0m: 9, \u001b[91mFAILED\u001b[0m: 0\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[(3, True, 0.089),\n",
       " (6, True, 0.249),\n",
       " (0, True, 0.186),\n",
       " (3, True, 0.368),\n",
       " (0, True, 0.085),\n",
       " (-1, True, 0.179),\n",
       " (-1, True, 0.002),\n",
       " (7, True, 0.319),\n",
       " (2, True, 0.335)]"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_cases(locate_card, tests)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "145f0716",
   "metadata": {},
   "source": [
    "In fact, once we have written out the algorithm, we may want to add a few more test cases:\n",
    "\n",
    "1. The number lies in first half of the array. \n",
    "2. The number lies in the second half of the array."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e8606131",
   "metadata": {},
   "source": [
    "Here is the final code for the algorithm (without the `print` statements):"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "8fa51332",
   "metadata": {},
   "outputs": [],
   "source": [
    "def test_location(cards, query, mid):\n",
    "    if cards[mid] == query:\n",
    "        if mid-1 >= 0 and cards[mid-1] == query:\n",
    "            return 'left'\n",
    "        else:\n",
    "            return 'found'\n",
    "    elif cards[mid] < query:\n",
    "        return 'left'\n",
    "    else:\n",
    "        return 'right'\n",
    "\n",
    "def locate_card(cards, query):\n",
    "    lo, hi = 0, len(cards) - 1\n",
    "    while lo <= hi:\n",
    "        mid = (lo + hi) // 2\n",
    "        result = test_location(cards, query, mid)\n",
    "        if result == 'found':\n",
    "            return mid\n",
    "        elif result == 'left':\n",
    "            hi = mid - 1\n",
    "        elif result == 'right':\n",
    "            lo = mid + 1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1401ce95",
   "metadata": {},
   "source": [
    "Try creating a few more test cases to test the algorithm more extensively. \n",
    "\n",
    "Let's save our work before continuing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "e97c93d0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "window.require && require([\"base/js/namespace\"],function(Jupyter){Jupyter.notebook.save_checkpoint()})"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[jovian] Updating notebook \"lisashen-iii/python-binary-search\" on https://jovian.ai\u001b[0m\n",
      "[jovian] Committed successfully! https://jovian.ai/lisashen-iii/python-binary-search\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'https://jovian.ai/lisashen-iii/python-binary-search'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jovian.commit()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9176d0ab",
   "metadata": {},
   "source": [
    "### 9. Analyze the algorithm's complexity and identify inefficiencies, if any.\n",
    "\n",
    "Once again, let's try to count the number of iterations in the algorithm. If we start out with an array of N elements, then each time the size of the array reduces to half for the next iteration, until we are left with just 1 element.\n",
    "\n",
    "Initial length - `N`\n",
    "\n",
    "Iteration 1 - `N/2`\n",
    "\n",
    "Iteration 2 - `N/4` i.e. `N/2^2`\n",
    "\n",
    "Iteration 3 - `N/8` i.e. `N/2^3`\n",
    "\n",
    "...\n",
    "\n",
    "Iteration k - `N/2^k`\n",
    "\n",
    "\n",
    "Since the final length of the array is 1, we can find the \n",
    "\n",
    "`N/2^k = 1`\n",
    "\n",
    "Rearranging the terms, we get\n",
    "\n",
    "`N = 2^k`\n",
    "\n",
    "Taking the logarithm\n",
    "\n",
    "`k = log N`\n",
    "\n",
    "Where `log` refers to log to the base 2. Therefore, our algorithm has the time complexity **O(log N)**. This fact is often stated as: binary search _runs_ in logarithmic time. You can verify that the space complexity of binary search is **O(1)**.\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "080c2947",
   "metadata": {},
   "source": [
    "### Binary Search vs. Linear Search\n",
    "\n",
    "Su\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "390b9e7c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card_linear(cards, query):\n",
    "    position = 0\n",
    "    while position < len(cards):\n",
    "        if cards[position] == query:\n",
    "            return position\n",
    "        position += 1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "aae8129a",
   "metadata": {},
   "outputs": [],
   "source": [
    "large_test = {\n",
    "    'input': {\n",
    "        'cards': list(range(10000000, 0, -1)),\n",
    "        'query': 2\n",
    "    },\n",
    "    'output': 9999998\n",
    "    \n",
    "} "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "5d1489cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 9999998\n",
      "Passed: True\n",
      "Execution Time: 1209.677 ms\n"
     ]
    }
   ],
   "source": [
    "result, passed, runtime = evaluate_test_case(locate_card_linear, large_test, display=False)\n",
    "\n",
    "print(\"Result: {}\\nPassed: {}\\nExecution Time: {} ms\".format(result, passed, runtime))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "1e97c27d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result: 9999998\n",
      "Passed: True\n",
      "Execution Time: 0.027 ms\n"
     ]
    }
   ],
   "source": [
    "result, passed, runtime = evaluate_test_case(locate_card, large_test, display=False)\n",
    "\n",
    "print(\"Result: {}\\nPassed: {}\\nExecution Time: {} ms\".format(result, passed, runtime))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "98db2b90",
   "metadata": {},
   "source": [
    "The binary search version is over 55,000 times faster than the linear search version. \n",
    "\n",
    "Furthermore, as the size of the input grows larger, the difference only gets bigger. For a list 10 times, the size, linear search would run for 10 times longer, whereas binary search would only require 3 additional operations! (can you verify this?) That's the real difference between the complexities **O(N)** and **O(log N)**.\n",
    "\n",
    "Another way to look at it is that binary search runs  `c * N / log N` times faster than linear search, for some fixed constant `c`. Since `log N` grows very slowly compared to `N`, the difference gets larger with the size of the input. Here's a graph showing how the comparing common functions for running time of algorithms ([source](https://dev.to/b0nbon1/understanding-big-o-notation-with-javascript-25mc)):\n",
    "\n",
    "<img src=\"https://res.cloudinary.com/practicaldev/image/fetch/s--NR3M1nw8--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_880/https://thepracticaldev.s3.amazonaws.com/i/z4bbf8o1ly77wmkjdgge.png\" width=\"480\">\n",
    "\n",
    "Do you see now why we ignore constants and lower order terms while expressing the complexity using the Big O notation?"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "612ff085",
   "metadata": {},
   "source": [
    "## Generic Binary Search\n",
    "\n",
    "Here is the general strategy behind binary search, which is applicable to a variety of problems:\n",
    "\n",
    "1. Come up with a condition to determine whether the answer lies before, after or at a given position\n",
    "1. Retrieve the midpoint and the middle element of the list.\n",
    "2. If it is the answer, return the middle position as the answer.\n",
    "3. If answer lies before it, repeat the search with the first half of the list\n",
    "4. If the answer lies after it, repeat the search with the second half of the list.\n",
    "\n",
    "Here is the generic algorithm for binary search, implemented in Python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "6a7e7311",
   "metadata": {},
   "outputs": [],
   "source": [
    "def binary_search(lo, hi, condition):\n",
    "    \"\"\"TODO - add docs\"\"\"\n",
    "    while lo <= hi:\n",
    "        mid = (lo + hi) // 2\n",
    "        result = condition(mid)\n",
    "        if result == 'found':\n",
    "            return mid\n",
    "        elif result == 'left':\n",
    "            hi = mid - 1\n",
    "        else:\n",
    "            lo = mid + 1\n",
    "    return -1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae09fd4a",
   "metadata": {},
   "source": [
    "The worst-case complexity or running time of binary search is **O(log N)**, provided the complexity of the condition used to determine whether the answer lies before, after or at a given position is **O(1)**.\n",
    "\n",
    "Note that `binary_search` accepts a function `condition` as an argument. Python allows passing functions as arguments to other functions, unlike C++ and Java.\n",
    "\n",
    "We can now rewrite the `locate_card` function more succinctly using the `binary_search` function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "5896718c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def locate_card(cards, query):\n",
    "    \n",
    "    def condition(mid):\n",
    "        if cards[mid] == query:\n",
    "            if mid > 0 and cards[mid-1] == query:\n",
    "                return 'left'\n",
    "            else:\n",
    "                return 'found'\n",
    "        elif cards[mid] < query:\n",
    "            return 'left'\n",
    "        else:\n",
    "            return 'right'\n",
    "    \n",
    "    return binary_search(0, len(cards) - 1, condition)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c25c5883",
   "metadata": {},
   "source": [
    "Note here that we have defined a function within a function, another handy feature in Python. And the inner function can access the variables within the outer function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "1f0adad1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "\u001b[1mTEST CASE #0\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.01 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #1\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}\n",
      "\n",
      "Expected Output:\n",
      "6\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "6\n",
      "\n",
      "Execution Time:\n",
      "0.007 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #2\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [4, 2, 1, -1], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.005 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #3\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [3, -1, -9, -127], 'query': -127}\n",
      "\n",
      "Expected Output:\n",
      "3\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "3\n",
      "\n",
      "Execution Time:\n",
      "0.006 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #4\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [6], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "0\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "0\n",
      "\n",
      "Execution Time:\n",
      "0.003 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #5\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [9, 7, 5, 2, -9], 'query': 4}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.009 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #6\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [], 'query': 7}\n",
      "\n",
      "Expected Output:\n",
      "-1\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "-1\n",
      "\n",
      "Execution Time:\n",
      "0.004 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #7\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}\n",
      "\n",
      "Expected Output:\n",
      "7\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "7\n",
      "\n",
      "Execution Time:\n",
      "0.006 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mTEST CASE #8\u001b[0m\n",
      "\n",
      "Input:\n",
      "{'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 6}\n",
      "\n",
      "Expected Output:\n",
      "2\n",
      "\n",
      "\n",
      "Actual Output:\n",
      "2\n",
      "\n",
      "Execution Time:\n",
      "0.006 ms\n",
      "\n",
      "Test Result:\n",
      "\u001b[92mPASSED\u001b[0m\n",
      "\n",
      "\n",
      "\u001b[1mSUMMARY\u001b[0m\n",
      "\n",
      "TOTAL: 9, \u001b[92mPASSED\u001b[0m: 9, \u001b[91mFAILED\u001b[0m: 0\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[(3, True, 0.01),\n",
       " (6, True, 0.007),\n",
       " (0, True, 0.005),\n",
       " (3, True, 0.006),\n",
       " (0, True, 0.003),\n",
       " (-1, True, 0.009),\n",
       " (-1, True, 0.004),\n",
       " (7, True, 0.006),\n",
       " (2, True, 0.006)]"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "evaluate_test_cases(locate_card, tests)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6f135a3",
   "metadata": {},
   "source": [
    "The `binary_search` function can now be used to solve other problems too. It is a tested piece of logic.\n",
    "\n",
    "\n",
    "> **Question**: Given an array of integers nums sorted in ascending order, find the starting and ending position of a given number. \n",
    "\n",
    "This differs from the problem in only two significant ways:\n",
    "\n",
    "1. The numbers are sorted in increasing order.\n",
    "2. We are looking for both the increasing order and the decreasing order.\n",
    "\n",
    "Here's the full code for solving the question, obtained by making minor modifications to our previous function:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "193f4111",
   "metadata": {},
   "outputs": [],
   "source": [
    "def first_position(nums, target):\n",
    "    def condition(mid):\n",
    "        if nums[mid] == target:\n",
    "            if mid > 0 and nums[mid-1] == target:\n",
    "                return 'left'\n",
    "            return 'found'\n",
    "        elif nums[mid] < target:\n",
    "            return 'right'\n",
    "        else:\n",
    "            return 'left'\n",
    "    return binary_search(0, len(nums)-1, condition)\n",
    "\n",
    "def last_position(nums, target):\n",
    "    def condition(mid):\n",
    "        if nums[mid] == target:\n",
    "            if mid < len(nums)-1 and nums[mid+1] == target:\n",
    "                return 'right'\n",
    "            return 'found'\n",
    "        elif nums[mid] < target:\n",
    "            return 'right'\n",
    "        else:\n",
    "            return 'left'\n",
    "    return binary_search(0, len(nums)-1, condition)\n",
    "\n",
    "def first_and_last_position(nums, target):\n",
    "    return first_position(nums, target), last_position(nums, target)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c20eb2e3",
   "metadata": {},
   "source": [
    "We can test our solution by making a submission here: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8854458b",
   "metadata": {},
   "source": [
    "## The Method - Revisited\n",
    "\n",
    "Here's a systematic strategy we've applied for solving the problem:\n",
    "\n",
    "1. State the problem clearly. Identify the input & output formats.\n",
    "2. Come up with some example inputs & outputs. Try to cover all edge cases.\n",
    "3. Come up with a correct solution for the problem. State it in plain English.\n",
    "4. Implement the solution and test it using example inputs. Fix bugs, if any.\n",
    "5. Analyze the algorithm's complexity and identify inefficiencies, if any.\n",
    "6. Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.\n",
    "\n",
    "Use this template for solving problems using this method: https://jovian.ai/aakashns/python-problem-solving-template\n",
    "\n",
    "This seemingly obvious strategy will help you solve almost any programming problem you will face in an interview or coding assessment. \n",
    "\n",
    "The objective of this course is to rewire your brain to think using this method, by applying it over and over to different types of problems. This is a course about thinking about problems systematically and turning those thoughts into code."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f905bd0c",
   "metadata": {},
   "source": [
    "## Problems for Practice\n",
    "\n",
    "\n",
    "Here are some resources to learn more and find problems to practice. \n",
    "\n",
    "* Assignment on Binary Search: https://jovian.ai/aakashns/python-binary-search-assignment\n",
    "* Binary Search Problems on LeetCode: https://leetcode.com/problems/binary-search/\n",
    "* Binary Search Problems on GeeksForGeeks: https://www.geeksforgeeks.org/binary-search/\n",
    "* Binary Search Problems on Codeforces: https://codeforces.com/problemset?tags=binary+search\n",
    "\n",
    "Use this template for solving problems: https://jovian.ai/aakashns/python-problem-solving-template\n",
    "\n",
    "Start a discussion on the forum: https://jovian.ai/forum/c/data-structures-and-algorithms-in-python/lesson-1-binary-search-linked-lists-and-complex/81\n",
    "\n",
    "Try to solve at least 5-10 problems over the week to master binary search."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "5ad95cde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/javascript": [
       "window.require && require([\"base/js/namespace\"],function(Jupyter){Jupyter.notebook.save_checkpoint()})"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[jovian] Attempting to save notebook..\u001b[0m\n",
      "[jovian] Updating notebook \"aakashns/python-binary-search\" on https://jovian.ai/\u001b[0m\n",
      "[jovian] Uploading notebook..\u001b[0m\n",
      "[jovian] Capturing environment..\u001b[0m\n",
      "[jovian] Committed successfully! https://jovian.ai/aakashns/python-binary-search\u001b[0m\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'https://jovian.ai/aakashns/python-binary-search'"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "jovian.commit()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
