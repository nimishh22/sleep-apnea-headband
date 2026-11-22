import argparse
import json
from pathlib import Path
import pandas as pd
from .io import load_recording
from .features import extract_window_features
from .detector import score_candidate
from .evaluation import evaluate_predictions

def main():
    parser = argparse.ArgumentParser(prog="sleepband", description="Research recording inspection tools")
    sub = parser.add_subparsers(dest="command", required=True)
    inspect = sub.add_parser("inspect", help="summarize a sensor CSV")
    inspect.add_argument("csv", type=Path)
    evaluate = sub.add_parser("evaluate", help="evaluate labelled predictions CSV")
    evaluate.add_argument("csv", type=Path)
    args = parser.parse_args()

    if args.command == "inspect":
        frame = load_recording(args.csv)
        features = extract_window_features(frame)
        print(json.dumps({
            "rows": len(frame),
            "duration_s": float(frame.timestamp_s.iloc[-1] - frame.timestamp_s.iloc[0]) if len(frame) > 1 else 0.0,
            "features": features,
            "experimental_candidate_score": score_candidate(features),
            "notice": "Research-only score; not a diagnosis."
        }, indent=2, allow_nan=True))
    elif args.command == "evaluate":
        frame = pd.read_csv(args.csv)
        print(json.dumps(evaluate_predictions(frame), indent=2))

if __name__ == "__main__":
    main()
