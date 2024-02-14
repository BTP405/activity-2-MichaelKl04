import matplotlib.pyplot as plt

def graphSnowfall(t):
    with open (t, 'r') as file:
        snowfall_data = [int(line.strip()) for line in file] 
    #converts the lines to int, strips the line of whitespace, for loop of line
        
    ranges = {"0-10": 0, "11-20": 0, "21-30": 0, "31-40": 0, "41-50": 0}

    for snow in snowfall_data:
        if snow <= 10:
            ranges["0-10"] += 1
        elif snow <= 20:
            ranges["11-20"] += 1
        elif snow <= 30:
            ranges["21-30"] += 1
        elif snow <= 40:
            ranges["31-40"] += 1
        elif snow <= 50:
            ranges["41-50"] += 1

    plt.bar(ranges.keys(), ranges.values())
    plt.xlabel('Snowfall range (cm)')
    plt.ylabel('Occurrences')
    plt.title('Snowfall Distribution')
    plt.savefig('snowfall_data.png')



graphSnowfall('text.txt')
