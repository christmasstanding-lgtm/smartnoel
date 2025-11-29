import base64
import datetime

def encode_string(s):
    return base64.b64encode(s.encode("utf-8")).decode("utf-8")

def decode_string(s):
    return base64.b64decode(s.encode("utf-8")).decode("utf-8")

def get_current_year():
    return datetime.datetime.now().year

def is_christmas_season():
    current_month = datetime.datetime.now().month
    return current_month in [11, 12]

def print_christmas_message():
    encoded_message = encode_string("Merry Christmas and Happy New Year!")
    decoded_message = decode_string(encoded_message)
    print(decoded_message)

def main():
    if is_christmas_season():
        print_christmas_message()
    else:
        print("It's not the Christmas season.")

if __name__ == "__main__":
    main()
