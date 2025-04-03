import json




if __name__ == "__main__":
    final_state = {"a":1}

    results_json = json.dumps(final_state, ensure_ascii=False, indent=4)
    print(results_json)
