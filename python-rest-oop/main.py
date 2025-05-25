from plugins.uppercase_plugin import UppercasePlugin
from plugins.remove_whitespace_plugin import RemoveWhitespacePlugin
from api_client import MockAPIClient

def main():
    client = MockAPIClient(base_url="https://mockapi.io/demo")
    raw_data = client.fetch_data()

    plugins = [RemoveWhitespacePlugin(), UppercasePlugin()]
    processed_data = raw_data
    for plugin in plugins:
        processed_data = plugin.run(processed_data)

    client.post_result(processed_data)
    print("Processing complete:", processed_data)

if __name__ == "__main__":
    main()
