import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Visualization function
def visualize_data(csv_filename):
    # Load the CSV file into a DataFrame
    df = pd.read_csv(csv_filename)
    
    # Visualization 1: Count of CVs per directory
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='directory', order=df['directory'].value_counts().index)
    plt.title('Count of CVs per Directory')
    plt.xlabel('Directory')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Visualization 2: Length of "Work Experience" text
    # Calculate the length of the "Work Experience" column for each CV
    df['Work Experience Length'] = df['Work Experience'].fillna('').apply(len)
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Work Experience Length'], bins=30, kde=True)
    plt.title('Distribution of Work Experience Text Lengths')
    plt.xlabel('Text Length')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()
    
    # Visualization 3: Presence of "Skills" in CVs
    # Check whether the "Skills" field is present (not null) in each CV
    df['Has Skills'] = df['Skills'].notna()
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='Has Skills')
    plt.title('Presence of Skills in CVs')
    plt.xlabel('Contains Skills')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
    
    # Visualization 4: Languages Mentioned
    # Calculate the number of languages mentioned in the "Languages" field
    df['Language Count'] = df['Languages'].fillna('').apply(lambda x: len(x.split(',')))
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Language Count'], bins=10, kde=False)
    plt.title('Number of Languages Mentioned')
    plt.xlabel('Number of Languages')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()
    
    # Visualization 5: Top Words in "Education"
    from collections import Counter
    from wordcloud import WordCloud
    import re

    # Combine all text in the "Education" field for analysis
    education_text = ' '.join(df['Education'].dropna())
    
    # Count word frequencies in the "Education" field
    word_counts = Counter(re.findall(r'\b\w+\b', education_text))
    
    # Generate a word cloud from the most common words
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
    
    # Display the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title('Top Words in Education Section')
    plt.axis('off')
    plt.show()

# Visualize the data from the CSV file
visualize_data("cv_data.csv")
