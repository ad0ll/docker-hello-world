import requests
import json
def write_response(data: str,message: str =""):
    # pathlib.Path("/run/result").mkdir(parents=True, exist_ok=True)
    result_json = json.dumps({
        "bounty_data": {
            "result": data,
            "message": message
        }
    })
    print(result_json)
    with open("result.json", "w") as f:
        f.write(result_json)

if __name__ == '__main__':
    try:
        # Index 12 is ETH/USDT, use res.data[12].weightedAvgPrice
        resp = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
        elems = resp.json()
        write_response(elems[12]["weightedAvgPrice"], "this is a test message")
    except Exception as e:
        message = e.message if hasattr(e, 'message') else ""
        write_response("", message=message)
