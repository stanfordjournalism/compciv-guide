# Todos

### Tool-crafting

- howoldami
- Upload to S3 via boto
- Text messaging
- Twitter botting
- Command-line text filtering
- Frequency counter: pattern, exact match, count
- 404-finder
- Bitly-converter
- Making a command-line package
- Twitter authenticator
- Google street view mapper
- Google translator
- Wikipedia population counter
- Beautiful screenmaking
- Youtube-to-Giffer
- My weather forecast


## New structure


- exercises
- routines (groups of exercises)
  - vertical
    - bash: Calculate New York Times revenues per Congressmember
    - python
    - python-cli
    - matplotlib
    - flask
    - flask-frozen
 
  - horizontal
    - Understanding regular expressions and command-line grep
    - csvcut

  - topical
    - Congressional expenditures
    - Campaign Finance Contributions



--------------
Example routine:


exercises:
  routines:
  standalone:
  





- vertical:

  Goldman Sachs Pie
  - point-and-click: 
    bash: regex only
    bash: csvcut, regex
    bash: regex, curl, multi-year
    bash: gnuplot
    bash: auto-webpage maker
    python: regex only
    python: csv + regex
    python: multiyear, requests
    python: pandas/matplotlib
    python: cli-interface
    python: web app

  Congressional-gender

  - bash ack
  - bash bioguide scrape?
  - Python: YAML to CSV data-wrangle
  - Python: YAML full object orientation
  - Python: Baseplotmap map
  - Python GMAps api

  Show me earthquakes this hour

  - Bash: earthquakes this hour, naive regex, ack printing
  - Bash: ack, csvcut
  - Python: regex only
  - Python: regex-plus-csv
  - Python: json parsing
  - Python: make google static map
  - Python: cli-interface
  - Flask app
  - AWS texter

  Earthquakes this big
  - Bash
  - Python regex only
  

  Name-popularity

  - Bash: bc, ack
  - Bash with cli
  - Python interactive
  - Python CLI argument count
  - Python argparse
  - Python chartmaker
  - Python wrangle
  - Python pandas
  - Python datasets/SQL
  - Flask app



- Verticals
  - CLI: How long until I die?
  - Python:
  - Python-with-data
    - life-expectancy-graph
  - CLI: How long until you die?


- horizontals:

  regex-and-ack
  - goldman sachs calculate
  - benfords-law
  - earthquake filter

  data-parsing and regex
  - 


- topical:
  - FEC campaign finance

Earthquakes



----------

end-user-software

data-markup-specs
- html
- css
- Markdown
- JSON
- csv
- YAML
- use pandoc

regex/
  syntax
    - +
    - *
    - ?
    - .
    - ^
    - $
    - |
    - [sets]
    - {min, max}
    - (token)
    - (?:token)
    - (?!token)
    - (?=token)
    - (?<=token)
    - (?!=token)
  shorthand
    - \b
    - \d
    - \D
    - \s
    - \n
    - \w
    - \W
    - \t
    - \1
    - $1

aws/
  commands/
    s3/
      cp
      sync
    rekognize
    sns


command-line/
  directory-structure.rst
  file-handling.rst
  stdout-stdin.rst
    syntax
      - |
      - $variable
      - ${variable}
      - $(command)
      - >>
      - >
      - <
      - =
      - &
      - *
      - ..
      - .
      - ~
      - /
      - whitespace
      - newlines


    non-standard/
      - ack
      - in2csv
      - convert
      - csvcut
      - csvgrep
      - csvsql
      - csvstack
      - csvsort
      - sqlite3
      - youtube-dl
      - ffmpeg
      - curl
      - wget
      - mdfind
      - whois
      - openssl
      - cowsay
      - tesseract
      - ffmpeg



      - pdftotext
      - pbpaste
      - pbcopy
      - screencapture
      - open
      - say



remote-login:
  - ssh
  - scp
  - rsync
  

fundamental-python/
    binary-operators
      arithmetic
      assignment
      comparison
      logical
    control-flow
      if
      elif
      else
    functions
      range
      type
    types
      str
      dict
      list
      int
      bool
    operators
      - parentheses
      - brackets




  standard-library/
    imports
      datettime


  third-party
    libraries


  Sorting
  Time
    datettime
    strptime



---------

# The Unix system

- File system
  - /tmp
  - /dev/null


# Bash


# Data serialization



# The Python Shell and Interpreter

- python from the command line
  - common flags
    - --version, -V
    - --help, -h
    - --cmd, -c
      python -c 'print("hello world")'
    - --mod, -m

- ipython
  - Tab to autocomplete
  - Magic commands
  - Keyboard shortcuts
  - help
  - ?



# Python Language Fundamentals

- Syntax
  - whitespace
  - indentation
  - semicolon
  - parentheses for continuation


- Simple Types
    - Numbers
    - Strings
    - Booleans

- Binary operators
  - Arithmetic
    - Addition
    - Subtraction
    - Multiplication
    - Division
      - Integer division
    - Modulus
    - Exponent

  - Comparison
    - ==
    - !=
    - >, <
    - >=, <=

  - Assignment operators (read after variables)
    -


    - keywords
- Variables
  - Assignment operator
  - Naming conventions
  - Purpose


- Methods
  - the dot operator
  - Number methods
  - String methods

- Functions

  - What is a function?
  - print()
  - type()
  - Basic Function definition
      + def
      + function name
      + argument list
      + body
      + indentation
      + return
  - Argument lists
    - Default arguments https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
    - Keyword arguments
  - Function scope

- Loops
  - While loop
  - For loop
  - break
  - continue

- Conditional statements
  - If
  - Else
  - elif
  - pass
  - inline if/else

