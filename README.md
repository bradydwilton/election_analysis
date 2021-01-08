# Election Audit: Coloardo Board of Elections

## Overview of Election Audit

The Colorado Board of Elections has requested an audit to verify the results of a recent election. A CSV file containing the voter ID, voter's county, and selected candidate of all votes cast in the election was provided for the analysis. Python was then used to read the CSV file and quantify several statistics regarding the election, including both the number of votes received by each candidate and the number cast in each county. After performing the analysis, the results are output to both the terminal and to a text file.

## Election Audit Results
__The results of the election are as follows:__

<pre>
- Total votes:                      369,711

- Votes by County
    - Jefferson:                    38,855 (10.5%)
    - Denver:                       306,055 (82.8%)
    - Arapahoe:                     24,801 (6.7%)
    
- County with most votes:           Denver

- Votes by Candidate
    - Charles Casper Stockham:      85,213 (23.0%)
    - Diana DeGette:                272,892 (73.8%)
    - Raymon Anthony Doane:         11,606 (3.1%)
    
- Winning Candidate:                Diana DeGette (272,892 votes, 73% of total)
</pre>
###### _**A copy of the results above can be viewed and downloaded [here](https://github.com/bradydwilton/election_analysis/blob/main/analysis/election_analysis.txt).**_

## Election-Audit Summary
In summary, the software created for this election audit has confirmed the winner of the election to be Diana DeGette, with 73.8% of the total votes cast. The majority of votes cast came from Denver county, from which 306,055 of the 369,711 total votes were cast. 

Going forward, a commercial version of software can be appled to any election at any level with only slight modifications. The first modification would be to allow for information to be passed to the script regarding the details of the election, such as jurisdiction, term, and date. This could be done either by reading information from a file (similar to how the votes are read in) or by utilizing input boxes at the beginning of the script. Below shows the additional code needed to gather election details via user input at the beginning of the script:

``` py
    # Gather information regarding the election:
    election_jurisdiction = input("Enter the jurisdiction of the election: ")
    election_position = input("Enter the position being elected: ")
    election_term = input("Enter the term length (in number of years) to be served by the elected candidate: ")
    election_date = input("Enter the date (mm/dd/yyyy) of the election: ")
```

The second modification would use the create a formal output more robust than what was created for this election. The new report would include the same information shown in the current [output text file](https://github.com/bradydwilton/election_analysis/blob/main/analysis/election_analysis.txt), but would also include the information regarding the election gathered at the beginning of the script, as well as a signature line at the bottom to allow for the report to be formally verified via signature by the body governing the election. A possible template for the new output file is shown [here](https://github.com/bradydwilton/election_analysis/blob/main/analysis/modified_election_analysis.txt). The modifications shown above are examples of the flexibility and customization of this software and are not meant to be the final commercial product. Prior to commercial use, the script would be modified to include any additional details requested and the output report customized to meet the needs of the election board.
