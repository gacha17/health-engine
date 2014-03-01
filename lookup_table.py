""" Reads recommendation table from disk and returns recommendations which meet the criteria 
described in the features"""

table = None # Stores all the recommendations

from features import Features

def lookup(features):
    
    keys = []
    recommendations = []
    
    # check if table is already loaded
    if 'table' in vars() or 'table' in globals():
        table = load_recommendations()
        for k in table.keys():
            print table[k]
    
    keys = make_keys(features)
    
    #TODO: Loop over the recommendations table and append the ones the meet the criteria in features
    # to recommendations list   
    '''    
    stub = {'feature0': feature[0], 'recommendation0': "Test recommendation" }
    stub = {'feature1': feature[1], 'recommendation1': "Test recommendation" }
    stub = {'feature2': feature[2], 'recommendation2': "Test recommendation" }

    recommendations.append(stub)
    '''
     
    return recommendations    

  

def make_keys(features):
    keys_temp = []
    bp_key = Features(features.bp_systolic_min, features.bp_systolic_max, features.bp_diastolic_min, 
                      features.bp_diastolic_max, None, None, None, None, None, None,
                 features.age_min, features.age_max)
    keys_temp.append(bp_key)
    
    #Todo: add more keys
    
    return keys_temp

def load_recommendations():
    table_temp = {};
    """ Reads the recommendations table from disk and returns it """
    import csv
    
    #Todo: add try block
    with open('recom.csv', 'rb') as f:
        reader = csv.reader(f)
        #Todo: Check how many roles there 
        for row in reader:
          #  print row
            key = Features(row[1], row[2], row[3], row[4],
                 row[5], row[6], row[7], row[8], row[9], row[10],
                 row[11], row[12])
            table_temp[key] = row[13];
        #return "hello"
        return table_temp;
    
lookup();
