Kanji Acquaintance Detector

General Functionability
The tool will allow a user to upload text and csv files, and read from a vocabulary website, and get the number of distinct kanji that are exist there. This list of kanji could help the user determine how many kanji they know (or at least have acquaintance with), thus helping them assess their Japanese level (JLPT N1-5).
The tool also cross-checks with the official and latest Joyo Kanji list. This list was created by the government and includes daily use kanji. Therefore, it could also showcase kanji knowledge relevance.

Algorithm
The tool shall ask the user to first upload text files, then csv files and finally URLs.
It would then scan the documents and count how many distinct kanji there are, using a simple Python set to eliminate duplicates. As the scale is small (no more than 10k objects), a set would suffice.
For every kanji, a cross-check with the Joyo kanji would be conducted. Every Joyo kanji found would also be inserted into a second Joyo set.
Eventually, the algorithm will count both sets' size and deliver the results for the user.

Input & Outputs:
Inputs: filepaths (txt, csv, URL)
Outputs: number of acquainted kanji, number of such kanji that are on the Joyo list

Directory Structure
When thinking about the different functionalities of the project, we could observe a few:
1. Main file to handle application's runs, taking inputs and delivering outputs
Inputs: filepaths (txt, csv), URL addresses, Outputs: number of acquainted kanji, number of such kanji that are on the Joyo list
2. Reading from files (txt, csv) and processing data - a read file
Inputs: filepaths (txt, csv), Outputs: Total Kanji Set, Joyo Kanji Set
3. Reading from a website - HTTP request file
Inputs: URL, Outputs: Total Kanji Set, Joyo Kanji Set
4. Is Kanji function - helper file
Input: a kanji char, Output: Boolean (True or False)