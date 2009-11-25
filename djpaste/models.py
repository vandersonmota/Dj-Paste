from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LANGUAGES = (('text', 'Text'),
             ('python','Python'),                   
)

class Snippet(models.Model):
    code = models.TextField(max_length=5000)
    language = models.CharField(max_length=15, choices=LANGUAGES, default='text')
    
    def highlighted_code(self):
        lexer = get_lexer_by_name(self.language)
        return highlight(self.code, lexer, HtmlFormatter())
        