# 3.2.8 Decsion Statements

def percent_of_votes():
    my_votes = int(input("How many votes did you get this election?"))
    total_votes = int(input("How many total votes were there?"))
    my_percent = my_votes / total_votes
    return my_percent


print(f"I received {100*percent_of_votes():.0f}% of the total vote.")
