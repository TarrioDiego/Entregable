from extract import extract
from transform import transform
from load import load

if __name__ == '__main__':
    data = extract()
    data = transform()
    load(data)