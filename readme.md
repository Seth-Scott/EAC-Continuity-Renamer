# EAC Continuity Renamer

EAC Continuity Renamer is a Python script designed to simplify the renaming of audio files, particularly for users of Exact Audio Copy (EAC) when ripping audio CDs. This tool ensures a seamless continuation of the naming schema when EAC enforces a restart of track numbering.

## Overview

Exact Audio Copy (EAC) is a widely used program for ripping audio CDs. EAC provides an option to use the last track number from a previous CD as a starting point for the current CD. However, it imposes a maximum number of tracks before requiring a restart of the numbering scheme. In such cases, EAC allows you to continue the naming schema from where you left off. The EAC Continuity Renamer script complements this functionality.

## Features

- User-Defined Starting Number: EAC Continuity Renamer allows you to specify the starting number for renaming audio files. This feature ensures that you can seamlessly continue the numbering scheme in alignment with EAC's behavior.

- Numerical Sorting: The script uses custom sorting to process files in the correct numerical order, avoiding issues where filenames jump from 10 to 100 or similar anomalies.

- Log File Generation: EAC Continuity Renamer generates a log file (rename_log.txt) that records the original and new filenames, providing a convenient record of the renaming process.

## Usage

1. Clone this repository to your local machine.

2. Place your audio files in the files folder.

3. Run the Python script and follow the prompts:

   ```bash
   python renamer.py

Specify the starting number for renaming, ensuring it aligns with your EAC numbering scheme.

The script will rename the files in the renamed folder and generate a log file (rename_log.txt) in the same directory.

## Prerequisites

- Python 3.x

## Example

Here's an example of the renaming process:

Original Filename > New Filename

```
01 Track01.wav > 991 Track01.wav
02 Track02.wav > 992 Track02.wav
03 Track03.wav > 993 Track03.wav
04 Track04.wav > 994 Track04.wav
```