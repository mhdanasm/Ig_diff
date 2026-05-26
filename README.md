# Instagram Followers vs Following Comparator

A simple Python tool to compare your Instagram **followers** and **following** lists using Instagram account export data.

This script helps you find:

- **People you follow who do not follow you back**
- **People who follow you but you do not follow back**

The tool parses Instagram-exported HTML files and compares usernames using Python and BeautifulSoup.

---

## Features

- Parses Instagram export HTML files
- Handles Instagram URL and username format inconsistencies
- Uses set operations for fast comparison
- Simple and lightweight

---

## Requirements

- Python 3.x


Install dependency using:

```bash
pip install -r requirements.txt
```

---

## Step 1: Export Your Instagram Data

You first need to export your Instagram account information.

### Export Steps

1. Open Instagram
2. Go to **Settings and Privacy**
3. Select **Accounts Center**
4. Go to **Your Information and Permissions**
5. Click **Download Your Information**
6. Choose:
   - **Some of your information**
   - Select:
     - Followers and Following
7. Choose:
   - Format: **HTML**
8. Submit the request and wait for Instagram to prepare the download.
9. Download and extract the ZIP file.

After extraction, locate:

```text
connections/
├── followers_and_following/
    ├── followers_1.html
    └── following.html
```

---

## Step 2: Clone This Repository

Clone the repository:

```bash
git clone <your-repo-url>
```

Move into the project folder:

```bash
cd <repo-folder>
```

---

## Step 3: Add Instagram Export Files

Copy:

```text
followers_1.html
following.html
```

into the same folder as the Python script.

Example:

```text
project/
├── compare_insta.py
├── requirements.txt
├── followers_1.html
└── following.html
```

---

## Step 4: Run the Script

Run:

```bash
python compare_insta.py
```

or on some Linux systems:

```bash
python3 compare_insta.py
```

---

## Example Output

```text
Not following you back:

user1
user2
user3

You don't follow back:

user4
user5
```

---

## How It Works

The script:

1. Parses Instagram HTML files using BeautifulSoup
2. Extracts usernames
3. Normalizes Instagram URL and username formats
4. Uses Python set difference operations:

```python
following - followers
followers - following
```

to compute the results.

---

## Privacy

This tool runs entirely **locally** on your machine.

Your Instagram data is **not uploaded** anywhere.

---

## Acknowledgment

This project was developed with assistance from a Large Language Model (LLM) for code generation and documentation support.