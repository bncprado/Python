# figurint out that...
# when you print X (iteration variable) outside the loop, it'll print the last item of the loop. Here's ChatGPT answer:
"""
The last line of code, print(x), prints the last item of list_a because it is outside the for loop. In Python, when a loop finishes iterating through all the elements in an iterable (in this case, list_a), the loop variable retains the value of the last element. Therefore, after the loop completes, x will hold the value of the last item in list_a. By calling print(x) outside the loop, it will print the final value of x, which corresponds to the last item in the list.
"""

attempts_per_year = [[1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020], 0]

for x in attempts_per_year:
    print (x)

print(x)

