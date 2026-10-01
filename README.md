# Lossless Compression — Dictionary-Based Methods

A Python project that implements **Dictionary-Based Lossless Compression** algorithms.

This project was developed as part of the **Information Theory and Data Compression** course at the **Faculty of Computers and Artificial Intelligence, Cairo University**.

## Algorithms

The project implements:

* **LZ77**
* **LZ78**
* **LZW (Lempel–Ziv–Welch)**

## Lossless Compression

Lossless compression reduces the size of data while preserving the original information exactly.

After decompression, the original data can be reconstructed without any loss.

## Dictionary-Based Compression

Dictionary-based compression algorithms detect repeated patterns in the input and represent them using references to a dictionary of previously encountered patterns.

### LZ77

Uses a **sliding window** to find repeated sequences and represent them using references.

### LZ78

Builds a dictionary of previously encountered sequences and represents the input using dictionary indices.

### LZW

Builds a dictionary dynamically while processing the input and represents repeated sequences using dictionary indices.

## Technologies

This project uses:

Python — Programming language
CustomTkinter — GUI library for building the graphical user interface

## Course

**Information Theory and Data Compression**

Faculty of Computers and Artificial Intelligence
Cairo University

## Team

* **Alaa Mamdouh**
* **Yara Ayman**
* **Mariam Samy**