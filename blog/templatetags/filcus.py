from googletrans import Translator
from django.utils.text import slugify
from django import template

register = template.Library()

def translate_hindi_to_english(hindi_text):
    translator = Translator()
    translation = translator.translate(hindi_text, src='hi', dest='en')
    english_text = translation.text
    return english_text

@register.filter(name='cuslug')
def cuslug(value):
    translated_text = translate_hindi_to_english(value)
    slugified_text = slugify(translated_text)
    return slugified_text

