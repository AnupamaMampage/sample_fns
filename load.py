import json
from urllib.request import urlopen
from time import time


def load(event, context):
    link = 'https://raw.githubusercontent.com/AnupamaMampage/sample_fns/main/data.json' # https://github.com/jdorfman/awesome-json-datasets
    
    start = time()
    f = urlopen(link)
    try:
        data = f.read().decode("utf-8","ignore")   
    except json.decoder.JSONDecodeError:
        error = "error"
    
    
    network = time() - start

    start = time()
    json_data = json.loads(data)
    str_json = json.dumps(json_data, indent=4)
    latency = time() - start

    # print(str_json)
    return {"network": network, "serialization": latency}

