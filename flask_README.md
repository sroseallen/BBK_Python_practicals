# Getting started
To run the server:
- install flask in your local environment
- download the file `flask_server.py`

then start the server using:
`flask --app flask_server run`

# Practical: implementing your own webserver functions
once you have the server running,
try to complete the following:
- finish the seq_complement function so that it returns the complementary dna sequence to the one provided, using biopython
- write a function so that going to localhost:5000/time shows the current time
- write a function so that going to localhost:5000/bold/<text> returns the provided text in bold (see: https://www.w3schools.com/html/html_formatting.asp)
- write a function that returns the composition of a provided sequence, (e.g. how many a, c, t, g, ...)
    - write the results in an html table: https://www.w3schools.com/html/html_tables.asp
- write a function so that going to localhost:5000/package/listdir shows you the current directory content (consider using os or pathlib here)
- modify the previous function so that going to localhost:5000/package/listdir/<dirname> shows you the given directory's content