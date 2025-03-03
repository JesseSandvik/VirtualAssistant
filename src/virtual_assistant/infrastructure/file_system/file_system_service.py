import json
import yaml

from typing import Any, Dict

class FileSystemService:

    @staticmethod
    def get_json_file_content(json_file_path: str) -> Dict[str, Any]:
        with open(json_file_path) as file:
            file_content = json.load(file)
        return file_content

    @staticmethod
    def get_yaml_file_contents(yaml_file_path: str) -> Any:
        with open(yaml_file_path) as file:
            file_content = yaml.safe_load(file)
        return file_content
