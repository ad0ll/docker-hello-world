#!/bin/zsh

#     forceable_outcomes = ["EXPECTED_ERROR", "UNEXPECTED_ERROR", "MALFORMED_RESULT", "NO_RESULT", "TIMEOUT"]
python main.py
python main.py "EXPECTED_ERROR"
python main.py "UNEXPECTED_ERROR"
python main.py "MALFORMED_RESULT"
python main.py "NO_RESULT"
#python main.py "TIMEOUT"