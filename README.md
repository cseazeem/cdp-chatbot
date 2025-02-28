# CDP Chatbot Project

A support agent chatbot built to answer "how-to" questions for Customer Data Platforms (CDPs) including **Segment**, **mParticle**, **Lytics**, and **Zeotap**. This project uses **Spring Boot** for the backend REST API, **Python** for web scraping and question processing, and **PostgreSQL** for storing documentation data. It fulfills Assignment 2 requirements for the Software Engineer Intern position at Zeotap.

---

## Project Overview

### Objective
The chatbot answers user queries like:
- "How do I set up a new source in Segment?"
- "How can I create a user profile in mParticle?"
- "How do I build an audience segment in Lytics?"
- "How can I integrate my data with Zeotap?"

It fetches relevant information from official CDP documentation and provides step-by-step guidance.

### Data Sources
- Segment: [https://segment.com/docs/](https://segment.com/docs/)
- mParticle: [https://docs.mparticle.com/](https://docs.mparticle.com/)
- Lytics: [https://docs.lytics.com/](https://docs.lytics.com/)
- Zeotap: [https://docs.zeotap.com/home/en-us/](https://docs.zeotap.com/home/en-us/)

---

## Project Structure
cdp-chatbot/
├── cdp-chatbot/              # Spring Boot backend
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/supportchatbot/cdp/
│   │   │   │   ├── controller/    # REST API endpoints
│   │   │   │   ├── model/         # JPA entities
│   │   │   │   └── repository/    # Database repositories
│   │   │   └── resources/         # Configs & static files
│   │   └── test/                  # Unit tests
│   ├── pom.xml                    # Maven dependencies
│   └── target/                    # Build output
├── python-scripts/           # Python scripts
│   ├── scrape_docs.py        # Scrapes CDP documentation
│   ├── process_question.py   # Processes user questions
│   └── requirements.txt      # Python dependencies
├── database/                 # Database setup
│   └── init.sql              # SQL script for table creation
├── .gitignore                # Git ignore file
└── README.md                 # This file



---

## Core Functionalities

1. **Answering "How-to" Questions**:
   - Understands user queries related to the four CDPs.
   - Extracts steps or instructions from stored documentation.

2. **Documentation Extraction**:
   - Scrapes content from official CDP docs using Python.
Flower
   - Stores data in PostgreSQL for quick retrieval.

3. **Handling Question Variations**:
   - Works with long/short queries (e.g., "How do I set up a source in Segment step-by-step?").
   - Responds to irrelevant questions with "Sorry, I can only help with CDP-related queries."

---

## Bonus Features

1. **Cross-CDP Comparisons** (Planned):
   - Example: "How does Segment's audience creation compare to Lytics?"
   - Note: Partially implemented in `process_question.py` (keyword detection).

2. **Advanced "How-to" Questions** (Planned):
   - Supports complex queries like integrations or configurations.
   - Limited by current scraping depth—can be enhanced with sub-page crawling.

---

## Setup Instructions

### Prerequisites
- **Java 17+**: For Spring Boot.
- **Python 3.11+**: For scraping and processing.
- **PostgreSQL 15+**: For data storage.
- **Maven**: For building Spring Boot.
- **Git**: For cloning the repository.

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone git https://github.com/cseazeem/cdp-chatbot.git
cd cdp-chatbot


---

## Core Functionalities

1. **Answering "How-to" Questions**:
   - Understands user queries related to the four CDPs.
   - Extracts steps or instructions from stored documentation.

2. **Documentation Extraction**:
   - Scrapes content from official CDP docs using Python.
Flower
   - Stores data in PostgreSQL for quick retrieval.

3. **Handling Question Variations**:
   - Works with long/short queries (e.g., "How do I set up a source in Segment step-by-step?").
   - Responds to irrelevant questions with "Sorry, I can only help with CDP-related queries."

---

## Bonus Features

1. **Cross-CDP Comparisons** (Planned):
   - Example: "How does Segment's audience creation compare to Lytics?"
   - Note: Partially implemented in `process_question.py` (keyword detection).

2. **Advanced "How-to" Questions** (Planned):
   - Supports complex queries like integrations or configurations.
   - Limited by current scraping depth—can be enhanced with sub-page crawling.

---

## Setup Instructions

### Prerequisites
- **Java 17+**: For Spring Boot.
- **Python 3.11+**: For scraping and processing.
- **PostgreSQL 15+**: For data storage.
- **Maven**: For building Spring Boot.
- **Git**: For cloning the repository.

### Step-by-Step Setup

#### 1. Clone the Repository
```bash
git clone git https://github.com/cseazeem/cdp-chatbot.git
cd cdp-chatbot

2. Database Setup
Install PostgreSQL and start the server.
Create a database:


psql -U postgres -c "CREATE DATABASE cdp_chatbot;"







