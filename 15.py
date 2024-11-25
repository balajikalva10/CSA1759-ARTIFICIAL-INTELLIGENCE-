import math

# Function to calculate entropy of a dataset
def entropy(data):
    total = len(data)
    value_counts = {}
    
    # Count occurrences of each class in the data
    for record in data:
        label = record[-1]  # The last element is the class label
        value_counts[label] = value_counts.get(label, 0) + 1

    # Calculate entropy using the formula
    ent = 0
    for count in value_counts.values():
        prob = count / total
        ent -= prob * math.log2(prob)
    
    return ent

# Function to calculate information gain of a dataset
def information_gain(data, feature_index):
    total_entropy = entropy(data)
    feature_values = {}
    
    # Group data by feature values
    for record in data:
        feature_value = record[feature_index]
        if feature_value not in feature_values:
            feature_values[feature_value] = []
        feature_values[feature_value].append(record)

    # Calculate weighted average entropy after splitting the data based on the feature
    weighted_entropy = 0
    for subset in feature_values.values():
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)
    
    # Information gain is the reduction in entropy
    return total_entropy - weighted_entropy

# Function to choose the best feature to split on
def best_split(data):
    best_feature = -1
    best_gain = -1
    
    # Loop through all features to find the one with the highest information gain
    num_features = len(data[0]) - 1  # The last column is the class label, not a feature
    for feature_index in range(num_features):
        gain = information_gain(data, feature_index)
        if gain > best_gain:
            best_gain = gain
            best_feature = feature_index
    
    return best_feature

# Function to build the decision tree
def build_tree(data):
    if len(data) == 0:
        return None

    # If all records have the same class, return that class as the leaf node
    classes = [record[-1] for record in data]
    if len(set(classes)) == 1:
        return classes[0]
    
    # Choose the best feature to split on
    best_feature = best_split(data)

    # If no feature gives any information gain, return the majority class
    if best_feature == -1:
        return max(classes, key=classes.count)

    # Create the tree node with the best feature
    tree = {best_feature: {}}
    feature_values = {}

    # Group the data by feature value
    for record in data:
        feature_value = record[best_feature]
        if feature_value not in feature_values:
            feature_values[feature_value] = []
        feature_values[feature_value].append(record)
    
    # Recursively build the tree for each feature value
    for feature_value, subset in feature_values.items():
        tree[best_feature][feature_value] = build_tree(subset)
    
    return tree

# Function to classify a record using the decision tree
def classify(tree, record):
    if not isinstance(tree, dict):
        return tree
    
    feature_index = list(tree.keys())[0]
    feature_value = record[feature_index]
    
    return classify(tree[feature_index].get(feature_value), record)

# Sample dataset: each record is [feature1, feature2, ..., featureN, label]
dataset = [
    [1, 1, 'Yes'],
    [1, 0, 'No'],
    [0, 1, 'Yes'],
    [0, 0, 'No'],
    [1, 1, 'Yes'],
    [0, 1, 'Yes'],
    [0, 0, 'No']
]

# Build the decision tree
tree = build_tree(dataset)

# Print the decision tree
print("Decision Tree:", tree)

# Classify a new record using the decision tree
new_record = [1, 0]
prediction = classify(tree, new_record)
print(f"Prediction for {new_record}: {prediction}")