- Input/output
  - open
  - read
    - read()
    - readlines()
  - write

- Datetime and Time
  The only library/module to have its own major section: https://medium.com/@timrwood/moment-endof-term-522d8965689#.fcp4wxmxw
  - sleep
  - now
  - timezones


- Data structures
  - Lists
    + append
    + extend
    + zip
  - Dictionaries
    + get
    + update
    + keys
    + values
    + items
  - Tuples
  - Mutability and immutability



# Real-world Python

- Importing libraries
  - import
  - from

- Argument lists, advanced
  - Unpacking https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

- Iterations, enumerations, and comprehensions

  - Sorting
    - sort
    - sorted (mutability)
    - lambda https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
    - itemgetter
  - List comprehensions
  - Dictionary Comprehensions
  - Complex loops
  - Inline conditionals

- File/IO
  - with
  - csv

- Command-line interfaces
  - if name == __main__
  - sys.argv

- Error handling

- Style and documentation
  - docstrings
  -

# Remote login
- scp
- ssh
- logout
  ## Exercises
  - Downloading a cat photo into your Stanford web space
  - Uploading a cat photo onto Stanford
  - Making a webpage on Stanford



# Data serialization
  - CSV.reader
  - CSV.writer
  - CSV.DictReader
  - CSV.DictWriter
  - JSON
  - XML
  - Other libraries: Pickle, Yaml.
    For reasons that will make your future employer scream, I don't take the time to cover the general purpose Pickle library.



# Python Standard Libraries

- Path

- DateTime
  - datetime.now
    - the Epoch
  - strptime
  - strftime
  - pytz
    - naive timezones


- re (regular expressions)
  - match
  - compile

- argparse


- string https://docs.python.org/3/library/string.html
  - constants
    - ascii_letters
    - ascii_lowercase
    - ascii_uppercase
    - whitespace
    - punctuation
  - helper functions
    - capwords
  - Template
    - substitute



- Path and filesystem

- shutil
- Datetime
- collections
- webbrowser
- urllib (for FTP)
  - urlencode
  - urlunparse
  - urljoin
  -


# Python Third Party Libraries

- xlrd
- dateutil https://dateutil.readthedocs.io/en/stable/
  - rrule https://dateutil.readthedocs.io/en/stable/examples.html
  - parse
  - 
- PIL
- Requests
- pytz
- python-dateutils

# Python Web Development with Flask


# Style guide for humans

- Guides
  - https://www.python.org/dev/peps/pep-0008/
  - https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style

- 4 spaces for indentation
  - Silicon Valley
- 79-character limit https://www.python.org/dev/peps/pep-0008/#maximum-line-length
  - history of terminal windows
  - parentheses for long expressions
  - line breaks before binary operators https://www.python.org/dev/peps/pep-0008/#should-a-line-break-before-or-after-a-binary-operator
  - Alignment of multilines

- Avoid trailing whitespace
  - Atom has it automatically configured
- Whitespace in arguments and operators
  - always use whitespace around binary operators
- Use snakecase


-------------------------

# The World of HTTP Connections

- Everything I know about HTTP I learned from Curl
- Running a local server
- APIs
- Webscraping






# Real-world exercises

- Make a funky-dancing gif
- Time-lapse of Obama speech
- Cabinet-Lobbyist matchup

- Time-lapse of Clinton/Trump debate
https://www.youtube.com/watch?v=VLdmEDOAA4A

- Happy Trump/Clinton


- Decoding bit.ly links on Twitter
  - curl
  - requests

- Benford Law
  - bash
    - https://github.com/helloworlddata/us-presidential-election-county-results
    - csvcut -c vote_rep us-presidential-election-county-results-2004-through-2012.csv | ack -o '^\d' | sort | uniq -c
      - use csvgrep to filter by year

- Shakespeare word count
- pbpaste to pbcopy, amazon to smile
- Build a Gutenberg spellcheck

- Caesar Cipher

- FEC Data Dive

- translate earthquake data into localtime
  - datetime
  - csv

- Find earthquakes local to me
  - exercise: translate earthquake data into localtime
  - argparse

- translate Twitter timestamps
  - datetime
  - json

- Translate from Google Chrome database
  - datetime

- Free lunch at Stanford

- Next to die: Texas
- Next to die: Death Penalty Center
- Next to die: Florida

- Geocoding NYPD stop and frisks
- Classifying NYPD stop and frisks, use of force
- Charting racial demographics

- Census data explorer
  - command-line invocation
  - compare two counties

- Find text in a document

- Name reconciliation of shooting victims

- Count up congressmembers
- Find congressmember with longest term
- Fix up NYPD timestamps, get an hourly time series


######## Prep

- Creat Github org compcivbox
- Create Github repo compcivbox.github.io
- compciv.gibhub.io/

# Datasets
  - path: data/us-presidential-election-county-results.csv
    source: https://github.com/helloworlddata/us-presidential-election-county-results
  - path: data/nypd-stop-and-frisks
  - path: data/sfpd-crime (raw)
  - path: data/oakland-crimes
  - deathpenaltycenter
  - fatal encounters
  - guardian
  - Washington Post shootings
  - Census county files
  - LA County shooting incidents  
  - Dallas shooting incidents
  - Chicago shooting incidents
  - Power 100
  - IMDB top 500
  - Congressmembers



# Samples


# Documents

- Clinton emails
- Press releases

# Mirrors

  - path: usa.analytics.gov
  - path: deathrow.tx.us
  - path: stanford.edu.calendar
  - path: nytimes/front page
  - path: nytimes/interview
  - twitter history search

# Apps
  - path: error-server
