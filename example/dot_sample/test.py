import requests

def save_dot_png(dot_txt ,output_dir):
    url = "https://quickchart.io/graphviz"

    with open(dot_txt, "r")as f:      
        dot_data = f.read() 
    payload = {
        "graph":dot_data, 
        "format":"png"
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:

        with open(output_dir, "wb") as f: 
            f.write(response.content)
        
    else:
        print(f"Error: {response.status_code}")

dot_txt = "/app/example/sample.dot"
save_dot_png(dot_txt, "/app/output/graph.png")