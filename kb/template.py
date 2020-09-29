import frontmatter
from pathlib import Path
import pprint

def get_template(template):
    if template is 'blog':
        return 'blog.md' 
    elif template is 'notable':
        return 'notable.md'
    else:
        return 'default.md'
    
def load(template, title, categories, author):
    path = str(Path('kb','templates', get_template(template)))
    post = frontmatter.load(path)
    post['title'] = title
    post['categories'] = categories
    post['author'] = author
    return post

def export(post):
    return frontmatter.dumps(post, default_flow_style=None, allow_unicode=True)
