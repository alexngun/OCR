#%%
import yaml
import json
import re
import os

#%%

class fieldExtractor:

    def __init__(self, template_directory:str, texts:list) -> None:

        self.dir = template_directory
        self.texts = texts
        self.templates = self.__load_templates()

    def __load_templates(self):

        """"
        Load all templates from a directory
        A valid template must have 'keywords', 'exclude_keywords',
        'fields', and 'fields' are the data that we are interested to
        extract from the invoice. 
        """

        templates = []

        for file in os.listdir(self.dir):
            if file.endswith('.yml'):
                with open(self.dir+'/'+file, 'r') as stream:
                    try:
                        template = yaml.safe_load(stream)
                    except:
                        pass
                templates.append(template)

        return templates

    def __keyword_match(self, text, template):
        
        for keyword in template['keywords']:
            if re.search(keyword, text):
                return True
        return False

    def __exkeyword_match(self, text, template):

        for keyword in template['exclude_keywords']:
            if re.search(keyword, text):
                return True
        return False

    def __template_search(self, text):

        for template in self.templates:
            if self.__exkeyword_match(text, template):
                return False
            if self.__keyword_match(text, template):
                return template
    
        print("Error: No valid template was found!")
        return False

    def fetch(self) -> dict:

        data = {'invoice_number':[], 'amount':[], 'date':[]}

        for text in self.texts:
            template = self.__template_search(text)
            for field in template['fields']:
                data[field].append(re.search(template['fields'][field], text)[0])

        return data

    def save(self, entry:dict, fname='data') -> None:

        a = []
        path = 'Data/'+fname+'.json'
        if not os.path.isfile(path):
            a.append(entry)
            with open(path, mode='w') as f:
                f.write(json.dumps(a, indent=2))
        else:
            with open(path) as feedsjson:
                feeds = json.load(feedsjson)
            feeds.append(entry)
            with open(path, mode='w') as f:
                f.write(json.dumps(feeds, indent=2))


# %%
