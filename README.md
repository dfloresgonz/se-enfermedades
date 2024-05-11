# Expert System for Sickness Diagnosis

## Introduction
This Python project aims to create an expert system for diagnosing sicknesses based on symptoms and causes. The system provides users with information about various sicknesses, their symptoms, causes, and how they are related. By inputting symptoms, users can receive suggestions about possible sicknesses along with their corresponding causes.

## Features
1. **Sickness Database:** The system contains a fact base which serves as a database of common sicknesses, including information about their symptoms and causes.
2. **Symptom Matching:** Users can input their symptoms, and the system will match them with potential sicknesses.
3. **Cause Analysis:** The system provides insights into the causes of each sickness and how they relate to the exhibited symptoms.
4. **Command-Line Interface:** The interface is a command-line interface (CLI) designed to be intuitive, making it easy for users to input symptoms and receive relevant information. The `client.py` acts as a user interface with the expert system.

## Dependencies
- Python 3.x
- Libraries: pyke (for expert system logic), and any additional libraries specified in pyke's documentation page.

## Installation
1. Clone the repository: `git clone https://github.com/dfloresgonz/se-enfermedades.git`
2. Delete the `compiled_krb/` directory to build a fresh one.
3. Run `python3 client.py` this will generate a new `compiled_krb` directory.

## Usage
1. Run the main Python script: `python3 client.py`
2. Follow the prompts to input symptoms.
3. Receive suggestions about possible sicknesses along with their causes.

## Example
Suppose a user inputs symptoms "low_fever, cough, nausea" into the system. The system may suggest sicknesses such as "Common Cold" or "Migraine" based on the matching symptoms. It will then provide information about the causes of each suggested sickness, such as viral infections, and how they manifest in the exhibited symptoms.

## UTEC AI fundamentals course
This is a project which is part of the AI fundamentals course in the Master program of Data science and artificial intelligence I'm part of, this is just meant for academic usage.

