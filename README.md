

# web scraper




# Features 

* Scrape a Wikipedia page and record which passages need citations.
m  E.g. History of Mexico has a few “citations needed”.
* web scraper  reports the number of citations needed.
*  web scraper identifies those cases AND include the relevant passage.
   E.g. Citation needed for “lorem spam and impsum eggs”
**Considering the “relevant passage” to be the parent element that contains the passage, often a paragraph element.**

# Implementation Notes

1- Count function is named get_citations_needed_count
    **get_citations_needed takes in a url and returns an integer**
2-  Report function is named get_citations_needed_report
    **get_citations_needed_report takes in a url and returns a string**
the string should be formatted with each citation needed on own line, in order found.
3- Module os  named scraper.py






<hr/>
    <p align="right">(<a href="#top">back to top</a>)</p>





  <br/><br/>

<p align="right">Ghaida Al Momani, Software Engineer</p>
<p align="right">Jordan, Amman</p>
  <p align="right">22, 14 APR </p>