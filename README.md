# Slack/Discord Channel Namer

Often(?) clubs or societies have conventions for a dedicated communications channel in their servers that will be named after a member from each year, for example [#a-b-c-d]() where _a_ is a fourth year student, _b_ is a third year student etc

This is a python script to make finding appropiate names for these channels easier. As this was made for a very specific use-case it also requires a very specific format to be used.

## Usage

1. A directory structure is followed with names being stored in `csv` files, and each file being named after the year of admission. The files must be placed in a `Contacts` folder as shown below.

```sh
.
├── name_gen.py
├── requirements.txt
├── Contacts
│   ├── 2019.csv
│   ├── 2020.csv
│   ├── 2021.csv
│   ├── 2022.csv
│   ├── 2023.csv
│   ├── 2024.csv
```

2. Each `csv` file must have a column named **"Name"** containing the names of the members of that year.

> [!CAUTION] 
> not "name" or "names" or "Names" but "**Name**"

3. Install the requirements. This script uses [`english_words`](https://pypi.org/project/english-words/) to compare the bruteforced results against some common english words and [`pandas`](https://pandas.pydata.org/pandas-docs/stable/index.html) to read the `csv` files

```sh
pip install -r requirements.txt
```

4. Run the script from the root of the repo and pick a funny name :)

```sh
python name_gen.py > results.txt
```

## Further

I might make this more modular/general-purpose in the future if literally anyone shows any interest in using this, until then it exists for my specific use-case

Thank you [@SachdevJai](https://github.com/SachdevJai) naisu inspiration
