import os
import re


def get_md_info(path, type_name):
    info = {}
    f = open(path, 'r', encoding='utf-8')
    raw_data = f.readlines()
    data = [item.strip() for item in raw_data]
    data = ''.join(data)

    for item in part_row_content[type_name]:
        if item == 'title':
            continue

        try:
            info[item] = re.search(r'###\s' + show_name[item].replace(' ', '\s') + r'([^#]*)', data).group(1)
        except Exception as e:
            print('%s: format is not correct. Exception is "%s".' % (path, e))
            info[item] = ''

    info['title'] = raw_data[0][2:-1]

    return info


readme = open('README.md', 'w', encoding='utf-8')

part_head = {
    'paper': '| Name | Title | Description | Publication | Links |  \n| --- | --- | --- | --- | --- |  ',
    'dataset': '| Name | Title | Description | Scale | Annotation | Links |  \n| --- | --- | --- | --- | --- | --- |  ',
    'event': '| Name | Title | Description | Links | \n| --- | --- | --- | --- |  ',
    'organization': '| Name | Description | Links | \n| --- | --- | --- |  ',
    'repo': '| Name | Description | Links | \n| --- | --- | --- |  '
}

part_row_content = {
    'paper': ['title', 'desc', 'pub', 'paper_link', 'project_link'],
    'dataset': ['title', 'desc', 'scale', 'annotation', 'paper_link', 'project_link'],
    'event': ['title', 'desc', 'event_link'],
    'organization': ['desc', 'organization_link'],
    'repo': ['desc', 'repo_link']
}

show_name = {
    'title': 'Title',
    'desc': 'Description',
    'pub': 'Publication',
    'paper_link': 'Paper Link',
    'project_link': 'Project Link',
    'scale': 'Scale',
    'annotation': 'Annotation',
    'event_link': 'Event Link',
    'repo_link': 'Repo Link',
    'organization_link': 'Organization Link'
}

def generate(type_name):
    print(part_head[type_name], file=readme)
    
    for item in os.listdir('./' + type_name):
        if item.split('.')[-1] != 'md' or item == 'template.md':
            continue

        temp_path = os.path.join('./' + type_name, item)
        info = get_md_info(temp_path, type_name)

        link_col = ''
        temp_row = '| ' + item[:-3]
        for i in part_row_content[type_name]:
            if 'link' in i:
                if info[i] == '':
                    link_col += ' [%s]' % (i.split('_')[0])
                else:
                    link_col += ' [[%s](%s)]' % (i.split('_')[0], info[i])
            else:
                temp_row += (' | ' + info[i])
        
        # TODO: add the link of note
        link_col += ' [[note]()]'
        temp_row += ' | ' + link_col + ' |  '

        print(temp_row, file=readme)


# start of generation

print('# ✔AI Design Papers\n', file=readme)

print('## 📃Paper\n', file=readme)
generate('paper')

print('\n## 🎯Dataset\n', file=readme)
generate('dataset')

print('\n## 🎈Event\n', file=readme)
generate('event')

print('\n## 🏢Organization\n', file=readme)
generate('organization')

print('\n## 📂Repo\n', file=readme)
generate('repo')

print('---\n', file=readme)
# add how to contribution to the bottom

print('\n', file=readme)
f = open('contribute.md', 'r', encoding='utf-8')
for line in f.readlines():
    print(line, end='', file=readme)
