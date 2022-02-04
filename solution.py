import json

def Query_search(Query):
    start = 0
    Query_split = Query.split()
    phrase_list, sol = [], []
    while start < len(Query_split) - 1:
        sol.append(Query_split[start])
        sub_string = " ".join(sol)
        phrase = [phrase for phrase in P if sub_string in phrase]
        if not phrase:
            if start + 1 < len(Query_split):
                unmatched_word = sol.pop()
                sol.append(Query_split[start + 1])
                matched_phrase = " ".join(sol)
                if matched_phrase in P:
                    sol.insert(-1, unmatched_word)
                    matched_phrase = " ".join(sol)
                    phrase_list.append(matched_phrase)
            sol = []
        else:
            phrase = phrase[0].split()
            if len(sol) == len(phrase):
                if sol == phrase:
                    matched_phrase = " ".join(phrase)
                    phrase_list.append(matched_phrase)
                    sol = []
                    start += 1
        start += 1
    return phrase_list

def phrasel_search(P, Queries):
    # Write your solution here
    ans = []
    for Query in Queries:
        phrase_list = Query_search(Query)
        if phrase_list:
            ans.append(phrase_list)
    return ans

if __name__ == "__main__":
    with open('sample.json', 'r') as f:
        sample_data = json.loads(f.read())
        P, Queries = sample_data['phrases'], sample_data['queries']
        returned_ans = phrasel_search(P, Queries)
        if returned_ans == sample_data['solution']:
             print('returned',returned_ans,'\nsolution',sample_data['solution'])

        #print('============= ALL TEST PASSED SUCCESSFULLY ===============')