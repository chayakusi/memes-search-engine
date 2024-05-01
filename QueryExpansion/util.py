import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import WordNetLemmatizer
from string import punctuation

# Make sure to download necessary NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')


def tokenize_and_stem(text):
    # Load English stopwords
    english_stopwords = stopwords.words("english")

    # Convert text to lowercase
    text = text.lower()

    # Tokenize text
    tokens = wordpunct_tokenize(text)

    # Remove stopwords
    tokens = [token for token in tokens if token not in english_stopwords]

    # Remove punctuation
    tokens = [token for token in tokens if token not in punctuation]

    # Initialize the lemmatizer
    lemmatizer = WordNetLemmatizer()

    # Lemmatize the tokens
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    return lemmatized_tokens



def process_documents(all_docs):
    """
    Processes documents to extract content and IDs, tokenizes the content,
    and organizes tokens by document IDs.

    Parameters:
    - all_docs: A dictionary containing all documents.
    - query: The search query string.
    - tokenize_and_stem: A function that tokenizes and stems a given text.

    Returns:
    - tokens: A list of all tokens from all documents.
    - doc_dict: A dictionary with document IDs as keys and token lists as values.
    """
    # Extract content and IDs from each document if they have 'content' and 'id' fields
    # Assuming 'documents' is the array of document dictionaries
    main_content = [doc['content'] for doc in all_docs if 'content' in doc]
    main_ids = [doc['id'] for doc in all_docs if 'content' in doc]

    # Initialize tokens list and doc dictionary
    tokens = []
    doc_dict = {}

    # Iterate over each document's content and corresponding ID
    for content, doc_id in zip(main_content, main_ids):
        # Tokenize and stem the document content
        doc_tokens = tokenize_and_stem(content)

        # Store the tokens in the dictionary with the document ID as the key
        doc_dict[doc_id] = doc_tokens

        # Extend the main token list with the tokens from this document
        tokens.extend(doc_tokens)

    return tokens, doc_dict


def tuple_to_string(tup):
    """
    Converts a tuple of strings into a single string, with each element separated by a space.

    Parameters:
    tup (tuple): A tuple containing string elements.

    Returns:
    str: A single string made by concatenating all elements of the tuple, separated by spaces.
    """
    new_str = ""
    for i in range(len(tup)):
        new_str = new_str + str(tup[i])
    new_string = re.sub(r'[^a-zA-Z0-9 ]', '', new_str)
    return new_string

