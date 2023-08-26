from ppy_common import PPyCException
from ppy_file_text import FileUtil


class TextFileMan:
    @staticmethod
    def get_text_from_file(file_path, exception_message: str = "Invalid File"):
        if not FileUtil.is_exist(file_path):
            raise PPyCException(exception_message)
        with open(file_path, 'r', encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def write_text_to_file(file_path, text_content):
        FileUtil.delete(file_path)
        try:
            stream = open(file_path, 'w', encoding="utf-8")
            stream.write(text_content)
            stream.close()
            return True
        except Exception as e:
            return False

    @staticmethod
    def write_text_file_specific_index(file_path, index, text_content):
        try:
            stream = open(file_path, 'r+', encoding="utf-8")
            lines = stream.readlines()
            lines.insert(index, text_content)
            stream.seek(0)
            stream.writelines(lines)
            stream.close()
        except Exception as e:
            return False

    @staticmethod
    def find_replace_text_content(file_path, find_replace_list_of_dict: list):
        text_content = TextFileMan.get_text_from_file(file_path)
        for find_replace_dict in find_replace_list_of_dict:
            if "find" in find_replace_dict and "replace" in find_replace_dict:
                text_content = text_content.replace(find_replace_dict["find"], find_replace_dict["replace"])

        if text_content:
            TextFileMan.write_text_to_file(file_path, text_content)
