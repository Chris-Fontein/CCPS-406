import yaml


def yaml_loader(filepath):
    # Loads the Items YAML file
    with open(filepath, "r") as file_descriptor:
       data = yaml.load(file_descriptor)
    return data


if __name__ == "__main__":
    filepath = "test.yaml"
    data = yaml_loader(filepath)
    print data

    items = data.get('items')

    


