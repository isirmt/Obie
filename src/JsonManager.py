import json


JSON_PATH = "data/target.json"
JSON_PATH_W = "data/target.json"


def load(jsonFile=JSON_PATH):
    """Load json from jsonFile to dict. (default is JSON_PATH)"""
    return json.load(open(jsonFile, encoding="utf-8_sig"))


def save(data, jsonFile=JSON_PATH_W):
    """Damp to json from data(dict). (default is JSON_PATH_W)"""
    json.dump(
        data, open(jsonFile, "w", encoding="utf-8_sig"), ensure_ascii=False, indent=4
    )


def getByDictionary(id, Dictionary):
    data = load().get("targetList", None)[id]
    for i in Dictionary["attribute"]:
        Dictionary["attribute"][i] = data.get("attribute", None)[i]


def SaveDictionary(dict, jsonFile=JSON_PATH_W):
    data = load()
    id = -1
    num = 1
    for i in data.get("targetList", None):
        num += 1
        if dict.get("id") == i.get("id"):
            id = dict.get("id")
    if id != -1:
        del data.get("targetList", None)[id]
    data.get("targetList", None).append(dict)
    data["num"] = num
    save(data, jsonFile)


if __name__ == "__main__":
    test = {
        "id": 0,
        "attribute": {
            "kind": None,
            "amount": None,
            "Period": None,
            "repeat": None,
            "active": None,
        },
    }
    test2 = {
        "id": 3,
        "attribute": {
            "kind": "食事",
            "amount": 12121,
            "Period": None,
            "repeat": None,
            "active": None,
        },
    }
    test3 = {
        "id": 4,
        "attribute": {
            "kind": "食事",
            "amount": 121211,
            "Period": None,
            "repeat": None,
            "active": None,
        },
    }
    print("old is " + str(test))
    getByDictionary(test.get("id"), test)
    print("new is " + str(test))
    print()
    print("old is \n" + str(load()))
    SaveDictionary(test2)
    print("new is \n" + str(load()))
    print()
    print("old is \n" + str(load()))
    SaveDictionary(test3)
    print("new is \n" + str(load()))
