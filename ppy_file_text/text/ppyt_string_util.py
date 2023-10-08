import re
from copy import copy


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
        text = str(text)
        text = text.strip()
        text = re.sub(r'(?<!^)(?=[A-Z])', to, text)
        return text

    @staticmethod
    def remove_special_character(text: str, to: str = ""):
        return re.sub(r'[^\w\s/\-]', to, text)

    @staticmethod
    def text_to_url_text(text: str):
        text = StringUtil.camelcase_to(copy(text), "-")
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
        text = copy(text)
        return text.replace(find, replace)

    @staticmethod
    def human_readable(text: str):
        text = StringUtil.camelcase_to(copy(text), " ")
        text = StringUtil.find_and_replace_with(text, "-", " ")
        text = text.strip()
        text = text.title()
        return StringUtil.replace_space_with(text, " ")

    @staticmethod
    def replace_multiple_occurrence_to_single_with(text: str, to: str = "_"):
        return re.sub(f"{to}+", to, text)

    @staticmethod
    def system_readable(text: str):
        text = StringUtil.camelcase_to(copy(text), "_")
        text = StringUtil.find_and_replace_with(text, " ", "_")
        text = StringUtil.replace_multiple_occurrence_to_single_with(text=text, to="_")
        text = text.strip()
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9_]', '', text)
        return text

    @staticmethod
    def remove_leading_number(text: str):
        return re.sub("^\d+", '', text)

    @staticmethod
    def lower_first_char(text: str):
        if not text:
            return ""
        text = str(text)
        return text[0].lower() + text[1:]

    @staticmethod
    def py_underscore_name(name: str):
        name = StringUtil.lower_first_char(text=name)
        name = StringUtil.system_readable(name)
        name = StringUtil.remove_special_character(name)
        name = StringUtil.remove_leading_number(name)
        return name

    @staticmethod
    def py_hyphen_name(name: str):
        name = StringUtil.py_underscore_name(name=name)
        name = StringUtil.find_and_replace_with(text=name, find="_", replace="-")
        return name

    @staticmethod
    def py_class_name(name: str):
        name = StringUtil.py_underscore_name(name=name)
        name = StringUtil.underscore_to_camelcase(word=name)
        return name
