import yaml

def load_config(path="configs/default.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    print("Pipeline initialized")
    print(config)

if __name__ == "__main__":
    main()

