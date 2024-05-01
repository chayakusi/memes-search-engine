import os
from collections import defaultdict

def process_linkdb_data(linkdb_file_path):
    total_nodes = 0
    total_links = 0
    max_inlinks = 0
    max_outlinks = 0
    inlink_counts = defaultdict(int)
    outlink_counts = defaultdict(int)

    with open(linkdb_file_path, 'r', encoding='ISO-8859-2') as linkdb_file:
        for line in linkdb_file:
            # Process each line of the linkdb data
            # Here you can parse the line to extract relevant information
            # For example, you can split the line and extract URLs and inlinks

            # Increment total_nodes for each URL encountered
            total_nodes += 1

            # Count the number of inlinks for each URL
            inlinks = line.strip().split('\t')[-1].split(',')
            num_inlinks = len(inlinks)
            total_links += num_inlinks

            # Update max_inlinks if the current URL has more inlinks
            if num_inlinks > max_inlinks:
                max_inlinks = num_inlinks

            # Count the number of inlinks for each URL
            for inlink in inlinks:
                inlink_counts[inlink] += 1

            # Count the number of outlinks for each URL
            from_url = line.strip().split('\t')[0]
            outlink_counts[from_url] += 1

    # Calculate average number of inlinks per node
    avg_inlinks = total_links / total_nodes
    max_outlinks = max(outlink_counts.values())

    return total_nodes, total_links, max_inlinks, max_outlinks, avg_inlinks, inlink_counts

# Path to the linkdb data file
linkdb_file_path = 'C:/Users/chaya/Documents/apache-nutch-1.19/finalcrawl/linkdb/current/part-r-00000/data'

# Process the linkdb data file
total_nodes, total_links, max_inlinks, max_outlinks, avg_inlinks, inlink_counts = process_linkdb_data(linkdb_file_path)

# Display the statistics
print("Total number of nodes:", total_nodes)
print("Total number of links:", total_links)
print("Maximum number of inlinks:", max_inlinks)
print("Maximum number of outlinks:", max_outlinks)
print("Average number of inlinks per node:", avg_inlinks)