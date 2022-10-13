import requests
import os
import pathlib

def write_response(data: str, failed: bool = False, message: str =""):
    # pathlib.Path("/run/result").mkdir(parents=True, exist_ok=True)
    with open("result.json", "w") as f:
        f.write(f"""{{
                    "result": "{data}",
                    "failed": "{failed}",
                    "message": "{message}"
                }}""")

if __name__ == '__main__':
    try:
        # Index 12 is ETH/USDT, use res.data[12].weightedAvgPrice
        resp = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
        # See PyCharm help at https://www.jetbrains.com/help/pycharm/
        elems = resp.json()
        write_response(elems[12]["weightedAvgPrice"])
    except Exception as e:
        message = e.message if hasattr(e, 'message') else ""
        write_response("", failed=True, message=message)
