# convert user text in slug

title = input('Enter your title: ')

def slugify(text):
    slug = text.strip().replace(' ', '-')
    while '--' in slug:
        slug = slug.replace('--', '-')
    return slug

print(slugify(title))