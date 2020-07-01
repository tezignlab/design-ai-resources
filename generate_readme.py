import os
import re


def get_md_info(path, type_name):
    info = {}
    f = open(path, 'r', encoding='utf-8')
    data = f.readlines()
    data = [item.strip() for item in data]
    data = ''.join(data)

    for item in part_row_content[type_name]:
        try:
            info[item] = re.search(r'###\s' + show_name[item].replace(' ', '\s') + r'([^#]*)', data).group(1)
        except Exception as e:
            print(item, e)
            info[item] = ''

    info['title'] = re.search(r'#\s([^#{1,3}]*)#', data).group(1)

    return info


readme = open('README.md', 'w', encoding='utf-8')

part_head = {
    'paper': '| Name | Title | Description | Publication | Links |  \n| --- | --- | --- | --- | --- |  ',
    'dataset': '| Name | Title | Description | Scale | Annotation | Links |  \n| --- | --- | --- | --- | --- | --- |  ',
    'event': '',
    'company': '',
    'repo': ''
}

part_row_content = {
    'paper': ['title', 'desc', 'pub', 'paper_link', 'project_link'],
    'dataset': ['title', 'desc', 'scale', 'annotation', 'paper_link', 'project_link'],
    'event': [],
    'company': [],
    'repo': []
}

show_name = {
    'title': 'Title',
    'desc': 'Description',
    'pub': 'Publication',
    'paper_link': 'Paper Link',
    'project_link': 'Project Link',
    'scale': 'Scale',
    'annotation': 'Annotation'
}

def generate(type_name):
    print(part_head[type_name], file=readme)
    
    for item in os.listdir('./' + type_name):
        temp_path = os.path.join('./' + type_name, item)
        info = get_md_info(temp_path, type_name)

        non_link_num = 0

        link_col = ''
        temp_row = '| ' + item.split('.')[0]
        for i in part_row_content[type_name]:
            if 'link' in i:
                link_col += ' [[%s](%s)]' % (i.split('_')[0], info[i])
            else:
                temp_row += (' | ' + info[i])
        
        link_col += ' [[note](...)]'
        temp_row += ' | ' + link_col + ' |  '

        print(temp_row, file=readme)


# start of generation

print('# AI Design Papers\n', file=readme)

print('## 📃Paper\n', file=readme)
generate('paper')

print('\n## 🎯Dataset\n', file=readme)
generate('dataset')
