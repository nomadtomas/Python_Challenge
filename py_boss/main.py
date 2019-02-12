import csv
import os

fname = os.path.join('employee_data.csv')

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

with open('employees_formatted_data.csv', 'w', newline="") as wf:
    fieldnames = ["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"]
    csvwriter = csv.DictWriter(wf,fieldnames= fieldnames, delimiter=",")
    
    csvwriter.writeheader()
    
    with open('employee_data.csv', 'r') as cr:
        csv_reader = csv.DictReader(cr)
        
        for i in csv_reader:
            output_row = {}
            output_row['Emp ID'] = i['Emp ID']
            output_row['First Name'], output_row['Last Name'] = i['Name'].split(' ')
            output_row['DOB'] =i["DOB"] 
            output_row['SSN'] ="XXX-XX-" + i['SSN'][slice(7,12)]
            
            for k, val in states.items():
                if i['State'].strip().lower() == val.lower():
                    output_row['State'] = k
        
            csvwriter.writerow(output_row)