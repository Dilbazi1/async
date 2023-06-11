from yaml.loader import Loader
import yaml
action_dict={
    'key1':[1,2,3],
    'key2':213,
    'key3':{'k1':'10\u20B0',
            'k2':"10\u20AC"
}
}
with open ("file.yaml", 'w') as f_n:
    yaml.dump(action_dict, f_n, default_flow_style=False, allow_unicode=True)
with open ('file.yaml','r',encoding='utf8') as f_n:
     f_n_content=yaml.load(f_n,Loader)
     for key,value in f_n_content.items():
         assert value==action_dict[key]