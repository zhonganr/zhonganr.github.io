import re
import json


files = ["descriptors", "database", "model", "system"]

def match_pattern(contents):
    pattern = r"\.\. option::\s+([^\s]+)\s*?\((.+?)\)\s*$\s+([\w\W\s\n]+?)Default (?:is )?``(.+?)``\.?\s*$"
    return re.findall(pattern, contents, re.MULTILINE)


docs_contents = {fi:{} for fi in files}



for key in docs_contents: 

    with open(f'contents/ml/{key}.rst', 'r') as f:
        contents = f.read()
    
    match = match_pattern(contents)

    for m in match:
        if len(m)==4:

            doc_str = re.sub("\s{2,}", " ", m[2].replace('\n', ' '))
            docs_contents[key][m[0]] = {'type':m[1],
                        'doc string': doc_str,
                        'value': m[3].split("=")[-1]}
        else:
            print("Incorrect number of match. Found:", m)


with open('contents/docs_options.json', 'w') as f:
    json.dump(docs_contents, f, indent=2)