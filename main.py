import sys

import requests
import json
import time

def write_response(data, result_message):
    # pathlib.Path("/run/result").mkdir(parents=True, exist_ok=True)
    result_json = json.dumps({
        "bounty_data": {
            "result": data,
            "message": result_message
        }
    })
    print(result_json)
    with open("result.json", "w") as f:
        f.write(result_json)

if __name__ == '__main__':
    print("Running with %s" % sys.argv)
    forceable_outcomes = ["EXPECTED_ERROR", "UNEXPECTED_ERROR", "MALFORMED_RESULT", "NO_RESULT", "TIMEOUT"]
    force_result = "" #Optionally pass "EXPECTED_ERROR", "UNEXPECTED_ERROR", "MALFORMED_RESULT", "ADDITIONAL_FIELDS"
    if len(sys.argv) >= 2:
        force_result = sys.argv[1]
        print("Received instruction to force outcome: %s" % force_result)
    if force_result != "" and force_result not in forceable_outcomes:
        raise Exception(format("InputError: provided arg %s not one of %s" % (force_result, forceable_outcomes)))

    if force_result == "UNEXPECTED_ERROR":
        raise Exception("This is an UNEXPECTED_ERROR")

    try:
        if force_result == "EXPECTED_ERROR":
            raise Exception("This is an EXPECTED_ERROR")
        if force_result == "TIMEOUT":
            time.sleep(1*60*60)  # We don't know what the bounty or universal timeout are, so just sleep for an hour
        if force_result == "MALFORMED_RESULT":
            write_response({
                "a": {
                    "b": "c"
                }
            }, 9001)  # This will write a result with an Object as "result" and a number as message

        # Index 12 is ETH/USDT, use res.data[12].weightedAvgPrice
        resp = requests.get("https://api2.binance.com/api/v3/ticker/24hr")
        elems = resp.json()
        if force_result == "NO_RESULT":
            print("Not printing result because of NO_RESULT condition")
        else:
            write_response(elems[12]["weightedAvgPrice"], "this is a test message")
    except Exception as e:
        print(e)
        message = e.message if hasattr(e, 'message') else ""
        write_response("", message)
