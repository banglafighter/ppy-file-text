import re


class StringUtil:

    @staticmethod
    def underscore_to_camelcase(word, sign="_"):
        return ''.join(x.capitalize() or sign for x in word.split(sign))

    @staticmethod
    def find_replace_into_text(content: str, key_value: dict):
        for key in key_value:
            value = key_value[key]
            if not value:
                value = ""
            content = content.replace(key, value)
        return content

    @staticmethod
    def camelcase_to(text: str, to: str = "_"):
        return re.sub(r'(?<!^)(?=[A-Z])', to, text)

    @staticmethod
    def remove_special_character(text: str, to: str = ""):
        return re.sub(r'[^\w\s/\-]', to, text)

    @staticmethod
    def text_to_url_text(text: str):
        text = StringUtil.camelcase_to(text, "-")
        text = StringUtil.find_and_replace_with(text, " ", "-")
        text = StringUtil.find_and_replace_with(text, "_", "-")
        text = StringUtil.remove_special_character(text)
        text = text.strip()
        text = text.strip("-")
        text = text.lower()
        return text

    @staticmethod
    def camelcase_to_lower(text: str, to: str = "_"):
        return StringUtil.camelcase_to(text, to).lower()

    @staticmethod
    def replace_space_with(text: str, to: str = "_"):
        return re.sub('\s+', to, text)

    @staticmethod
    def find_and_replace_with(text: str, find: any, replace: any):
        return text.replace(find, replace)

    @staticmethod
    def human_readable(text: str):
        text = StringUtil.camelcase_to(text, " ")
        text = StringUtil.find_and_replace_with(text, "-", " ")
        text = text.strip()
        text = text.title()
        return text

    @staticmethod
    def system_readable(text: str):
        text = StringUtil.camelcase_to(text, "_")
        text = StringUtil.find_and_replace_with(text, " ", "_")
        text = text.strip()
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9_]', '', text)
        return text
