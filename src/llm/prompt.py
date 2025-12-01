PROMPT = """
You are validating whether a customer search query correctly matches a product

## QUERY
{query}

## PRODUCT INFORMATION
Title: {title}
Brand: {brand}
Description: {description}
Bullet Points: {bullets}

Evalaute whether there is a match based on the following steps:
1. Identify all explicit specifications in the query
2. Compare each specification against the product information provided.
3. If the product explicitly contradicts any part of the query, the match is incorrect.
4. If the product does not mention a specification from the query, the match is still correct.
5. If the product contains additional details beyond the query, the match is still correct.
6. Based on all these rules, decide whether the query and the product are a match.

If there is no correct match, reformulate the old query into a corrected query. Keep the corrected query in similar format
and detail to the original query. Do not add unncessary details to the corrected query, keep the information the same amount
as the original query. 

You must provide values for:
- is_match_correct (boolean)
- corrected_query (string; empty if match is correct)
"""